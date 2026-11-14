# canonical

Актуальный набор доменных правил «canonical» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `canonical`. Тип: **domains**.

Правил: **12**. Точные домены: 0; доменные зоны: 12; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_canonical_a31cd002.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_canonical_a31cd002.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-canonical.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: canonical.com
domain_suffix: launchpad.net
domain_suffix: launchpadcontent.net
domain_suffix: launchpadlibrarian.com
domain_suffix: launchpadlibrarian.net
domain_suffix: launchpadlibrarian.org
domain_suffix: snapcraft.io
domain_suffix: snapstore.io
domain_suffix: ubuntu-touch.io
domain_suffix: ubuntu.com
domain_suffix: ubuntu.net
domain_suffix: ubuntuforums.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
