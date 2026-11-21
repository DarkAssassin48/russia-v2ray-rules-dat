# category-container

Актуальный набор доменных правил «category-container» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `category-container`. Тип: **domains**.

Правил: **10**. Точные домены: 0; доменные зоны: 9; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_category_container_77b64b9d.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_category_container_77b64b9d.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-category-container.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: azurecr.io
domain_suffix: docker.io
domain_suffix: ecr.aws
domain_suffix: gcr.io
domain_suffix: ghcr.io
domain_suffix: mcr.microsoft.com
domain_suffix: quay.io
domain_suffix: registry.gitlab.com
domain_suffix: registry.k8s.io
domain_regex: .+\.dkr\.ecr\.[^\.]+\.amazonaws\.com$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
