# mailcom

Актуальный набор доменных правил «mailcom» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `mailcom`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_mailcom_6f56670f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_mailcom_6f56670f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-mailcom.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: mail.com
domain_suffix: ui-portal.de
domain_suffix: uicdn.com
domain_suffix: uimserv.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
