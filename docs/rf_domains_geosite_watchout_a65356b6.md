# watchout

Актуальный набор доменных правил «watchout» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `watchout`. Тип: **domains**.

Правил: **2**. Точные домены: 0; доменные зоны: 2; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_watchout_a65356b6.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_watchout_a65356b6.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-watchout.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: waa.tw
domain_suffix: watchout.tw
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
