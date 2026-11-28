# libgen

Актуальный набор доменных правил «libgen» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `libgen`. Тип: **domains**.

Правил: **8**. Точные домены: 0; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_libgen_036854b8.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_libgen_036854b8.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-libgen.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: gen.lib.rus.ec
domain_suffix: libgen.fun
domain_suffix: libgen.is
domain_suffix: libgen.life
domain_suffix: libgen.me
domain_suffix: libgen.rs
domain_suffix: libgen.st
domain_suffix: library.lol
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
