# hashicorp

Актуальный набор доменных правил «hashicorp» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `hashicorp`. Тип: **domains**.

Правил: **8**. Точные домены: 0; доменные зоны: 8; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_hashicorp_12aa5945.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_hashicorp_12aa5945.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-hashicorp.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: consul.io
domain_suffix: hashicorp.com
domain_suffix: nomadproject.io
domain_suffix: packer.io
domain_suffix: terraform.io
domain_suffix: vagrantcloud.com
domain_suffix: vagrantup.com
domain_suffix: vaultproject.io
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
