# pingcap

Актуальный набор доменных правил «pingcap» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `pingcap`. Тип: **domains**.

Правил: **7**. Точные домены: 0; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_pingcap_20062fe1.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_pingcap_20062fe1.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-pingcap.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: asktug.com
domain_suffix: pingcap.cn
domain_suffix: pingcap.com
domain_suffix: tidb.ai
domain_suffix: tidb.net
domain_suffix: tidbcloud.com
domain_suffix: tikv.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
