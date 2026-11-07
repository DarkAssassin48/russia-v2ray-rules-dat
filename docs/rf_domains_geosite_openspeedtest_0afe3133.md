# openspeedtest

Актуальный набор доменных правил «openspeedtest» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `openspeedtest`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_openspeedtest_0afe3133.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_openspeedtest_0afe3133.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-openspeedtest.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: open.cachefly.net
domain_suffix: openspeedtest.com
domain_suffix: openspeedtest.in
domain_suffix: openspeedtest.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
