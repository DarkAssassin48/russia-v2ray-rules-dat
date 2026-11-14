# kinopoisk

Актуальный набор доменных правил «kinopoisk» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `kinopoisk`. Тип: **domains**.

Правил: **5**. Точные домены: 2; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_kinopoisk_79128c01.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_kinopoisk_79128c01.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-kinopoisk.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: kp-config-smart-tv.akamaized.net
domain: kp-configs-smart-tv.s3.eu-central-1.amazonaws.com
domain_suffix: kinopoisk-ru.clstorage.net
domain_suffix: kinopoisk.ru
domain_suffix: kp.yandex.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
