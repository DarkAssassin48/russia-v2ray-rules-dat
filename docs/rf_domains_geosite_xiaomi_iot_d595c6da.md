# xiaomi-iot

Актуальный набор доменных правил «xiaomi-iot» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `xiaomi-iot`. Тип: **domains**.

Правил: **4**. Точные домены: 0; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_xiaomi_iot_d595c6da.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_xiaomi_iot_d595c6da.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-xiaomi-iot.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: account.xiaomi.com
domain_suffix: cn-ha.mqtt.io.mi.com
domain_suffix: ha.api.io.mi.com
domain_suffix: miot-spec.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
