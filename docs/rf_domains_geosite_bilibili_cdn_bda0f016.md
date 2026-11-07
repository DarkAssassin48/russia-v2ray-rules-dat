# bilibili-cdn

Актуальный набор доменных правил «bilibili-cdn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `bilibili-cdn`. Тип: **domains**.

Правил: **14**. Точные домены: 1; доменные зоны: 13; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_bilibili_cdn_bda0f016.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_bilibili_cdn_bda0f016.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-bilibili-cdn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: upos-hz-mirrorakam.akamaized.net
domain_suffix: bilicdn1.com
domain_suffix: bilicdn2.com
domain_suffix: bilicdn3.com
domain_suffix: bilicdn4.com
domain_suffix: bilicdn5.com
domain_suffix: biliimg.com
domain_suffix: bilivideo.cn
domain_suffix: bilivideo.com
domain_suffix: bilivideo.net
domain_suffix: hdslb.com
domain_suffix: hdslb.org
domain_suffix: maoercdn.com
domain_suffix: mincdn.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
