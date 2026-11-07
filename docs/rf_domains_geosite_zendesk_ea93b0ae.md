# zendesk

Актуальный набор доменных правил «zendesk» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `zendesk`. Тип: **domains**.

Правил: **6**. Точные домены: 0; доменные зоны: 6; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_zendesk_ea93b0ae.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_zendesk_ea93b0ae.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-zendesk.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: outbound.io
domain_suffix: zdassets.com
domain_suffix: zdusercontent.com
domain_suffix: zendesk.com
domain_suffix: zndsk.com
domain_suffix: zopim.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
