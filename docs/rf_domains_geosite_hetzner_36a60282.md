# hetzner

Актуальный набор доменных правил «hetzner» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hetzner`. Тип: **domains**.

Правил: **15**. Точные домены: 1; доменные зоны: 14; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hetzner_36a60282.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hetzner_36a60282.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hetzner.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: sentry.hetzner.company
domain_suffix: first-ns.de
domain_suffix: hetzner-cloud.de
domain_suffix: hetzner.cloud
domain_suffix: hetzner.com
domain_suffix: hetzner.company
domain_suffix: hetzner.de
domain_suffix: hetzner.social
domain_suffix: htznr.li
domain_suffix: second-ns.com
domain_suffix: second-ns.de
domain_suffix: your-objectstorage.com
domain_suffix: your-server.de
domain_suffix: your-storagebox.de
domain_suffix: your-storageshare.de
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
