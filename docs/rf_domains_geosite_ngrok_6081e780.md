# ngrok

Актуальный набор доменных правил «ngrok» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `ngrok`. Тип: **domains**.

Правил: **11**. Точные домены: 0; доменные зоны: 11; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_ngrok_6081e780.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_ngrok_6081e780.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-ngrok.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: equinox.io
domain_suffix: ngrok-agent.com
domain_suffix: ngrok-free.app
domain_suffix: ngrok-free.dev
domain_suffix: ngrok-free.pizza
domain_suffix: ngrok.app
domain_suffix: ngrok.com
domain_suffix: ngrok.dev
domain_suffix: ngrok.io
domain_suffix: ngrok.pizza
domain_suffix: ngrok.pro
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
