# zdns

Актуальный набор доменных правил «zdns» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `zdns`. Тип: **domains**.

Правил: **12**. Точные домены: 0; доменные зоны: 12; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_zdns_e19c7051.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_zdns_e19c7051.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-zdns.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: zcmbc.com.cn
domain_suffix: zdns.cn
domain_suffix: zdns.net.cn
domain_suffix: zdns.org.cn
domain_suffix: zdnscloud.biz
domain_suffix: zdnscloud.cn
domain_suffix: zdnscloud.com
domain_suffix: zdnscloud.com.cn
domain_suffix: zdnscloud.info
domain_suffix: zdnscloud.net
domain_suffix: zdnscloud.net.cn
domain_suffix: zdnscloud.org.cn
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
