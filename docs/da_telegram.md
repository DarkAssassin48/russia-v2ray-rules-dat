# Telegram — сайты и доменные сервисы

Домены Telegram, веб-клиента и связанных сервисов. Для соединений клиентов по IP доступны отдельные IP-наборы Telegram в каталоге.

Код: `telegram`. Тип: **domains**.

Правил: **21**. Точные домены: 0; доменные зоны: 21; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_telegram.txt)
- [Полный JSON с исходной логикой](../details/da_telegram.json)
- [Готовый SRS](../custom/telegram.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: cdn-telegram.org
domain_suffix: comments.app
domain_suffix: contest.com
domain_suffix: fragment.com
domain_suffix: graph.org
domain_suffix: quiz.directory
domain_suffix: t.me
domain_suffix: tdesktop.com
domain_suffix: telega.one
domain_suffix: telegra.ph
domain_suffix: telegram-cdn.org
domain_suffix: telegram.dog
domain_suffix: telegram.me
domain_suffix: telegram.org
domain_suffix: telegram.space
domain_suffix: telesco.pe
domain_suffix: tg.dev
domain_suffix: ton.org
domain_suffix: toncenter.com
domain_suffix: tx.me
domain_suffix: usercontent.dev
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
