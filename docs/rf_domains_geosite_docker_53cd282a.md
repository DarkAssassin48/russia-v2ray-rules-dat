# docker

Актуальный набор доменных правил «docker» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `docker`. Тип: **domains**.

Правил: **6**. Точные домены: 2; доменные зоны: 4; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_docker_53cd282a.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_docker_53cd282a.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-docker.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com
domain: docker-pinata-support.s3.amazonaws.com
domain_suffix: compose-spec.io
domain_suffix: docker.com
domain_suffix: docker.io
domain_suffix: dockerstatic.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
