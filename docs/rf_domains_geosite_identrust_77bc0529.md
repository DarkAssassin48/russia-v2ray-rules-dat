# identrust

Актуальный набор доменных правил «identrust» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `identrust`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_identrust_77bc0529.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_identrust_77bc0529.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-identrust.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: identrust.co.uk
domain_suffix: identrust.com
domain_suffix: identrust.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
