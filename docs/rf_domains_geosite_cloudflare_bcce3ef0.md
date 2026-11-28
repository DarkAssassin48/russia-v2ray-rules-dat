# cloudflare

Актуальный набор доменных правил «cloudflare» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cloudflare`. Тип: **domains**.

Правил: **76**. Точные домены: 0; доменные зоны: 76; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cloudflare_bcce3ef0.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cloudflare_bcce3ef0.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cloudflare.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: argotunnel.com
domain_suffix: browser.run
domain_suffix: cf-china.info
domain_suffix: cf-ipfs.com
domain_suffix: cf-ns.com
domain_suffix: cf-ns.net
domain_suffix: cf-ns.site
domain_suffix: cf-ns.tech
domain_suffix: cfargotunnel.com
domain_suffix: cfdata.org
domain_suffix: cfl.re
domain_suffix: cftest5.cn
domain_suffix: cftest6.cn
domain_suffix: cftest7.com
domain_suffix: cftest8.com
domain_suffix: cloudflare-cn.com
domain_suffix: cloudflare-dns.com
domain_suffix: cloudflare-ech.com
domain_suffix: cloudflare-esni.com
domain_suffix: cloudflare-gateway.com
domain_suffix: cloudflare-ipfs.com
domain_suffix: cloudflare-quic.com
domain_suffix: cloudflare-terms-of-service-abuse.com
domain_suffix: cloudflare.app
domain_suffix: cloudflare.com
domain_suffix: cloudflare.dev
domain_suffix: cloudflare.net
domain_suffix: cloudflare.pay
domain_suffix: cloudflare.tv
domain_suffix: cloudflareaccess.com
domain_suffix: cloudflareanycast.net
domain_suffix: cloudflareapps.com
domain_suffix: cloudflarebolt.com
domain_suffix: cloudflarebrowser.com
domain_suffix: cloudflarechallenge.com
domain_suffix: cloudflarechina.cn
domain_suffix: cloudflareclient.com
domain_suffix: cloudflarecn.net
domain_suffix: cloudflarecp.com
domain_suffix: cloudflareglobal.net
domain_suffix: cloudflareinsights-cn.com
domain_suffix: cloudflareinsights.com
domain_suffix: cloudflareok.com
domain_suffix: cloudflarepartners.com
domain_suffix: cloudflareperf.com
domain_suffix: cloudflareportal.com
domain_suffix: cloudflarepreview.com
domain_suffix: cloudflareprod.com
domain_suffix: cloudflareregistrar.com
domain_suffix: cloudflareresearch.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
