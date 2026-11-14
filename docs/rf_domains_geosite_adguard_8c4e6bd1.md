# adguard

Актуальный набор доменных правил «adguard» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `adguard`. Тип: **domains**.

Правил: **19**. Точные домены: 0; доменные зоны: 19; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_adguard_8c4e6bd1.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_adguard_8c4e6bd1.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-adguard.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: adguard-dns.com
domain_suffix: adguard-dns.io
domain_suffix: adguard-mail.com
domain_suffix: adguard-vpn.com
domain_suffix: adguard-vpn.online
domain_suffix: adguard.app
domain_suffix: adguard.com
domain_suffix: adguard.info
domain_suffix: adguard.io
domain_suffix: adguard.org
domain_suffix: adguardaccount.com
domain_suffix: adguardaccount.net
domain_suffix: adguardcdn.com
domain_suffix: adguardvpn.com
domain_suffix: adtidy.net
domain_suffix: adtidy.org
domain_suffix: agrd.eu
domain_suffix: agrd.io
domain_suffix: mask.me
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
