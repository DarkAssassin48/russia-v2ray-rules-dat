# Spotify — приложение, музыка и изображения

Сайт и приложение Spotify, вход, API, обложки и известные узлы доставки аудио. Добавлены адреса CDN Spotify; общие зоны Akamai и Fastly целиком не включаются.

Код: `spotify`. Тип: **domains**.

Правил: **29**. Точные домены: 11; доменные зоны: 18; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_spotify.txt)
- [Полный JSON с исходной логикой](../details/da_spotify.json)
- [Готовый SRS](../custom/spotify.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: adeventtracker.spotify.com
domain: adstudio-assets.scdn.co
domain: audio-ak-spotify-com.akamaized.net
domain: audio4-ak-spotify-com.akamaized.net
domain: bloodhound.spotify.com
domain: cdn-spotify-experiments.conductrics.com
domain: heads-ak-spotify-com.akamaized.net
domain: heads4-ak-spotify-com.akamaized.net
domain: spotify.com.edgesuite.net
domain: spotify.map.fastly.net
domain: spotify.map.fastlylb.net
domain_suffix: byspotify.com
domain_suffix: lifeatspotify.com
domain_suffix: pscdn.co
domain_suffix: scdn.co
domain_suffix: spoti.fi
domain_suffix: spotify-everywhere.com
domain_suffix: spotify.com
domain_suffix: spotify.com.edgesuite.net
domain_suffix: spotify.design
domain_suffix: spotify.link
domain_suffix: spotifycdn.com
domain_suffix: spotifycdn.net
domain_suffix: spotifycharts.com
domain_suffix: spotifycodes.com
domain_suffix: spotifyforbrands.com
domain_suffix: spotifyforvendors.com
domain_suffix: spotifyjobs.com
domain_suffix: tospotify.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
