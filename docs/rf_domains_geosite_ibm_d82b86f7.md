# ibm

Актуальный набор доменных правил «ibm» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `ibm`. Тип: **domains**.

Правил: **20**. Точные домены: 0; доменные зоны: 20; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_ibm_d82b86f7.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_ibm_d82b86f7.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-ibm.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: .ibm
domain_suffix: .weather
domain_suffix: .weatherchannel
domain_suffix: appdomain.cloud
domain_suffix: bluemix.com
domain_suffix: bluemix.net
domain_suffix: consul.io
domain_suffix: hashicorp.com
domain_suffix: ibm.com
domain_suffix: ibm.eu
domain_suffix: ibm.net
domain_suffix: ibm.us
domain_suffix: nomadproject.io
domain_suffix: packer.io
domain_suffix: s-bluemix.net
domain_suffix: s81c.com
domain_suffix: terraform.io
domain_suffix: vagrantcloud.com
domain_suffix: vagrantup.com
domain_suffix: vaultproject.io
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
