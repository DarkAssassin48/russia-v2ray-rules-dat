# mihoyo-cn

Актуальный набор доменных правил «mihoyo-cn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `mihoyo-cn`. Тип: **domains**.

Правил: **17**. Точные домены: 0; доменные зоны: 16; фрагменты: 0; regex: 1; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_mihoyo_cn_dd73f636.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_mihoyo_cn_dd73f636.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-mihoyo-cn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: benghuai.com
domain_suffix: bh3.com
domain_suffix: bhsr.com
domain_suffix: juequling.com
domain_suffix: log-upload.mihoyo.com
domain_suffix: mhystatic.com
domain_suffix: mhyurl.cn
domain_suffix: mihayo.com
domain_suffix: mihayou.com
domain_suffix: mihoyo.com
domain_suffix: mihoyocg.com
domain_suffix: mihoyogift.com
domain_suffix: mihoyomall.com
domain_suffix: miyoushe.com
domain_suffix: themisweeps.com
domain_suffix: yuanshen.com
domain_regex: ^.+-mihayo\.akamaized\.net$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
