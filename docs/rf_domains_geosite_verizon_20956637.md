# verizon

Актуальный набор доменных правил «verizon» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `verizon`. Тип: **domains**.

Правил: **15**. Точные домены: 0; доменные зоны: 15; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_verizon_20956637.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_verizon_20956637.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-verizon.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: oath.cloud
domain_suffix: oath.com
domain_suffix: ouroath.com
domain_suffix: static-verizon.com
domain_suffix: uplynk.com
domain_suffix: verizon.com
domain_suffix: verizon.net
domain_suffix: verizonbusinessfios.com
domain_suffix: verizondigitalmedia.com
domain_suffix: verizonenterprise.com
domain_suffix: verizonfios.com
domain_suffix: verizonmedia.com
domain_suffix: verizonwireless.com
domain_suffix: vzw.com
domain_suffix: xo.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
