# DarkAssassin — каталог runetfreedom для Forkozz

Форк [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat): все исходные SRS-наборы, 22 готовых профиля и полный справочник доменов и IP-сетей. Каталог рассчитан на поле «Свой каталог списков» в Forkozz / Zapret Manager.

## Ссылка для вставки в Forkozz

```text
https://darkassassin48.github.io/russia-v2ray-rules-dat/lists.json
```

Основная ссылка отдаётся через GitHub Pages вместе с бинарными SRS и содержит все наборы. В ней сохранены поля, которые действительно нужны парсеру Forkozz; подробные сведения остаются в справочнике.

**Если панель сообщает о лимите 17 секунд**, используйте небольшой каталог **22 готовых профилей**:

```text
https://darkassassin48.github.io/russia-v2ray-rules-dat/lists-lite.json
```

В нём есть Discord + hCaptcha, NVIDIA App, Spotify, OpenAI и остальные профили из списка ниже. Все 2 287 исходных наборов остаются в полном каталоге и справочнике; малый вариант не включает их отдельно. Идентификаторы одинаковых профилей совпадают между вариантами, содержимое правил не урезается.

Лимит панели относится ко всей операции: скачивание **и разбор** JSON. Полный справочник из тысяч пунктов может не уложиться на маломощном устройстве даже при быстром интернете. Малый каталог предназначен для этого случая. Точное время на вашем роутере зависит также от его загрузки и сетевого маршрута.

[Резервная исходная ссылка через raw GitHub](https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/lists.json) продолжает работать. Справочник адресов и исходные DAT хранятся в ветке `release`; GitHub Pages раздаёт только каталоги и SRS, около 31 МБ.

Откройте «Forkozz → Сервисы → Каталог списков → Сменить источник», вставьте ссылку и подключите каталог. Название пункта может зависеть от версии панели. Затем включите только нужные сервисы и сохраните настройки. Все новые пункты выключены по умолчанию. Замена каталога сама по себе не включает все маршруты и не очищает ранее выбранные списки: проверьте их в панели.

## Какие сервисы и адреса входят

- **[Полный каталог с описаниями и адресами](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/release/CATALOG.md)** — все сервисы, категории и IP-наборы; для каждого доступны TXT, исходный JSON и SRS.
- [Discord — чаты, медиа и награды заданий](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/release/docs/da_discord_quests.md): категория Discord + hCaptcha, включая меняющиеся поддомены `hcaptcha.com`.
- [NVIDIA App — вход, драйверы и обновления](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/release/docs/da_nvidia_app.md): категория NVIDIA без доменов Hugging Face. Полная исходная NVIDIA также сохранена отдельно.
- [Spotify — приложение, музыка и изображения](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/release/docs/da_spotify.md): категория Spotify + известные отдельные узлы CDN Akamai/Fastly; общие зоны этих CDN целиком не добавляются.
- [OpenAI / ChatGPT / Codex](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/release/docs/da_openai.md): исходный набор + основные домены входа, ресурсов и файлов.
- Дополнительно: YouTube, Telegram, Twitch, Steam, Blizzard / Battle.net, Epic Games, Riot, GitHub, Gemini, Claude, Instagram, WhatsApp, X / Twitter, Netflix, Signal, Google Play, Zoom и отдельная hCaptcha.

Группы в каталоге: «DarkAssassin · Готовые профили», «runetfreedom · Сервисы», «runetfreedom · Категории», «runetfreedom · IP-сети». Большие наборы помечены отдельно.

`domain_suffix` включает домен и все его поддомены; `domain` — только точное имя; `domain_keyword` — фрагмент; `domain_regex` — регулярное выражение; `ip_cidr` — сеть. Логические комбинации и исключения сохраняются в JSON без упрощения. TXT содержит все адреса и типы правил; для сложных комбинаций JSON является точным описанием логики.

