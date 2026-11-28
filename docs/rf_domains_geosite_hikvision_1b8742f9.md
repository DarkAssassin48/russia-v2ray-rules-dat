# hikvision

Актуальный набор доменных правил «hikvision» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hikvision`. Тип: **domains**.

Правил: **8**. Точные домены: 0; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hikvision_1b8742f9.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hikvision_1b8742f9.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hikvision.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: eziot.com
domain_suffix: ezviz.com
domain_suffix: hik-cloud.com
domain_suffix: hik-express.com
domain_suffix: hikiot.com
domain_suffix: hikmall.com
domain_suffix: hikvision.com
domain_suffix: ys7.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
