# google-trust-services

Актуальный набор доменных правил «google-trust-services» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `google-trust-services`. Тип: **domains**.

Правил: **12**. Точные домены: 11; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_google_trust_services_78adcd9f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_google_trust_services_78adcd9f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-google-trust-services.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: c.pki.goog
domain: clients1.google.com
domain: crl.pki.goog
domain: crls.pki.goog
domain: i.pki.goog
domain: o.pki.goog
domain: ocsp.pki.goog
domain: pki-goog.l.google.com
domain: pki.google.com
domain: preprod-publicca.googleapis.com
domain: publicca.googleapis.com
domain_suffix: pki.goog
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