Доменные наборы не гарантируют покрытия голосового или игрового UDP-трафика по IP. Общие IP-сети могут охватывать несколько сервисов. Количество записей означает число условий в наборе, а не число всех возможных поддоменов. Покрытие меняется вместе с исходными данными.

## Автоматическое обновление

[GitHub Actions](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/actions/workflows/build.yml) запускает сборку каждые 6 часов: **01:17, 07:17, 13:17 и 19:17 по Москве** (UTC+3). Планировщик GitHub может задерживать запуск. Также предусмотрены ручной запуск **Run workflow** и сборка после изменения профилей или генератора в `main`.

Каждая сборка:

1. Берёт последний опубликованный `release` runetfreedom и фиксирует его commit SHA.
2. Проверяет контрольные суммы DAT, декомпилирует все исходные SRS, создаёт полный справочник и обновляет дополнительные профили.
3. Проверяет структуру каталога, уникальность идентификаторов, все ссылки на локальные файлы, состав Discord / NVIDIA и SHA-256 каждого файла.
4. Публикует проверенный снимок в ветку `release` и развёртывает полный и малый каталоги вместе с SRS на GitHub Pages. При ошибке до публикации последний исправный каталог остаётся доступен.

Постоянные ссылки `lists.json` и `lists-lite.json` не меняются. Оба варианта пересоздаются при каждой сборке; кэш CDN может задержать появление новой версии. Обновление файлов на GitHub и скачивание правил самим Forkozz — отдельные процессы: период обновления на роутере определяется настройками установленной панели. Этот репозиторий не подключается к роутеру и не меняет его настройки.

Дополнительные платные службы и секреты не требуются: workflow использует встроенный токен GitHub только для публикации в этот форк. У GitHub действуют собственные правила доступности и приостановки расписаний; состояние последнего запуска видно на вкладке Actions. Если Actions отключены, включите их там.

## Данные и проверяемость

- [`services.json`](https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/services.json) — полный машиночитаемый справочник.
- [`build-info.json`](https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/build-info.json) — время, исходный commit и статистика сборки.
- [`SHA256SUMS.txt`](https://raw.githubusercontent.com/DarkAssassin48/russia-v2ray-rules-dat/release/SHA256SUMS.txt) — SHA-256 всех опубликованных файлов.
- `geoip.dat`, `geosite.dat`, `sing-box/` и `sing-box.zip` сохраняют исходные категории runetfreedom. Дополнения находятся в `custom/`.
- Стабильные идентификаторы существующих пунктов не меняются при обновлении содержимого.

## Разработка

Нужен Python 3.11+ без сторонних пакетов и официальный CLI sing-box. CLI используется только для компиляции / декомпиляции SRS; сетевой туннель не запускается. Генератор сохраняет совместимый SRS v1 для дополнительных профилей.

```sh
python -m unittest discover -s tests -v
python scripts/build_catalog.py --repository DarkAssassin48/russia-v2ray-rules-dat --output publish --work .build/run --cache .cache --sing-box /path/to/sing-box --jobs 4
python scripts/verify_generated.py publish --repository DarkAssassin48/russia-v2ray-rules-dat
```

Выходная папка должна быть пустой. Профили задаются в [`catalog/profiles.json`](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/main/catalog/profiles.json), русские названия — в [`catalog/labels.json`](https://github.com/DarkAssassin48/russia-v2ray-rules-dat/blob/main/catalog/labels.json). Не заменяйте URL на чужие исполняемые скрипты. Публикация ограничена этим форком.

## Источники и лицензия

Форк распространяется с исходной лицензией [GPL-3.0](LICENSE). Сохранены [исходное описание и благодарности runetfreedom](UPSTREAM.md). Правила поступают из [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat), который объединяет [russia-blocked-geosite](https://github.com/runetfreedom/russia-blocked-geosite), [russia-blocked-geoip](https://github.com/runetfreedom/russia-blocked-geoip), [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community) и перечисленные там источники. Официальный компилятор — [SagerNet/sing-box](https://github.com/SagerNet/sing-box).
