# bitwarden

Актуальный набор доменных правил «bitwarden» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `bitwarden`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_bitwarden_1ac9574e.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_bitwarden_1ac9574e.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-bitwarden.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: bitwarden.com
domain_suffix: bitwarden.eu
domain_suffix: bitwarden.net
domain_suffix: btwrdn.co
domain_suffix: btwrdn.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
