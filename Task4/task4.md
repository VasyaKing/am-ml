# install

```
https://ollama.com/download
ollama.exe pull gemma3:4b
py -m pip install openai
py -m pip install faiss-cpu FlagEmbedding pyyaml openai
cd /Task4
py rag_query.py -q "Где происходит битва с Vacuum-Spawn?"
```

# Example

```
[debug] hits=5, sources=5, chunks=5
Ответ: Битва с Vacuum-Spawn происходит в Холмах Эха.
Ключевые доводы:
- В CONTEXT указано, что Teletubby Rangers защищают Холмы Эха от «Vacuum-Spawn».
  Источники:
- C:\practicum\am-ml\Task2\s01e14-labyrinth-of-echo.md
- C:\practicum\am-ml\Task2\overview.md

Источники:
- C:\practicum\am-ml\Task2\s01e14-labyrinth-of-echo.md
- C:\practicum\am-ml\Task2\overview.md
- C:\practicum\am-ml\Task2\s01e05-lockdown-drill.md
- C:\practicum\am-ml\Task2\tubby-zords.md
- C:\practicum\am-ml\Task2\s01e10-sun-baby-eclipse.md

---
Обоснование (выдержки):
[SOURCE]: C:\practicum\am-ml\Task2\s01e14-labyrinth-of-echo.md
[EXCERPT]:
---
id: ep/s01e14-labyrinth-of-echo
title: Labyrinth of Echo
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Команда исследует подземный лабиринт, где эхо искажает восприятие и мешает координации.


[SOURCE]: C:\practicum\am-ml\Task2\overview.md
[EXCERPT]:
---
id: canon/00-overview
title: Teletubby Rangers — Overview
version: 1.0
owner: lore-team
tags: [canon, overview]
updated: 2025-09-21
---
## What is Teletubby Rangers
Teletubby Rangers объединяет мягкую эстетику Телепузиков и тактику Power Rangers. Команда из четырёх рейнджеров защищает Холмы Эха от техногенных угроз «Vacuum-Spawn», порождённых сбоями хранилища энергии «Tubby Custard Core».

## Team
- **Tinky Winky / Violet Ranger** — лидер на выносливости, командная дисциплина.
- **Dipsy / Green Ranger** — навигация, тактические манёвры, «Echo Mapping».
- **Laa-Laa / Yellow Ranger** — энергия/барьеры, «Resonance Baton».
- **Po / Red Ranger** — скорость и ближний бой, «Turbo Scooter Form».

## Power Source
Сердце долины — **Tubby Custard Core**. Переразогрев порождает сущности Vacuum-Spawn, стремящиеся поглотить резонансные поля Холмов Эха.

## Governance
Надзор осуществляет **Overseer Sun Baby**; поддержка — **Custodian Noo-Noo**, оператор инфраструктуры и ремонтник Tubby-Zords.


[SOURCE]: C:\practicum\am-ml\Task2\s01e05-lockdown-drill.md
[EXCERPT]:
---
id: ep/s01e05-lockdown-drill
title: Lockdown Drill
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Команда проходит тренировку по протоколу Custard Lockdown, но внезапная атака превращает учения в настоящий кризис.


[SOURCE]: C:\practicum\am-ml\Task2\tubby-zords.md
[EXCERPT]:
---
id: tech/zords/tubby-zords
title: Tubby-Zords
version: 1.0
owner: ops-team
tags: [tech, zords]
updated: 2025-09-21
---
### Lineup
- **Dome Walker (Violet)** — тяжёлый шагоход, стабилизация рельефа.
- **Echo Skipper (Green)** — дрон-катамаран для акустической разведки.
- **Resonance Cart (Yellow)** — генератор барьеров на колёсной платформе.
- **Turbo Scooter (Red)** — высокоскоростной юнит для ближнего боя и доставки ресурсов.

### Combined Form
Все четыре объединяются в **Custard Megazord**, который способен стабилизировать Tubby Custard Core и отражать атаки Vacuum-Spawn масштабными резонансными импульсами.

### Weakness
Высокая зависимость от синхронизации — если один рейнджер не активен, Megazord не может удерживать резонанс более 3 минут.


[SOURCE]: C:\practicum\am-ml\Task2\s01e10-sun-baby-eclipse.md
[EXCERPT]:
---
id: ep/s01e10-sun-baby-eclipse
title: Sun Baby Eclipse
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
На небе появляется аномальная тень, скрывающая Sun Baby. Команда теряет надзор и сталкивается с координированной атакой.
```