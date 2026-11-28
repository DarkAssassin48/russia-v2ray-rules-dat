# wistia

Актуальный набор доменных правил «wistia» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `wistia`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_wistia_d05067e5.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_wistia_d05067e5.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-wistia.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: embedwistia-a.akamaihd.net
domain_suffix: wistia.com
domain_suffix: wistia.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
