# hCaptcha

Актуальный набор доменных правил «hCaptcha» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hcaptcha`. Тип: **domains**.

Правил: **3**. Точные домены: 0; доменные зоны: 3; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hcaptcha_004e3665.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hcaptcha_004e3665.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hcaptcha.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: botstop.com
domain_suffix: hcaptcha.com
domain_suffix: hcaptchastatus.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
