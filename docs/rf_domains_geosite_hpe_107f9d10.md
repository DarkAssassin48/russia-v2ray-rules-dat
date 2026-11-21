# hpe

Актуальный набор доменных правил «hpe» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hpe`. Тип: **domains**.

Правил: **16**. Точные домены: 1; доменные зоны: 15; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hpe_107f9d10.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hpe_107f9d10.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hpe.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: hpefonts.s3.amazonaws.com
domain_suffix: greenlakeaas.com
domain_suffix: greenlakehybridcloud.com
domain_suffix: hewlett-packard.asia
domain_suffix: hewlett-packard.ch
domain_suffix: hewlett-packard.co
domain_suffix: hewlett-packard.co.il
domain_suffix: hewlett-packard.co.uk
domain_suffix: hewlett-packard.com.cn
domain_suffix: hewlett-packard.com.mx
domain_suffix: hewlett-packard.com.sg
domain_suffix: hewlett-packard.jp
domain_suffix: hewlett-packard.mobi
domain_suffix: hewlettpackard.enterprises
domain_suffix: hpe.com
domain_suffix: hpecyber.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
