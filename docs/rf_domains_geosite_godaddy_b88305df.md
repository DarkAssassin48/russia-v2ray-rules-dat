# godaddy

Актуальный набор доменных правил «godaddy» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `godaddy`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_godaddy_b88305df.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_godaddy_b88305df.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-godaddy.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: .godaddy
domain_suffix: godaddy.com
domain_suffix: godaddy.net
domain_suffix: wsimg.com
domain_suffix: x.co
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
