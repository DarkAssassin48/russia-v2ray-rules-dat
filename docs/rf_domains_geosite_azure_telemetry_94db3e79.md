# azure@telemetry

Актуальный набор доменных правил «azure@telemetry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `azure@telemetry`. Тип: **domains**.

Правил: **3**. Точные домены: 2; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_azure_telemetry_94db3e79.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_azure_telemetry_94db3e79.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-azure@telemetry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: dc.applicationinsights.azure.com
domain: live.applicationinsights.azure.com
domain_suffix: in.applicationinsights.azure.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
