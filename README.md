### Event manager

Для запуска приложения достаточно склонировать репозиторий
и из папки с проектом запустить Docker-Compose  
`git clone https://github.com/Utugoed/event_manager.git`  
`docker-compose up`

Есть некоторые моменты, которые я не успел исправить
- Чат
  - Я организовал странный способ авторизации
  - Если зайти в /api/token и получить токен в браузере
  - токен будет сохранен в куки и получать его /chat и /chat/<room_name>
  - будут именно из кукис
- База данных организованная в SQLite там и осталась
  - поэтому можно залогиниться в панели администратора
  - с учетной записью admin@ad.min - password
  - и не настроена инициализация данных в docker-compose
- Эндпоинты /api/events /api/events/create /api/organisations
  - доступны только авторизованным через JWT
  - и посетить я их смог только с Postman так как
  - токен необходимо поместить в заголовок Authrization

Список эндпоинтов
- admin/ - Admin panel
- api/ events - List of events
- api/ events/create - Create event
- api/ events/<int:id> - Event detail
- api/ organisations - List of organisations / Create organisation
- api/ register - Create user
- api/ token - Auth
- api/ token/refresh - Refresh token
- chat/ - Choose chat
- chat/ <str:room_name> - Chat with somebody
