# sber@telemetry

Актуальный набор доменных правил «sber@telemetry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `sber@telemetry`. Тип: **domains**.

Правил: **5**. Точные домены: 4; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_sber_telemetry_e917f67e.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_sber_telemetry_e917f67e.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-sber@telemetry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: error-tracking.megamarket.tech
domain: metrics.21-school.ru
domain: sentry.sberauto.com
domain: tracing-http.megamarket.tech
domain_suffix: clickstream.sberbank.ru
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
