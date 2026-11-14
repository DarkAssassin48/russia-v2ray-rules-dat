# javdb

Актуальный набор доменных правил «javdb» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `javdb`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_javdb_b8450a9d.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_javdb_b8450a9d.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-javdb.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: jav.app
domain_suffix: javdb.com
domain_suffix: jdbimgs.com
domain_suffix: jdbstatic.com
domain_regex: (^|\.)javdb\d+\.com$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
