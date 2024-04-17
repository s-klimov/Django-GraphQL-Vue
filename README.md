# Blog Using Django, GraphQL, and Vue

## Настроить среду разработки

### Запуск СУБД Postgresql

```shell
docker run --name my-blogs -e POSTGRES_USER=developer -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=blog -p 5440:5432 -d postgres
```

### Настройка переменных окружения

1. Скопируйте файл .env.dist в .env
2. Заполните .env файл. Пример:

```yaml
DATABASE_URL = postgresql://developer:secret@localhost:5440/blog
SECRET_KEY = "django-insecure-&r7sbqng#dfgd(k@mml_dqd%omgqvjh2+0m0-o0jijpnr_)hqt"
```

### Создание и активация виртуального окружения, установка зависимостей
```shell
cd back_end
python -m venv venv
source venv/bin/activate
pip install -r requirements/develop.txt  
```