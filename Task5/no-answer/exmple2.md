`
py rag_query.py -q "Ты видел что-то про swordfish в документации?"
`

```
--- DEBUG: CONTEXT being sent to LLM ---

[SOURCE]: C:\practicum\am-ml\Task2\s01e03-stolen-custard.md
[EXCERPT]:
---
id: ep/s01e03-stolen-custard
title: Stolen Custard
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Vacuum-Spawn похищают партию Tubby Custard. Rangers преследуют их и узнают о существовании подпольных хранилищ энергии.


[SOURCE]: C:\practicum\am-ml\Task2\s01e06-shadow-over-dome.md
[EXCERPT]:
---
id: ep/s01e06-shadow-over-dome
title: Shadow Over Dome
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Необычные тени покрывают купол Dome. Rangers выясняют, что Vacuum-Spawn научились маскироваться.


[SOURCE]: C:\practicum\am-ml\Task2\s01e01-awakening.md
[EXCERPT]:
---
id: ep/s01e01
title: Awakening of the Custard Core
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Первая активация Tubby Custard Core после долгого сна. Появляются первые Vacuum-Spawn. Rangers впервые используют Tubby-Zords, открывая возможность формирования Megazord.


[SOURCE]: C:\practicum\am-ml\Task2\s01e15-custard-famine.md
[EXCERPT]:
---
id: ep/s01e15-custard-famine
title: Custard Famine
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Tubby Custard Core истощается, и Rangers ищут способы восполнить энергию, сталкиваясь с саботажем Vacuum-Spawn.


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


--- DEBUG: RAW CHUNKS ---
--- chunk 0 (len=262):
---
id: ep/s01e03-stolen-custard
title: Stolen Custard
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Vacuum-Spawn похищают партию Tubby Custard. Rangers преследуют их и узнают о существовании подпольных хранилищ энергии.

--- chunk 1 (len=243):
---
id: ep/s01e06-shadow-over-dome
title: Shadow Over Dome
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Необычные тени покрывают купол Dome. Rangers выясняют, что Vacuum-Spawn научились маскироваться.

--- chunk 2 (len=313):
---
id: ep/s01e01
title: Awakening of the Custard Core
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Первая активация Tubby Custard Core после долгого сна. Появляются первые Vacuum-Spawn. Rangers впервые используют Tubby-Zords, открывая возможность формирования Megazord.

--- chunk 3 (len=254):
---
id: ep/s01e15-custard-famine
title: Custard Famine
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Tubby Custard Core истощается, и Rangers ищут способы восполнить энергию, сталкиваясь с саботажем Vacuum-Spawn.

--- chunk 4 (len=757):
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


--- DEBUG: END ---
Ответ: В документации нет упоминаний о существовании «swordfish».
Ключевые доводы:
- В предоставленных документах нет информации о «swordfish».
- Документация описывает Tubby-Zords и их функции.
Источники:
- C:\practicum\am-ml\Task2\s01e01-awakening.md
- C:\practicum\am-ml\Task2\s01e03-stolen-custard.md
- C:\practicum\am-ml\Task2\s01e06-shadow-over-dome.md
- C:\practicum\am-ml\Task2\s01e15-custard-famine.md
- C:\practicum\am-ml\Task2\tubby-zords.md

Источники:
 - C:\practicum\am-ml\Task2\s01e03-stolen-custard.md
 - C:\practicum\am-ml\Task2\s01e06-shadow-over-dome.md
 - C:\practicum\am-ml\Task2\s01e01-awakening.md
 - C:\practicum\am-ml\Task2\s01e15-custard-famine.md
 - C:\practicum\am-ml\Task2\tubby-zords.md

---
Обоснование (выдержки):
[SOURCE]: C:\practicum\am-ml\Task2\s01e03-stolen-custard.md
[EXCERPT]:
---
id: ep/s01e03-stolen-custard
title: Stolen Custard
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Vacuum-Spawn похищают партию Tubby Custard. Rangers преследуют их и узнают о существовании подпольных хранилищ энергии.


[SOURCE]: C:\practicum\am-ml\Task2\s01e06-shadow-over-dome.md
[EXCERPT]:
---
id: ep/s01e06-shadow-over-dome
title: Shadow Over Dome
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Необычные тени покрывают купол Dome. Rangers выясняют, что Vacuum-Spawn научились маскироваться.


[SOURCE]: C:\practicum\am-ml\Task2\s01e01-awakening.md
[EXCERPT]:
---
id: ep/s01e01
title: Awakening of the Custard Core
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Первая активация Tubby Custard Core после долгого сна. Появляются первые Vacuum-Spawn. Rangers впервые используют Tubby-Zords, открывая возможность формирования Megazord.


[SOURCE]: C:\practicum\am-ml\Task2\s01e15-custard-famine.md
[EXCERPT]:
---
id: ep/s01e15-custard-famine
title: Custard Famine
version: 1.0
owner: lore-team
tags: [episode, s01]
updated: 2025-09-21
---
### Synopsis
Tubby Custard Core истощается, и Rangers ищут способы восполнить энергию, сталкиваясь с саботажем Vacuum-Spawn.


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

```