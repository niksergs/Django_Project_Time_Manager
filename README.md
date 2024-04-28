# TODO APP

Приложение, отображающее список дел, созданное для ознакомления с Django Framework. Для отображения frontend части
используется Django Template Language и Semantic UI.

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Django_Project_Time_Manager
    cd time_manager

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements.txt

Run the app locally:
    
    npm run start
    python manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    pip install gunicorn
    gunicorn backend_api.wsgi:application -b 0.0.0.0:8000
    
