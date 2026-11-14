# mdn

Актуальный набор доменных правил «mdn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `mdn`. Тип: **domains**.

Правил: **9**. Точные домены: 1; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_mdn_d5368a10.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_mdn_d5368a10.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-mdn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: mdn.mozillademos.org
domain_suffix: developer.allizom.org
domain_suffix: developer.mozilla.org
domain_suffix: mdn.allizom.net
domain_suffix: mdn.dev
domain_suffix: mdn.mozilla.net
domain_suffix: mdn.mozit.cloud
domain_suffix: mdnplay.dev
domain_suffix: mdnyalp.dev
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
