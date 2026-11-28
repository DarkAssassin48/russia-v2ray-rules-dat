# adblock

Актуальный набор доменных правил «adblock» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `adblock`. Тип: **domains**.

Правил: **2**. Точные домены: 0; доменные зоны: 2; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_adblock_fd9bcab6.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_adblock_fd9bcab6.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-adblock.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: adblockcdn.com
domain_suffix: getadblock.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
