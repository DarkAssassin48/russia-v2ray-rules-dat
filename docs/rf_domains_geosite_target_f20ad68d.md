# target

Актуальный набор доменных правил «target» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `target`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_target_f20ad68d.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_target_f20ad68d.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-target.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: .target
domain_suffix: target.com
domain_suffix: targetimg1.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
