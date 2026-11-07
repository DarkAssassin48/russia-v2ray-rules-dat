# ubiquiti

Актуальный набор доменных правил «ubiquiti» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `ubiquiti`. Тип: **domains**.

Правил: **13**. Точные домены: 0; доменные зоны: 13; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_ubiquiti_06cbd2f9.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_ubiquiti_06cbd2f9.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-ubiquiti.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: amplifi.com
domain_suffix: amplifi.com.cn
domain_suffix: frontrow.com
domain_suffix: frontrow.com.cn
domain_suffix: ubncloud.com
domain_suffix: ubnt.com
domain_suffix: ubnt.com.cn
domain_suffix: ui.com
domain_suffix: ui.com.cn
domain_suffix: uisp.com
domain_suffix: uum.com.cn
domain_suffix: uwn.com
domain_suffix: wifiman.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
