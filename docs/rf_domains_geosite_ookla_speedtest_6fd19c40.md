# ookla-speedtest

Актуальный набор доменных правил «ookla-speedtest» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `ookla-speedtest`. Тип: **domains**.

Правил: **21**. Точные домены: 1; доменные зоны: 19; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_ookla_speedtest_6fd19c40.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_ookla_speedtest_6fd19c40.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-ookla-speedtest.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: www.speedtest.net.cdn.cloudflare.net
domain_suffix: cdnst.net
domain_suffix: cellmaps.com
domain_suffix: ekahau.cloud
domain_suffix: ekahau.com
domain_suffix: ookla-speedtest-central.hgconair.hgc.com.hk
domain_suffix: ookla.com
domain_suffix: ooklaserver.net
domain_suffix: pingtest.net
domain_suffix: speedtest.app
domain_suffix: speedtest.cc
domain_suffix: speedtest.co
domain_suffix: speedtest.ee
domain_suffix: speedtest.in
domain_suffix: speedtest.me
domain_suffix: speedtest.net
domain_suffix: speedtest.ng
domain_suffix: speedtest.tv
domain_suffix: speedtestcustom.com
domain_suffix: webtest.net
domain_regex: ^speed\.(coe|open)\.ad\.[a-z]{2,6}\.prod\.hosts\.ooklaserver\.net$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
