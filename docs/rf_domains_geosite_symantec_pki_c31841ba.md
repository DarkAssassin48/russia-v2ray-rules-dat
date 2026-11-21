# symantec-pki

Актуальный набор доменных правил «symantec-pki» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `symantec-pki`. Тип: **domains**.

Правил: **5**. Точные домены: 0; доменные зоны: 5; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_symantec_pki_c31841ba.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_symantec_pki_c31841ba.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-symantec-pki.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: pki.symantec.com
domain_suffix: symauth.com
domain_suffix: symcb.com
domain_suffix: symcd.com
domain_suffix: ws.symantec.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
