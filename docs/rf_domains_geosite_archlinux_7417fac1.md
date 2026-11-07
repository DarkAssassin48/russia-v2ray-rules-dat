# archlinux

Актуальный набор доменных правил «archlinux» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `archlinux`. Тип: **domains**.

Правил: **6**. Точные домены: 0; доменные зоны: 6; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_archlinux_7417fac1.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_archlinux_7417fac1.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-archlinux.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: archlinux.de
domain_suffix: archlinux.org
domain_suffix: archlinux.page
domain_suffix: archlinuxarm.org
domain_suffix: archlinuxcn.org
domain_suffix: pkgbuild.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
