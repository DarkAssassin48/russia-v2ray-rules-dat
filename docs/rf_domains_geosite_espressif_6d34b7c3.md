# espressif

Актуальный набор доменных правил «espressif» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `espressif`. Тип: **domains**.

Правил: **7**. Точные домены: 0; доменные зоны: 7; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_espressif_6d34b7c3.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_espressif_6d34b7c3.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-espressif.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: esp32.com
domain_suffix: esp8266.cn
domain_suffix: esp8266.com
domain_suffix: esp8266.com.cn
domain_suffix: espressif.cn
domain_suffix: espressif.com
domain_suffix: espressif.com.cn
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
