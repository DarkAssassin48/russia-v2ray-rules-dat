# verisign-pki

Актуальный набор доменных правил «verisign-pki» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `verisign-pki`. Тип: **domains**.

Правил: **50**. Точные домены: 0; доменные зоны: 50; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_verisign_pki_7e0cce91.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_verisign_pki_7e0cce91.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-verisign-pki.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: adobe-crl.verisign.com
domain_suffix: certipath-aia.verisign.com
domain_suffix: certipath-crl.verisign.com
domain_suffix: crl.verisign.com
domain_suffix: csc3-2004-aia.verisign.com
domain_suffix: csc3-2004-crl.verisign.com
domain_suffix: csc3-2009-2-aia.verisign.com
domain_suffix: csc3-2009-2-crl.verisign.com
domain_suffix: csc3-2009-aia.verisign.com
domain_suffix: csc3-2009-crl.verisign.com
domain_suffix: csc3-2010-aia.verisign.com
domain_suffix: csc3-2010-crl.verisign.com
domain_suffix: eca-client-crl.verisign.com
domain_suffix: eca-client-ocsp.verisign.com
domain_suffix: evintl-aia.verisign.com
domain_suffix: evintl-crl.verisign.com
domain_suffix: evintl-ocsp.verisign.com
domain_suffix: evintl-t1-crl.verisign.com
domain_suffix: evsecure-aia.verisign.com
domain_suffix: evsecure-crl.verisign.com
domain_suffix: evsecure-ocsp.verisign.com
domain_suffix: evsecure-t1-aia.verisign.com
domain_suffix: evsecure-t1-crl.verisign.com
domain_suffix: ocsp.verisign.com
domain_suffix: onsitecrl.verisign.com
domain_suffix: orgc3-crl.verisign.com
domain_suffix: pki-ocsp.verisign.com
domain_suffix: ssp-aia.verisign.com
domain_suffix: ssp-crl.verisign.com
domain_suffix: ssp-ocsp.verisign.com
domain_suffix: svr-wimax-ocsp.verisign.com
domain_suffix: svrintl-aia.verisign.com
domain_suffix: svrintl-crl.verisign.com
domain_suffix: svrintl-g3-aia.verisign.com
domain_suffix: svrintl-g3-crl.verisign.com
domain_suffix: svrintl-t1-aia.verisign.com
domain_suffix: svrintl-t1-crl.verisign.com
domain_suffix: svrsecure-aia.verisign.com
domain_suffix: svrsecure-crl.verisign.com
domain_suffix: svrsecure-g2-aia.verisign.com
domain_suffix: svrsecure-g2-crl.verisign.com
domain_suffix: svrsecure-g3-aia.verisign.com
domain_suffix: svrsecure-g3-crl.verisign.com
domain_suffix: svrsecure-oracle-aia.verisign.com
domain_suffix: svrsecure-oracle-crl.verisign.com
domain_suffix: svrsecure-oracle-ocsp.verisign.com
domain_suffix: svrsecure-t1-aia.verisign.com
domain_suffix: svrsecure-t1-crl.verisign.com
domain_suffix: svrtrial-g2-aia.verisign.com
domain_suffix: svrtrial-g2-crl.verisign.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
