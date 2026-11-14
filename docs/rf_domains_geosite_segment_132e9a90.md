# segment

Актуальный набор доменных правил «segment» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `segment`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_segment_132e9a90.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_segment_132e9a90.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-segment.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: segment.com
domain_suffix: segment.io
domain_suffix: segmenthub.com
domain_suffix: segmentify.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
