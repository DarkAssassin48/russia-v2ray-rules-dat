# vpngate

Актуальный набор доменных правил «vpngate» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `vpngate`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_vpngate_b6fdb2d8.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_vpngate_b6fdb2d8.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-vpngate.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: opengw.net
domain_suffix: vpngate.jp
domain_suffix: vpngate.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
