# bilibili2

Актуальный набор доменных правил «bilibili2» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `bilibili2`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_bilibili2_6edf982d.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_bilibili2_6edf982d.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-bilibili2.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: bili2.cc
domain_suffix: bili888.com
domain_suffix: bili999.com
domain_regex: (^|\.)bilibili3(0[1-9]|1[0-2])\.xyz$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
