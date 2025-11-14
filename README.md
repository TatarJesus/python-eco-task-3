# python-eco-task-3

## Описание
Реализация REST API для простого глоссария.


Поддерживаемые операции:
- Получение списка всех терминов: `GET /terms`
- Получение информации о термине по ключу: `GET /terms/{keyword}`
- Добавление нового термина: `POST /terms` (JSON `{ "keyword": "...", "description": "..." }`)
- Обновление существующего термина: `PUT /terms/{keyword}` (JSON `{ "description": "..." }`)
- Удаление термина: `DELETE /terms/{keyword}`


Применяются Pydantic/SQLModel для валидации и схем.


## Запуск локально


1. Клонировать репозиторий
2. Создать виртуальное окружение и установить зависимости


```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
