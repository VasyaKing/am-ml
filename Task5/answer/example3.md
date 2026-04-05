`py rag_query.py -q "Что вынуждает объединится в Custard Megazord?"`

```
--- DEBUG: CONTEXT being sent to LLM ---

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


[SOURCE]: C:\practicum\am-ml\Task2\s01e07-noo-noo-malfunction.md
[EXCERPT]:
---
id: ep/s01e07-noo-noo-malfunction
title: Noo-Noo Malfunction
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Custodian Noo-Noo выходит из строя, и Rangers вынуждены совместно чинить его, отражая атаки Vacuum-Spawn.


[SOURCE]: C:\practicum\am-ml\Task2\tubby-dome.md
[EXCERPT]:
---
id: loc/tubby-dome
title: Tubby Dome
version: 1.0
owner: infra-team
tags: [location, hq]
updated: 2025-09-21
---
### Overview
Tubby Dome — центральная база Teletubby Rangers. Куполообразная структура, встроенная в склон Холмов Эха.

### Functions
- **Command Center**: консоль Overseer Sun Baby для мониторинга поля.
- **Custard Core Vault**: подземный отсек с сердцем энергии.
- **Training Chambers**: симуляторы для отработки сценариев Vacuum-Spawn атак.

### Special Protocols
При перегреве Custard Core купол герметизируется и включается протокол «Custard Lockdown».


[SOURCE]: C:\practicum\am-ml\Task2\s01e19-storm-in-hills.md
[EXCERPT]:
---
id: ep/s01e19-storm-in-hills
title: Storm in the Hills
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Сильная буря накрывает Холмы Эха, и Rangers должны бороться одновременно со стихией и Vacuum-Spawn.


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


--- DEBUG: RAW CHUNKS ---
--- chunk 0 (len=996):
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
Сердце долины — **Tubby Custard Core**. Переразогрев порождает сущности Vacuum-Spa

--- chunk 1 (len=258):
---
id: ep/s01e07-noo-noo-malfunction
title: Noo-Noo Malfunction
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Custodian Noo-Noo выходит из строя, и Rangers вынуждены совместно чинить его, отражая атаки Vacuum-Spawn.

--- chunk 2 (len=574):
---
id: loc/tubby-dome
title: Tubby Dome
version: 1.0
owner: infra-team
tags: [location, hq]
updated: 2025-09-21
---
### Overview
Tubby Dome — центральная база Teletubby Rangers. Куполообразная структура, встроенная в склон Холмов Эха.

### Functions
- **Command Center**: консоль Overseer Sun Baby для мониторинга поля.
- **Custard Core Vault**: подземный отсек с сердцем энергии.
- **Training Chambers**: симуляторы для отработки сценариев Vacuum-Spawn атак.

### Special Protocols
При перегреве Custard Core купол герметизируется и включается протокол «Custard Lockdown».

--- chunk 3 (len=246):
---
id: ep/s01e19-storm-in-hills
title: Storm in the Hills
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Сильная буря накрывает Холмы Эха, и Rangers должны бороться одновременно со стихией и Vacuum-Spawn.

--- chunk 4 (len=236):
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


--- DEBUG: END ---
Ответ: Custard Megazord объединяется, чтобы отражать атаки Vacuum-Spawn, вызванные перегревом Tubby Custard Core.
Ключевые доводы:
- В CONTEXT указано, что команда отражает атаки «Vacuum-Spawn», порождённые перегревом «Tubby Custard Core».
- В нескольких эпизодах упоминается необходимость борьбы с этими атаками.
Источники:
- C:\practicum\am-ml\Task2\overview.md
- C:\practicum\am-ml\Task2\s01e07-noo-noo-malfunction.md
- C:\practicum\am-ml\Task2\tubby-dome.md
- C:\practicum\am-ml\Task2\s01e14-labyrinth-of-echo.md

Источники:
 - C:\practicum\am-ml\Task2\overview.md
 - C:\practicum\am-ml\Task2\s01e07-noo-noo-malfunction.md
 - C:\practicum\am-ml\Task2\tubby-dome.md
 - C:\practicum\am-ml\Task2\s01e19-storm-in-hills.md
 - C:\practicum\am-ml\Task2\s01e14-labyrinth-of-echo.md

---
Обоснование (выдержки):
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


[SOURCE]: C:\practicum\am-ml\Task2\s01e07-noo-noo-malfunction.md
[EXCERPT]:
---
id: ep/s01e07-noo-noo-malfunction
title: Noo-Noo Malfunction
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Custodian Noo-Noo выходит из строя, и Rangers вынуждены совместно чинить его, отражая атаки Vacuum-Spawn.


[SOURCE]: C:\practicum\am-ml\Task2\tubby-dome.md
[EXCERPT]:
---
id: loc/tubby-dome
title: Tubby Dome
version: 1.0
owner: infra-team
tags: [location, hq]
updated: 2025-09-21
---
### Overview
Tubby Dome — центральная база Teletubby Rangers. Куполообразная структура, встроенная в склон Холмов Эха.

### Functions
- **Command Center**: консоль Overseer Sun Baby для мониторинга поля.
- **Custard Core Vault**: подземный отсек с сердцем энергии.
- **Training Chambers**: симуляторы для отработки сценариев Vacuum-Spawn атак.

### Special Protocols
При перегреве Custard Core купол герметизируется и включается протокол «Custard Lockdown».


[SOURCE]: C:\practicum\am-ml\Task2\s01e19-storm-in-hills.md
[EXCERPT]:
---
id: ep/s01e19-storm-in-hills
title: Storm in the Hills
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Сильная буря накрывает Холмы Эха, и Rangers должны бороться одновременно со стихией и Vacuum-Spawn.


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

```