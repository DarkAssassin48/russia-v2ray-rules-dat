# wikimedia

Актуальный набор доменных правил «wikimedia» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `wikimedia`. Тип: **domains**.

Правил: **18**. Точные домены: 0; доменные зоны: 18; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_wikimedia_d9d74a70.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_wikimedia_d9d74a70.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-wikimedia.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: mediawiki.org
domain_suffix: toolforge.org
domain_suffix: w.wiki
domain_suffix: wikibooks.org
domain_suffix: wikidata.org
domain_suffix: wikimedia.org
domain_suffix: wikimediacloud.org
domain_suffix: wikimediafoundation.org
domain_suffix: wikinews.org
domain_suffix: wikipedia.org
domain_suffix: wikiquote.org
domain_suffix: wikisource.org
domain_suffix: wikiversity.org
domain_suffix: wikivoyage.org
domain_suffix: wiktionary.org
domain_suffix: wmcloud.org
domain_suffix: wmflabs.org
domain_suffix: wmfusercontent.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
