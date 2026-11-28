# snap

Актуальный набор доменных правил «snap» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `snap`. Тип: **domains**.

Правил: **9**. Точные домены: 1; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_snap_6b374f45.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_snap_6b374f45.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-snap.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: impala-media-production.s3.amazonaws.com
domain_suffix: sc-cdn.net
domain_suffix: sc-gw.com
domain_suffix: sc-static.net
domain_suffix: snap-dev.net
domain_suffix: snap.com
domain_suffix: snapads.com
domain_suffix: snapchat.com
domain_suffix: snapkit.co
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
