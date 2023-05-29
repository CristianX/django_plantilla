# Motor de inferencia con DJango

## 1. Para la ejecución incial del proyecto

- python manage.py migrate
- python manage.py runserver

## 2. Para la migración de modelos personalizados (Existentes en app)

1. python manage.py makemigrations
<!-- Obteniendo un id de la migración Ejem. 001 -->
2. python manage.py sqlmigrate motorInferencia 001
3. python manage.py migrate
