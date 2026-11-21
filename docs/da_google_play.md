# Google Play — домены магазина

Домены Google Play из исходной категории. Общие сервисы аккаунтов Google доступны отдельными наборами.

Код: `google-play`. Тип: **domains**.

Правил: **23**. Точные домены: 14; доменные зоны: 7; фрагменты: 0; regex: 2; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_google_play.txt)
- [Полный JSON с исходной логикой](../details/da_google_play.json)
- [Готовый SRS](../custom/google-play.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: .
domain: a
domain: c
domain: d
domain: e
domain: g
domain: i
domain: l
domain: m
domain: o
domain: p
domain: r
domain: t
domain: y
domain_regex: ^r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com$
domain_regex: ^r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.xn--ngstr-lra8j\.com$
domain_suffix: googleplay.com
domain_suffix: play-fe.googleapis.com
domain_suffix: play-games.googleusercontent.com
domain_suffix: play-lh.googleusercontent.com
domain_suffix: play.google.com
domain_suffix: play.googleapis.com
domain_suffix: xn--ngstr-lra8j.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
