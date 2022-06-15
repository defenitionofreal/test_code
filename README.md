Тестовое задание
=====================
**Описание**

В выборку попадают только Блюда у которых is_publish=True.
Если в категории нет блюд (или все блюда данной категории 
имеют is_publish=False) - не включаем ее в выборку.
  
Запрос в БД сделать любым удобным способом:
Django ORM (предпочтительно), Raw SQL, Sqlalchemy...

endpoint - 127.0.0.1:8000/api/v1/foods
______
Для того, чтобы запустить проект локально, выполните следующие команды:
```
mkdir new_project
cd new_project
python3 -m venv venv
source venv/bin/activate
git clone https://github.com/defenitionofreal/test_code.git
cd test_code
pip install -r requirements.txt
```


Новая база данных пустая. Запустите следующую команду, чтобы применить миграции:
```
export DJANGO_SETTINGS_MODULE=project.settings.local
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```

Воспульзуйтесь готовыми данными из папки fixtures:
```
python manage.py loaddata fixtures/db.json
```

Запуск:
```
python manage.py runserver
```
