# vimeo

Актуальный набор доменных правил «vimeo» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `vimeo`. Тип: **domains**.

Правил: **17**. Точные домены: 0; доменные зоны: 16; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_vimeo_5181f07b.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_vimeo_5181f07b.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-vimeo.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: livestream.com
domain_suffix: vhx.tv
domain_suffix: vhxqa1.com
domain_suffix: vhxqa2.com
domain_suffix: vhxqa3.com
domain_suffix: vhxqa4.com
domain_suffix: vhxqa6.com
domain_suffix: vimeo-staging.com
domain_suffix: vimeo-staging2.com
domain_suffix: vimeo.com
domain_suffix: vimeo.fr
domain_suffix: vimeobusiness.com
domain_suffix: vimeocdn.com
domain_suffix: vimeogoods.com
domain_suffix: vimeoondemand.com
domain_suffix: vimeostatus.com
domain_regex: ^[0-9]+vod-adaptive\.akamaized\.net$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
