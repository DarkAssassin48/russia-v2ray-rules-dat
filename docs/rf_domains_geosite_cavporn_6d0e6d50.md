# cavporn

Актуальный набор доменных правил «cavporn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cavporn`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 2; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cavporn_6d0e6d50.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cavporn_6d0e6d50.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cavporn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: cavporn.com
domain_suffix: cavporn.github.io
domain_regex: (^|\.)cav1(0[2-9]|1[0-9])\.com$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
