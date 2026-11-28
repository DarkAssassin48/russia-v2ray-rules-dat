# origin

Актуальный набор доменных правил «origin» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `origin`. Тип: **domains**.

Правил: **9**. Точные домены: 4; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_origin_b559895a.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_origin_b559895a.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-origin.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: cloudsync-prod.s3.amazonaws.com
domain: origin-a.akamaihd.net
domain: rtm.tnt-ea.com
domain: ssl-lvlt.cdn.ea.com
domain_suffix: dawngate.com
domain_suffix: eastore.com
domain_suffix: lordofultima.com
domain_suffix: origin.com
domain_suffix: origin.tv
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
