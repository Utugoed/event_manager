### Event manager

Для запуска приложения достаточно склонировать репозиторий
и из папки с проектом запустить Docker-Compose  
`git clone https://github.com/Utugoed/event_manager.git`  
`docker-compose up`

Чат доступен только по JWT  
Аторизоваться можно прямо в браузере /api/token  
Токен будет сохранен в кукис и в дальнейшем подставлен  
в заголовок, поэтому в браузере можно проверить и остальные  
эндпоинты  
  
Также я не успел зааменить БД с SQLite или организовать  
какую бы то ни было инициализацию в docker-compose,  
поэтому файл сохранен как есть, со всеми данными  
  
В админ панель можно зайти с данными - admin@ad.min - password  
  
Список эндпоинтов
- admin/ - Admin panel
- api/ events - List of events
- api/ events/create - Create event
- api/ events/\<int:id\> - Event detail
- api/ organisations - List of organisations / Create organisation
- api/ register - Create user
- api/ token - Auth
- api/ token/refresh - Refresh token
- chat/ - Choose chat
- chat/ \<str:room_name\> - Chat with somebody
