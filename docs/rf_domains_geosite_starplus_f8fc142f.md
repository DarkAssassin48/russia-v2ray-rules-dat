# starplus

Актуальный набор доменных правил «starplus» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `starplus`. Тип: **domains**.

Правил: **6**. Точные домены: 0; доменные зоны: 6; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_starplus_f8fc142f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_starplus_f8fc142f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-starplus.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: star.api.edge.bamgrid.com
domain_suffix: star.connections.edge.bamgrid.com
domain_suffix: star.content.edge.bamgrid.com
domain_suffix: star.playback.edge.bamgrid.com
domain_suffix: starott.com
domain_suffix: starplus.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
