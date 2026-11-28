# cybertrust

Актуальный набор доменных правил «cybertrust» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `cybertrust`. Тип: **domains**.

Правил: **2**. Точные домены: 0; доменные зоны: 2; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_cybertrust_c1208dc7.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_cybertrust_c1208dc7.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-cybertrust.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: cybertrust.co.jp
domain_suffix: cybertrust.ne.jp
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
