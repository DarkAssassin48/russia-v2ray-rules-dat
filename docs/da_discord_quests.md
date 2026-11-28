# Discord — чаты, медиа и награды заданий

Домены Discord и hCaptcha в одном наборе: чаты, вложения, загрузка проверки перед получением наград. hCaptcha должна идти через то же подключение, что и Discord. Голосовые UDP-серверы по IP этим доменным набором не описываются.

Код: `discord-quests`. Тип: **domains**.

Правил: **31**. Точные домены: 2; доменные зоны: 29; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_discord_quests.txt)
- [Полный JSON с исходной логикой](../details/da_discord_quests.json)
- [Готовый SRS](../custom/discord-quests.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: discord-attachments-uploads-prd.storage.googleapis.com
domain: hammerandchisel.ssl.zendesk.com
domain_suffix: airhorn.solutions
domain_suffix: airhornbot.com
domain_suffix: bigbeans.solutions
domain_suffix: botstop.com
domain_suffix: dis.gd
domain_suffix: discord-activities.com
domain_suffix: discord.co
domain_suffix: discord.com
domain_suffix: discord.design
domain_suffix: discord.dev
domain_suffix: discord.gg
domain_suffix: discord.gift
domain_suffix: discord.gifts
domain_suffix: discord.media
domain_suffix: discord.new
domain_suffix: discord.store
domain_suffix: discord.tools
domain_suffix: discordactivities.com
domain_suffix: discordapp.com
domain_suffix: discordapp.io
domain_suffix: discordapp.net
domain_suffix: discordcdn.com
domain_suffix: discordmerch.com
domain_suffix: discordpartygames.com
domain_suffix: discordsays.com
domain_suffix: discordstatus.com
domain_suffix: hcaptcha.com
domain_suffix: hcaptchastatus.com
domain_suffix: watchanimeattheoffice.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
