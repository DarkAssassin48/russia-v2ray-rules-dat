# yandex@telemetry

Актуальный набор доменных правил «yandex@telemetry» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `yandex@telemetry`. Тип: **domains**.

Правил: **18**. Точные домены: 5; доменные зоны: 13; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_yandex_telemetry_d8adb611.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_yandex_telemetry_d8adb611.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-yandex@telemetry.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: analytics.mobile.yandex.net
domain: log.strm.yandex.ru
domain: mc.yandex.com
domain: mc.yandex.net
domain: mc.yango.com
domain_suffix: appmetrica.yandex.com
domain_suffix: appmetrica.yandex.net
domain_suffix: appmetrica.yandex.ru
domain_suffix: appmetrica.yango.com
domain_suffix: counter.yandex.ru
domain_suffix: mc.yandex.ru
domain_suffix: metrika.yandex.com
domain_suffix: metrika.yandex.net
domain_suffix: metrika.yandex.ru
domain_suffix: webvisor.com
domain_suffix: webvisor.org
domain_suffix: yandex-metrica.ru
domain_suffix: yandexmetrica.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
