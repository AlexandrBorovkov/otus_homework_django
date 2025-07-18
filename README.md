## ДЗ ##
Обучающий сайт на выбранную тему

Создать проект django

Настроить его

Создать модели данных

Провести миграции

Подключить админку


В проект добавляем страницы

Пока добавляем классические страницы с рендерингом на сервере

Добавить страницу для просмотра списка курсов

Добавить страницу для просмотра одного курса

Добавить страницы для создания, удаления, редактирования курса

## Как установить и запустить приложение? ##
1. **Клонирование репозитория**:
    ```sh
    git clone https://github.com/AlexandrBorovkov/otus_homework_django.git
   ```
    или
    ```sh
    git clone git@github.com:AlexandrBorovkov/otus_homework_django.git
    ```
2. **Создайте файл .env (смотри образец .env.example)**
3. **Установка зависимостей**:
    - Установить uv:
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
    ```
    ```sh
    make install
    ```
    - Установить redis:
    ```sh
    sudo apt-get update
    sudo apt-get install redis
    ```
4. **Миграции**:
    ```sh
    make migrate
    ```
5. **Регистрация яндекс-аккаунта**:

    Регистрируем и настраиваем почту в соответствии с документацией:

    https://yandex.ru/support/yandex-360/customers/mail/ru/mail-clients/others.html
6. **Запуск приложения**:
    ```sh
    make start
    ```