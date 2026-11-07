# Blizzard / Battle.net — доменные сервисы

Сайты, аккаунты и известные доменные сервисы Blizzard / Battle.net. Включайте только при необходимости: доменная маршрутизация не описывает весь игровой UDP-трафик Overwatch.

Код: `blizzard`. Тип: **domains**.

Правил: **25**. Точные домены: 9; доменные зоны: 16; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_blizzard.txt)
- [Полный JSON с исходной логикой](../details/da_blizzard.json)
- [Готовый SRS](../custom/blizzard.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: blizzard.nefficient.co.kr
domain: blizzcon-a.akamaihd.net
domain: blzddist1-a.akamaihd.net
domain: blzddistkr1-a.akamaihd.net
domain: blzmedia-a.akamaihd.net
domain: blznav.akamaized.net
domain: bnetcmsus-a.akamaihd.net
domain: bnetproduct-a.akamaihd.net
domain: bnetshopus.akamaized.net
domain_suffix: battle.net
domain_suffix: blizzard.com
domain_suffix: blizzardgearstore.com
domain_suffix: blz-contentstack.com
domain_suffix: diablo.com
domain_suffix: diablo3.com
domain_suffix: diablo4.com
domain_suffix: diabloimmortal.com
domain_suffix: firesidegatherings.com
domain_suffix: heroesofthestorm.com
domain_suffix: playhearthstone.com
domain_suffix: playoverwatch.com
domain_suffix: playwarcraft3.com
domain_suffix: starcraft.com
domain_suffix: starcraft2.com
domain_suffix: worldofwarcraft.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
