# firefox

Актуальный набор доменных правил «firefox» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `firefox`. Тип: **domains**.

Правил: **8**. Точные домены: 2; доменные зоны: 6; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_firefox_e2ea539b.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_firefox_e2ea539b.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-firefox.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: mozilla-ohttp.fastly-edge.com
domain: mozilla.map.fastly.net
domain_suffix: extendfirefox.com
domain_suffix: firefox-portal-detection.com
domain_suffix: firefox.com
domain_suffix: firefox.hu
domain_suffix: firefoxtweetmachine.com
domain_suffix: firefoxusercontent.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
