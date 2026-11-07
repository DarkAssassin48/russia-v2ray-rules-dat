# google-registry

Актуальный набор доменных правил «google-registry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `google-registry`. Тип: **domains**.

Правил: **13**. Точные домены: 0; доменные зоны: 13; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_google_registry_e44478e6.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_google_registry_e44478e6.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-google-registry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: charlestonroadregistry.com
domain_suffix: crr.com
domain_suffix: get.app
domain_suffix: get.dev
domain_suffix: get.how
domain_suffix: get.new
domain_suffix: get.page
domain_suffix: get.rsvp
domain_suffix: hey.boo
domain_suffix: iam.soy
domain_suffix: new.day
domain_suffix: registry.google
domain_suffix: xn--p8j9a0d9c9a.xn--q9jyb4c
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
