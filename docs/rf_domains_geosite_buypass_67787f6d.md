# buypass

Актуальный набор доменных правил «buypass» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `buypass`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_buypass_67787f6d.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_buypass_67787f6d.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-buypass.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: buypass-ssl.com
domain_suffix: buypass.com
domain_suffix: buypass.no
domain_suffix: buypass.se
domain_suffix: minid.no
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
