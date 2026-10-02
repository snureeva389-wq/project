# project — Бот-каталог книг с поиском по цитатам

**Лабораторные работы 1–2: Инициация проекта и Git-флоу**

## Что это

Telegram-бот, который находит книгу по фразе из неё, выдаёт случайные
цитаты и ведёт трекер чтения.

## Цель

Решить проблему: человек помнит цитату, но не помнит автора и название.
Обычные каталоги ищут только по названию и автору — не по содержимому.

## Ключевые функции

- Поиск книги по цитате (полнотекстовый поиск).
- Случайная цитата дня.
- Трекер чтения: «читаю / прочитано / хочу».
- Напоминания о чтении.
- Кнопка «Купить» с партнёрской ссылкой.

## Wiki

Вся проектная документация — в Wiki:

👉 https://github.com/snureeva389-wq/project/wiki

- [Home](https://github.com/snureeva389-wq/project/wiki/Home)
- [Ideas](https://github.com/snureeva389-wq/project/wiki/Ideas)
- [Evaluation](https://github.com/snureeva389-wq/project/wiki/Evaluation)
- [Concept](https://github.com/snureeva389-wq/project/wiki/Concept)
- [Stakeholders](https://github.com/snureeva389-wq/project/wiki/Stakeholders)

## Структура репозитория
project/
├── README.md # описание проекта
├── LICENSE # лицензия MIT
├── .gitignore # игнорируемые файлы
├── src/ # исходный код бота
│ └── README.md
├── content/ # тексты, цитаты, материалы
│ └── index.md
└── data/ # база цитат и книг
└── README.md

## Как запустить

Проект в разработке. MVP появится в следующих лабораторных.
Планируемый стек: Python 3.11, aiogram 3.x, SQLite + FTS5.

## Эксперты

- Снуреева А. — менеджер проекта, эксперт 1
- Одногруппник 1 — эксперт 2
- Одногруппник 2 — эксперт 3

## Лицензия

MIT — см. файл [LICENSE](LICENSE).
