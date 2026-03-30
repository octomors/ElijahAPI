# Запуск проекта ElijahAPI

## Требования
- Python **3.12**
- Установленный `pip` (или `uv` по желанию)

## Быстрый старт
1. Клонируйте репозиторий и перейдите в него:
   ```bash
   git clone https://github.com/octomors/ElijahAPI.git
   cd ElijahAPI
   ```

2. (Опционально) создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -e .
   ```
   или через `uv`:
   ```bash
   uv sync
   ```

4. Создайте файл окружения:
   ```bash
   cp .env.template .env
   ```

5. Запустите приложение (команда выполняется из каталога `app`):
   ```bash
   cd app
   python -m uvicorn main:main_app --reload
   ```

6. Откройте документацию API:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Настройка окружения (.env)
Файл `.env.template` содержит все необходимые переменные. Ключевые параметры:

```dotenv
APP_CONFIG__DB__URL=sqlite+aiosqlite:///./test.db
APP_CONFIG__DB__ECHO=False
APP_CONFIG__RUN__RELOAD=True
APP_CONFIG__RUN__HOST=0.0.0.0
APP_CONFIG__RUN__PORT=8000
```

### Использование PostgreSQL (опционально)
Замените строку подключения, например:
```dotenv
APP_CONFIG__DB__URL=postgresql+asyncpg://user:password@localhost:5432/elijahapi
```

## Что происходит при запуске
- Приложение автоматически создаёт таблицы в базе данных при старте.
- База данных SQLite будет создана в файле `./test.db` (если используется значение по умолчанию).

## Полезные команды
- Проверка форматирования кода:
  ```bash
  black --check --target-version py312 .
  ```

> В проекте нет настроенных тестов, поэтому отдельной команды для запуска тестового набора нет.
