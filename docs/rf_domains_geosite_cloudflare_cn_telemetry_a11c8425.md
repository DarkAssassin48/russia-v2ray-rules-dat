# cloudflare-cn@telemetry

Актуальный набор доменных правил «cloudflare-cn@telemetry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cloudflare-cn@telemetry`. Тип: **domains**.

Правил: **1**. Точные домены: 0; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cloudflare_cn_telemetry_a11c8425.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cloudflare_cn_telemetry_a11c8425.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cloudflare-cn@telemetry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: cloudflareinsights-cn.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
