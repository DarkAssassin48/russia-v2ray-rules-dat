# dnspod

Актуальный набор доменных правил «dnspod» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `dnspod`. Тип: **domains**.

Правил: **14**. Точные домены: 0; доменные зоны: 14; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_dnspod_9a3f2252.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_dnspod_9a3f2252.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-dnspod.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: dns.pub
domain_suffix: dnsapi.cn
domain_suffix: dnspod.cn
domain_suffix: dnspod.com
domain_suffix: dnspod.com.cn
domain_suffix: dnspod.mobi
domain_suffix: dnspod.net
domain_suffix: dnspod.org
domain_suffix: dnsv2.com
domain_suffix: dnsv3.com
domain_suffix: dnsv4.com
domain_suffix: dnsv5.com
domain_suffix: doh.pub
domain_suffix: dot.pub
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
