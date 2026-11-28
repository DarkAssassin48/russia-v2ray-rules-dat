# sling

Актуальный набор доменных правил «sling» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `sling`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_sling_f0a5138b.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_sling_f0a5138b.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-sling.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: dishworld.com
domain_suffix: movenetworks.com
domain_suffix: movetv.com
domain_suffix: sling.com
domain_suffix: slinginternational.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
