# speedtest@ads

Актуальный набор доменных правил «speedtest@ads» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `speedtest@ads`. Тип: **domains**.

Правил: **1**. Точные домены: 0; доменные зоны: 0; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_speedtest_ads_f7ff15fc.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_speedtest_ads_f7ff15fc.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-speedtest@ads.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_regex: ^speed\.(coe|open)\.ad\.[a-z]{2,6}\.prod\.hosts\.ooklaserver\.net$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
