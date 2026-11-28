# winline

Актуальный набор доменных правил «winline» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `winline`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_winline_fbc3badc.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_winline_fbc3badc.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-winline.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: win-line.ru
domain_suffix: winline.ru
domain_suffix: winlinebet.ru
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
