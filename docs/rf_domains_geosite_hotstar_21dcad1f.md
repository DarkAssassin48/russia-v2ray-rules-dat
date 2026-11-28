# hotstar

Актуальный набор доменных правил «hotstar» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hotstar`. Тип: **domains**.

Правил: **6**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hotstar_21dcad1f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hotstar_21dcad1f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hotstar.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: hotstar-cdn.net
domain_suffix: hotstar-labs.com
domain_suffix: hotstar.com
domain_suffix: hotstarext.com
domain_suffix: hsprepack.akamaized.net
domain_regex: ^hses[1-7]?\.akamaized\.net$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
