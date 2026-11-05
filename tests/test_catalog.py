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

    def test_compact_catalog_keeps_every_id_group_and_default(self):
        entry={'id':'rf_domains_x','name_ru':'X','format':'srs','source':'runetfreedom','source_name':'Services','default_on':False,'count':2,'url':'https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/sing-box/x.srs'}
        doc={'version':'v1','generated_at':'now','domain_lists':[entry],'categories':[]}
        compact=b.compact_manifest(doc,'DarkAssassin48/russia-v2ray-rules-dat')
        self.assertEqual(compact['domain_lists'][0]['id'],entry['id'])
        self.assertEqual(compact['domain_lists'][0]['source_name'],entry['source_name'])
        self.assertEqual(compact['domain_lists'][0]['url'],'https://darkassassin48.github.io/russia-v2ray-rules-dat/sing-box/x.srs')
        self.assertIs(compact['domain_lists'][0]['default_on'],False)
        self.assertNotIn('count',compact['domain_lists'][0])
        self.assertEqual(doc['domain_lists'][0],entry)

    def test_lite_catalog_includes_all_profiles_and_no_other_entries(self):
        base={'name_ru':'Service','format':'srs','source_name':'Source','default_on':False,'url':'https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/custom/a.srs'}
        doc={'version':'v1','generated_at':'now','domain_lists':[dict(base,id='da_discord_quests'),dict(base,id='rf_domains_discord')],'categories':[dict(base,id='rf_ip_discord')]}
        compact=b.compact_manifest(doc,'DarkAssassin48/russia-v2ray-rules-dat',profiles_only=True)
        self.assertEqual([e['id'] for e in compact['domain_lists']],['da_discord_quests'])
        self.assertEqual(compact['categories'],[])

    def test_medium_keeps_profiles_and_priorities_but_excludes_variants_and_countries(self):
        def entry(key,path):return {'id':key,'url':'https://raw.githubusercontent.com/o/r/release/'+path}
        doc={'domain_lists':[entry('da_discord','custom/discord.srs'),entry('steam','geosite-steam.srs'),entry('youtube','geosite-youtube.srs'),entry('rare','geosite-rare.srs'),entry('ads','geosite-youtube@ads.srs'),entry('all','geosite-geolocation-!cn.srs')],'categories':[entry('us','geoip-us.srs'),entry('telegram_ip','geoip-telegram.srs')]}
        policy={'target_fraction':0.5,'ip_services':['telegram'],'exclude_codes':[],'priority_services':['steam'],'ranked_services':['youtube','rare']}
        selected=b.medium_ids(doc,policy)
        self.assertEqual(selected,{'da_discord','telegram_ip','steam','youtube'})
        doc['domain_lists'].reverse()
        self.assertEqual(b.medium_ids(doc,policy),selected)

    def test_medium_never_drops_ready_profiles_when_input_is_small(self):
        doc={'domain_lists':[{'id':'da_a','url':'https://example.org/custom/a.srs'},{'id':'da_b','url':'https://example.org/custom/b.srs'}],'categories':[]}
        policy={'target_fraction':0.5,'ip_services':[],'exclude_codes':[],'priority_services':[],'ranked_services':[]}
        self.assertEqual(b.medium_ids(doc,policy),{'da_a','da_b'})

if __name__=='__main__':unittest.main()
