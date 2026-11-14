# Windows — прочие домены

Актуальный набор доменных правил «Windows — прочие домены» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT.

Код: `win-extra`. Тип: **domains**.

Правил: **355**. Точные домены: 0; доменные зоны: 355; фрагменты: 0; regex: 0; IP-сети: 0.

## Полный состав

- [Все адреса в текстовом виде](../details/rf_domains_geosite_win_extra_3a780bee.txt)
- [Полный JSON с исходной логикой](../details/rf_domains_geosite_win_extra_3a780bee.json)
- [Готовый SRS](../sing-box/rule-set-geosite/geosite-win-extra.srs)

`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.

## Первые адреса

```text
domain_suffix: a-0001.dc-msedge.net
domain_suffix: a-0003.dc-msedge.net
domain_suffix: a-msedge.net
domain_suffix: a-ring.msedge.net
domain_suffix: a.config.skype.com
domain_suffix: activation-v2.sls.microsoft.com
domain_suffix: activation.sls.microsoft.com
domain_suffix: activity.windows.com
domain_suffix: answers.microsoft.com
domain_suffix: api.bing.com
domain_suffix: api.cdp.microsoft.com
domain_suffix: api.msn.com
domain_suffix: api.onedrive.com
domain_suffix: appex-rf.msn.com
domain_suffix: apps.skype.com
domain_suffix: arc.msn.com
domain_suffix: arc.msn.com.nsatc.net
domain_suffix: ars.smartscreen.microsoft.com
domain_suffix: assets.msn.com
domain_suffix: assuritystorage.blob.core.windows.net
domain_suffix: auth.gfx.ms
domain_suffix: autologon.microsoftazuread-sso.com
domain_suffix: automatedirstrprdeus.blob.core.windows.net
domain_suffix: az361816.vo.msecnd.net
domain_suffix: az512334.vo.msecnd.net
domain_suffix: az725175.vo.msecnd.net
domain_suffix: azpglspamprwduateus2.blob.core.windows.net
domain_suffix: azsc-euw.config.skype.com
domain_suffix: b-ring.msedge.net
domain_suffix: b.config.skype.com
domain_suffix: bingforbusiness.com
domain_suffix: bl3301-a.1drv.com
domain_suffix: bl3301-c.1drv.com
domain_suffix: bl3301-g.1drv.com
domain_suffix: blob.weather.microsoft.com
domain_suffix: blobs.officehome.msocdn.com
domain_suffix: bn2b-cor001.api.p001.1drv.com
domain_suffix: bn2b-cor002.api.p001.1drv.com
domain_suffix: bn2b-cor003.api.p001.1drv.com
domain_suffix: bn2b-cor004.api.p001.1drv.com
domain_suffix: bn3p-cor001.api.p001.1drv.com
domain_suffix: browser.events.data.msn.com
domain_suffix: by3301-a.1drv.com
domain_suffix: by3301-c.1drv.com
domain_suffix: by3301-e.1drv.com
domain_suffix: c-0001.dc-msedge.net
domain_suffix: c.bing.com
domain_suffix: c1.microsoft.com
domain_suffix: candycrushsoda.king.com
domain_suffix: cbecloud.com
```

Полный перечень без сокращений доступен по ссылкам выше.

По умолчанию выключен. Добавление каталога само по себе не включает маршрут.
