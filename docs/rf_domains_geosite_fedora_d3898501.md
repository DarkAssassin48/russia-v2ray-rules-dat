# fedora

Актуальный набор доменных правил «fedora» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `fedora`. Тип: **domains**.

Правил: **6**. Точные домены: 0; доменные зоны: 6; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_fedora_d3898501.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_fedora_d3898501.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-fedora.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: fedoraforum.org
domain_suffix: fedorainfracloud.org
domain_suffix: fedoramagazine.org
domain_suffix: fedorapeople.org
domain_suffix: fedoraproject.org
domain_suffix: getfedora.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
