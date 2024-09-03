**__Проект Django**

---Описание проекта---

Это проект Django, предназначенный для удержания текущих клиентов и привлечения новых. В качестве основной методики используются вспомогательные, или «прогревающие», информационные рассылки. 

Разработка проекта ведется на связке pip-venv и список необходимых для работы проекта библиотек хранится в requirements.txt в корневом каталоге проекта.

В данном проекте вы можете зарегистрироваться, просматривать товары и статьи в блоге, а также редактировать их при определенных условиях (если у вас есть права, либо вы являетесь админом, либо владельцем сообщения/рассылки/клиента).

---Установка---
1) Скачайте и распакуйте архив проекта;
2) Откройте терминал и перейдите в папку проекта;
3) Настройте виртуальное окружение проекта, подготовьте БД, а также при кэшировании - брокер(redis);
4) Заполните файл .env по примеру .env.sample;
5) Введите команду python manage.py runserver для запуска сервера Django.
   
---Заполнение данными и применения миграций---
1) Примените миграции, используя команду: python manage.py migrate;
2) Для заполнения базы данных данными, используйте команду python manage.py loaddata base_buckup.json.
Эти команды настроят БД под нужды проекта, а так же произведут наполнение некоторыми стандартными данными из фикстуры all_data.json.

---Настройка проекта---

Проект использует стандартные настройки Django и не требует дополнительной настройки. 