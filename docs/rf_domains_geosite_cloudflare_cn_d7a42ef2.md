# cloudflare-cn

Актуальный набор доменных правил «cloudflare-cn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cloudflare-cn`. Тип: **domains**.

Правил: **19**. Точные домены: 0; доменные зоны: 19; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cloudflare_cn_d7a42ef2.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cloudflare_cn_d7a42ef2.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cloudflare-cn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: cf-china.info
domain_suffix: cf-ns.com
domain_suffix: cf-ns.net
domain_suffix: cf-ns.site
domain_suffix: cf-ns.tech
domain_suffix: cftest5.cn
domain_suffix: cftest6.cn
domain_suffix: cftest7.com
domain_suffix: cftest8.com
domain_suffix: cloudflare-cn.com
domain_suffix: cloudflareanycast.net
domain_suffix: cloudflarechina.cn
domain_suffix: cloudflarecn.net
domain_suffix: cloudflareglobal.net
domain_suffix: cloudflareinsights-cn.com
domain_suffix: cloudflareperf.com
domain_suffix: cloudflareprod.com
domain_suffix: cloudflarestaging.com
domain_suffix: cloudflarestoragegw.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
