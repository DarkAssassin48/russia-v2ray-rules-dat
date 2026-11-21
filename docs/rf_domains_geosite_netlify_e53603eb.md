# netlify

Актуальный набор доменных правил «netlify» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `netlify`. Тип: **domains**.

Правил: **10**. Точные домены: 3; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_netlify_e53603eb.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_netlify_e53603eb.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-netlify.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: acd89244c803f7181.awsglobalaccelerator.com
domain: afa7f374f51cc8991.awsglobalaccelerator.com
domain: d33wubrfki0l68.cloudfront.net
domain_suffix: bitballoon.com
domain_suffix: netlify.app
domain_suffix: netlify.com
domain_suffix: netlifydns.com
domain_suffix: netlifystatus.com
domain_suffix: netlifyusercontent.com
domain_suffix: ntl.fyi
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
