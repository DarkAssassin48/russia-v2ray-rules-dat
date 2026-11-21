# aws-cn

Актуальный набор доменных правил «aws-cn» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `aws-cn`. Тип: **domains**.

Правил: **28**. Точные домены: 0; доменные зоны: 26; фрагменты: 0; regex: 2; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_aws_cn_2e45c3b6.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_aws_cn_2e45c3b6.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-aws-cn.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: a2z.org.cn
domain_suffix: amazonaws.cn
domain_suffix: amazonaws.com.cn
domain_suffix: amazonwebservices.cn
domain_suffix: amazonwebservices.com.cn
domain_suffix: amazonworkdocs.cn
domain_suffix: amazonworkdocs.com.cn
domain_suffix: amzndns-cn.biz
domain_suffix: amzndns-cn.cn
domain_suffix: amzndns-cn.com
domain_suffix: amzndns-cn.net
domain_suffix: asfiovnxocqpcry.com.cn
domain_suffix: aws-border.cn
domain_suffix: aws-icp-domain-manager.cn
domain_suffix: awsapps.cn
domain_suffix: awsapps.com.cn
domain_suffix: awsstatic.cn
domain_suffix: cloudfront-cn.net
domain_suffix: cloudfront-test.cn
domain_suffix: cloudfront.cn
domain_suffix: nwcdcloud.cn
domain_suffix: nwcdcloud.com.cn
domain_suffix: nwcddns.cn
domain_suffix: nwcdinfosec.cn
domain_suffix: route53.cn
domain_suffix: sagemaker.com.cn
domain_regex: .+\.awsdns-cn-[0-9][0-9]\.(biz|com|net|top)$
domain_regex: .+\.awsdns-cn-[0-9][a-e0-9]\.cn$
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
