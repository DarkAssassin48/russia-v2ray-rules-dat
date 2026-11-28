# microsoft-pki

Актуальный набор доменных правил «microsoft-pki» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `microsoft-pki`. Тип: **domains**.

Правил: **6**. Точные домены: 5; доменные зоны: 1; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_microsoft_pki_16877b0f.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_microsoft_pki_16877b0f.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-microsoft-pki.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: crl.microsoft.com
domain: mscrl.microsoft.com
domain: ocsp.microsoft.com
domain: oneocsp.microsoft.com
domain: www.microsoft.com
domain_suffix: msocsp.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
