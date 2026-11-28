# Signal — доменные сервисы

Домены Signal из исходной категории. Для звонков могут требоваться дополнительные IP-маршруты.

Код: `signal`. Тип: **domains**.

Правил: **8**. Точные домены: 0; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/da_signal.txt)
- [Полный JSON с исходной логикой](../details/da_signal.json)
- [Готовый SRS](../custom/signal.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: signal.art
domain_suffix: signal.group
domain_suffix: signal.link
domain_suffix: signal.me
domain_suffix: signal.org
domain_suffix: signal.tube
domain_suffix: signalusers.org
domain_suffix: whispersystems.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
