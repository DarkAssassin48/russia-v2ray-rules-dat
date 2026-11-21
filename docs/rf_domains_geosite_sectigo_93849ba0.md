# sectigo

Актуальный набор доменных правил «sectigo» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `sectigo`. Тип: **domains**.

Правил: **21**. Точные домены: 0; доменные зоны: 21; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_sectigo_93849ba0.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_sectigo_93849ba0.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-sectigo.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: aoc.cat
domain_suffix: catcert.cat
domain_suffix: comodoca.com
domain_suffix: comodoca2.com
domain_suffix: comodoca3.com
domain_suffix: comodoca4.com
domain_suffix: enterprisessl.com
domain_suffix: hackerguardian.com
domain_suffix: incommon-rsa.org
domain_suffix: instantssl.com
domain_suffix: netsolssl.com
domain_suffix: oemssl.cn
domain_suffix: oemssl.cn.cdn.cloudflare.net
domain_suffix: optimumssl.com
domain_suffix: positivessl.com
domain_suffix: sectigo.com
domain_suffix: sectigochina.com
domain_suffix: sectigochina.com.cdn.cloudflare.net
domain_suffix: trust-provider.cn
domain_suffix: trust-provider.com
domain_suffix: usertrust.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
