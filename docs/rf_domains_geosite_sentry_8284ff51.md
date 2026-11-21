# sentry

Актуальный набор доменных правил «sentry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `sentry`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_sentry_8284ff51.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_sentry_8284ff51.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-sentry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: getsentry.com
domain_suffix: sentry-cdn.com
domain_suffix: sentry.dev
domain_suffix: sentry.io
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
