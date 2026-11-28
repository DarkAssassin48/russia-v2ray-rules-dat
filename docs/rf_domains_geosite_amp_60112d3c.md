# amp

Актуальный набор доменных правил «amp» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `amp`. Тип: **domains**.

Правил: **6**. Точные домены: 2; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_amp_60112d3c.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_amp_60112d3c.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-amp.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: amp.akamaized.net
domain: cdn.ampproject.org
domain_suffix: amp.dev
domain_suffix: ampproject.com
domain_suffix: ampproject.net
domain_suffix: ampproject.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
