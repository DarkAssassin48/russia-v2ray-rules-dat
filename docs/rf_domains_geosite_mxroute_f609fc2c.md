# mxroute

Актуальный набор доменных правил «mxroute» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `mxroute`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_mxroute_f609fc2c.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_mxroute_f609fc2c.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-mxroute.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: mxlogin.com
domain_suffix: mxroute.com
domain_suffix: mxroutedocs.com
domain_suffix: mxroutehelp.com
domain_suffix: mxrouting.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
