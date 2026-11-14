# headhunter

Актуальный набор доменных правил «headhunter» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `headhunter`. Тип: **domains**.

Правил: **8**. Точные домены: 0; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_headhunter_7a39f81b.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_headhunter_7a39f81b.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-headhunter.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: hh.by
domain_suffix: hh.kz
domain_suffix: hh.ru
domain_suffix: hhcdn.ru
domain_suffix: rabota.by
domain_suffix: setka.ru
domain_suffix: talantix.ru
domain_suffix: zarplata.ru
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
