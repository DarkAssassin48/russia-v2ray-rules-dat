# fastly

Актуальный набор доменных правил «fastly» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `fastly`. Тип: **domains**.

Правил: **7**. Точные домены: 0; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_fastly_682a01c1.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_fastly_682a01c1.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-fastly.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: fastly-edge.com
domain_suffix: fastly-terrarium.com
domain_suffix: fastly.com
domain_suffix: fastly.io
domain_suffix: fastly.net
domain_suffix: fastlylabs.com
domain_suffix: fastlylb.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
