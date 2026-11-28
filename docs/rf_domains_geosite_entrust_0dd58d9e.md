# entrust

Актуальный набор доменных правил «entrust» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `entrust`. Тип: **domains**.

Правил: **10**. Точные домены: 1; доменные зоны: 9; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_entrust_0dd58d9e.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_entrust_0dd58d9e.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-entrust.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: www.entrust.cn
domain_suffix: affirmtrust.com
domain_suffix: atos.net
domain_suffix: certificat2.com
domain_suffix: entrust.cn
domain_suffix: entrust.com
domain_suffix: entrust.net
domain_suffix: entrustdatacard.com
domain_suffix: myatos.net
domain_suffix: trendmicro.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
