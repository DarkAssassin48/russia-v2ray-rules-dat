# synology

Актуальный набор доменных правил «synology» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `synology`. Тип: **domains**.

Правил: **20**. Точные домены: 0; доменные зоны: 20; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_synology_fdb91be7.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_synology_fdb91be7.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-synology.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: diskstation.me
domain_suffix: dscloud.biz
domain_suffix: dscloud.me
domain_suffix: dscloud.mobi
domain_suffix: dsmynas.com
domain_suffix: dsmynas.net
domain_suffix: dsmynas.org
domain_suffix: familyds.com
domain_suffix: familyds.net
domain_suffix: familyds.org
domain_suffix: gofile.me
domain_suffix: i234.me
domain_suffix: myds.me
domain_suffix: quickconnect.cn
domain_suffix: quickconnect.to
domain_suffix: synology.cn
domain_suffix: synology.com
domain_suffix: synology.me
domain_suffix: synologydownload.com
domain_suffix: synologyupdate.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
