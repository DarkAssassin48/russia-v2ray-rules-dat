# peppy

Актуальный набор доменных правил «peppy» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `peppy`. Тип: **domains**.

Правил: **10**. Точные домены: 9; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_peppy_343f02e5.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_peppy_343f02e5.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-peppy.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: a.ppy.sh
domain: assets.ppy.sh
domain: c.ppy.sh
domain: lazer.ppy.sh
domain: m1.ppy.sh
domain: notify.ppy.sh
domain: osu.ppy.sh
domain: sentry.ppy.sh
domain: spectator.ppy.sh
domain_suffix: ppy.sh
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
