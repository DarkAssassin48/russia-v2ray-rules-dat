# zscaler

Актуальный набор доменных правил «zscaler» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `zscaler`. Тип: **domains**.

Правил: **17**. Точные домены: 0; доменные зоны: 17; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_zscaler_79718956.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_zscaler_79718956.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-zscaler.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: securecloudtransformation.com
domain_suffix: securitypreview.com
domain_suffix: threatlabz.com
domain_suffix: zdxbeta.net
domain_suffix: zdxcloud.net
domain_suffix: zpagov.net
domain_suffix: zpath.com
domain_suffix: zscaler.com
domain_suffix: zscaler.jp
domain_suffix: zscaler.net
domain_suffix: zscalerbeta.net
domain_suffix: zscalergov.net
domain_suffix: zscalerone.net
domain_suffix: zscalershift.com
domain_suffix: zscalerthree.net
domain_suffix: zscalertwo.net
domain_suffix: zscloud.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
