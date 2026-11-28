# eset

Актуальный набор доменных правил «eset» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `eset`. Тип: **domains**.

Правил: **9**. Точные домены: 2; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_eset_69c22871.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_eset_69c22871.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-eset.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: epc-de-agent-proxy.germanywestcentral.cloudapp.azure.com
domain: eset-prod-ca48648d0ce7cadf.elb.eu-central-1.amazonaws.com
domain_suffix: cn.eset.com
domain_suffix: e5.sk
domain_suffix: eset.com
domain_suffix: eset.eu
domain_suffix: eset.sk
domain_suffix: eset.systems
domain_suffix: esetsoftware.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
