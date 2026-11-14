# lastfm

Актуальный набор доменных правил «lastfm» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `lastfm`. Тип: **domains**.

Правил: **4**. Точные домены: 3; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_lastfm_9cd1c6fb.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_lastfm_9cd1c6fb.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-lastfm.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: lastfm-img.freetls.fastly.net
domain: lastfm.freetls.fastly.net
domain: ws.audioscrobbler.com
domain_suffix: last.fm
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
