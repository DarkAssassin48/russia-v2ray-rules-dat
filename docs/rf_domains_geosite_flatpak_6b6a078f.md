# flatpak

Актуальный набор доменных правил «flatpak» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `flatpak`. Тип: **domains**.

Правил: **2**. Точные домены: 0; доменные зоны: 2; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_flatpak_6b6a078f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_flatpak_6b6a078f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-flatpak.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: flathub.org
domain_suffix: flatpak.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
