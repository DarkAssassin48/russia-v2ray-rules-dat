# Google Play

Актуальный набор доменных правил «Google Play» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `google-play`. Тип: **domains**.

Правил: **10**. Точные домены: 1; доменные зоны: 7; фрагменты: 0; regex: 2; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_google_play_ab54ca48.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_google_play_ab54ca48.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-google-play.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: redirector.c.play.google.com
domain_suffix: googleplay.com
domain_suffix: play-fe.googleapis.com
domain_suffix: play-games.googleusercontent.com
domain_suffix: play-lh.googleusercontent.com
domain_suffix: play.google.com
domain_suffix: play.googleapis.com
domain_suffix: xn--ngstr-lra8j.com
domain_regex: ^r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.xn--ngstr-lra8j\.com$
domain_regex: ^r+[0-9]+(---|\.)sn-(2x3|ni5|j5o)\w{5}\.googlevideo\.com$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
