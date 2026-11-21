# nixos

Актуальный набор доменных правил «nixos» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `nixos`. Тип: **domains**.

Правил: **12**. Точные домены: 1; доменные зоны: 11; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_nixos_6cb54dc2.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_nixos_6cb54dc2.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-nixos.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain: nix-community.github.io
domain_suffix: builtwithnix.org
domain_suffix: mynixos.com
domain_suffix: nix-community.org
domain_suffix: nix.dev
domain_suffix: nix.store
domain_suffix: nixcon.org
domain_suffix: nixcon2017.org
domain_suffix: nixlang.com
domain_suffix: nixos.org
domain_suffix: nixos.wiki
domain_suffix: nixpkgs.org
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
