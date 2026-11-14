# viu

Актуальный набор доменных правил «viu» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `viu`. Тип: **domains**.

Правил: **7**. Точные домены: 4; доменные зоны: 2; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_viu_95f03925.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_viu_95f03925.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-viu.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: api.viu.now.com
domain: d1k2us671qcoau.cloudfront.net
domain: d2anahhhmp1ffz.cloudfront.net
domain: dfp6rglgjqszk.cloudfront.net
domain_suffix: viu.com
domain_suffix: viu.tv
domain_regex: ^ewcdn[0-9]+\.nowe\.com$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
