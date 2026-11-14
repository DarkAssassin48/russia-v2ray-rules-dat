# certum

Актуальный набор доменных правил «certum» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `certum`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_certum_9648d39b.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_certum_9648d39b.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-certum.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: certum.pl
domain_suffix: ocsp-certum.com
domain_suffix: ocsp-responder.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
