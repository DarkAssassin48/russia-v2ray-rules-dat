# cern

Актуальный набор доменных правил «cern» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cern`. Тип: **domains**.

Правил: **7**. Точные домены: 0; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cern_4592d194.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cern_4592d194.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cern.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: .cern
domain_suffix: ams02.space
domain_suffix: cern.ch
domain_suffix: cixp.net
domain_suffix: dotcernpilot.info
domain_suffix: ippog.org
domain_suffix: linearcollider.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
