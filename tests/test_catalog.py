import importlib.util
import unittest
from pathlib import Path

spec=importlib.util.spec_from_file_location("builder",Path(__file__).resolve().parents[1]/"scripts/build_catalog.py")
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class CatalogTests(unittest.TestCase):
    def test_discord_profile_covers_rotating_captcha_hosts(self):
        doc=b.compose_profile({"bases":["discord"],"add_suffix":["hcaptcha.com"]},{"discord":{"rules":[{"domain_suffix":["discord.com","discordapp.com"]}]}})
        suffix=doc['rules'][0]['domain_suffix']
        for host in ['api.hcaptcha.com','newassets.hcaptcha.com','random-next.w.hcaptcha.com','discord.com']:
            self.assertTrue(any(host==x or host.endswith('.'+x) for x in suffix))

    def test_nvidia_app_removes_only_huggingface_zones(self):
        doc=b.compose_profile({"bases":["nvidia"],"exclude_suffix":["huggingface.co","hf.co","hf.space"]},{"nvidia":{"rules":[{"domain_suffix":["nvidia.com","geforce.com","huggingface.co","hf.co","hf.space"],"domain":["nvidia.custhelp.com","cdn.huggingface.co"]}]}})
        self.assertEqual(doc['rules'][0]['domain_suffix'],['geforce.com','nvidia.com'])
        self.assertEqual(doc['rules'][0]['domain'],['nvidia.custhelp.com'])

    def test_logical_and_inverted_sources_are_not_flattened(self):
        for rule in [{"type":"logical","mode":"and","rules":[]},{"invert":True,"domain_suffix":["example.com"]}]:
            with self.assertRaises(ValueError):b.compose_profile({'bases':['x']},{'x':{'rules':[rule]}})

    def test_native_identifier_collisions_are_rejected(self):
        base={"format":"srs","url":"https://raw.githubusercontent.com/owner/repo/release/a.srs","source":"upstream","source_name":"Source","default_on":False}
        doc={'domain_lists':[dict(base,id='a-b'),dict(base,id='a_b')],'categories':[]}
        with self.assertRaises(ValueError):b.validate_manifest(doc,[{},{}])

    def test_default_enabled_and_http_rules_are_rejected(self):
        for extra in [{'default_on':True},{'url':'http://example.com/a.srs'}]:
            entry={'id':'a','format':'srs','url':'https://raw.githubusercontent.com/o/r/release/a.srs','source':'upstream','source_name':'Source','default_on':False,**extra}
            with self.assertRaises(ValueError):b.validate_manifest({'domain_lists':[entry],'categories':[]},[{}])

    def test_text_exports_preserve_matcher_types_and_logical_paths(self):
        doc={'rules':[{'domain':['exact.example'],'domain_suffix':['suffix.example'],'domain_regex':['^ad[0-9]+\\.example$']},{'type':'logical','mode':'and','rules':[{'ip_cidr':['192.0.2.0/24']}]}]}
        text=''.join(b.full_text(doc));counts,unknown=b.summarize(doc)
        self.assertIn('rules[1].rules[0]\tip_cidr\t192.0.2.0/24',text)
        self.assertEqual(counts['total'],4);self.assertEqual(unknown,[])
        self.assertIn('\tdomain_regex\t^ad[0-9]+\\.example$',text)

    def test_generated_identifiers_are_stable_and_different(self):
        self.assertEqual(b.identifier('domains','geosite-nvidia'),b.identifier('domains','geosite-nvidia'))
        self.assertNotEqual(b.identifier('domains','geosite-a-b'),b.identifier('domains','geosite-a_b'))

if __name__=='__main__':unittest.main()
