# Netflix — доменные сервисы

Домены Netflix и доставки содержимого из исходной категории. Доступность контента дополнительно зависит от правил сервиса и выбранного VPN-сервера.

Код: `netflix`. Тип: **domains**.

Правил: **28**. Точные домены: 0; доменные зоны: 24; фрагменты: 0; regex: 4; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_netflix.txt)
- [Полный JSON с исходной логикой](../details/da_netflix.json)
- [Готовый SRS](../custom/netflix.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_regex: (^|\.)apiproxy-device-prod-nlb-.+\.amazonaws\.com$
domain_regex: (^|\.)apiproxy-website-nlb-prod-.+\.amazonaws\.com$
domain_regex: (^|\.)dualstack\.apiproxy-.+\.amazonaws\.com$
domain_regex: (^|\.)dualstack\.ichnaea-web-.+\.amazonaws\.com$
domain_suffix: fast.com
domain_suffix: netflix.ca
domain_suffix: netflix.com
domain_suffix: netflix.com.edgesuite.net
domain_suffix: netflix.net
domain_suffix: netflixdnstest0.com
domain_suffix: netflixdnstest1.com
domain_suffix: netflixdnstest10.com
domain_suffix: netflixdnstest2.com
domain_suffix: netflixdnstest3.com
domain_suffix: netflixdnstest4.com
domain_suffix: netflixdnstest5.com
domain_suffix: netflixdnstest6.com
domain_suffix: netflixdnstest7.com
domain_suffix: netflixdnstest8.com
domain_suffix: netflixdnstest9.com
domain_suffix: netflixinvestor.com
domain_suffix: netflixtechblog.com
domain_suffix: nflxext.com
domain_suffix: nflximg.com
domain_suffix: nflximg.net
domain_suffix: nflxsearch.net
domain_suffix: nflxso.net
domain_suffix: nflxvideo.net
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
