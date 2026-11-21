# connectivity-check

Актуальный набор доменных правил «connectivity-check» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `connectivity-check`. Тип: **domains**.

Правил: **28**. Точные домены: 17; доменные зоны: 11; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_connectivity_check_ca508f15.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_connectivity_check_ca508f15.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-connectivity-check.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: conn1.oppomobile.com
domain: conn2.oppomobile.com
domain: connect.rom.miui.com
domain: connectivity-check.ubuntu.com
domain: connectivity.samsung.com.cn
domain: connectivitycheck.gstatic.com
domain: connectivitycheck.platform.hicloud.com
domain: connectivitycheck.platform.hihonorcloud.com
domain: edge-http.microsoft.com
domain: networkcheck.kde.org
domain: nmcheck.gnome.org
domain: ping.archlinux.org
domain: redirect.archlinux.org
domain: wifi.vivo.com.cn
domain: www.gstatic.com
domain: www.qualcomm.cn
domain: www.qualcomm.com
domain_suffix: captive.apple.com
domain_suffix: cp.cloudflare.com
domain_suffix: detectportal.firefox.com
domain_suffix: firefox-portal-detection.com
domain_suffix: ipv6check-http.steamserver.net
domain_suffix: ipv6check-udp.steamserver.net
domain_suffix: kuketz.de
domain_suffix: msftconnecttest.com
domain_suffix: msftncsi.com
domain_suffix: network-test.debian.org
domain_suffix: test.steampowered.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
