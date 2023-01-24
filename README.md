# Проектная работа: диплом
[![CI](https://github.com/aigt/graduate_work/actions/workflows/main.yml/badge.svg)](https://github.com/aigt/graduate_work/actions/workflows/main.yml)

У вас будет один репозиторий на все 4 недели работы над дипломным проектом.

Если вы выбрали работу в командах, ревью будет организовано как в командных модулях с той лишь разницей, что формируете состав команды и назначаете тимлида вы сами, а не команда сопровождения.

Удачи!


### Документация

Сервис реализован в соответствии с разработанным проектным заданием:

- [documentation/Statement.md](documentation/Statement.md) проектное задание


## CI

### GitHub Workfow

Перед слиянием с основной веткой пул реквест должен пройти проверки автоматические.


### Pre-Commit

Для атоматической предварительной проверки перед коммитом используйте [pre-commit](https://pre-commit.com/)

1. Установка - см. инструкцию на сайте: https://pre-commit.com/

2. Инициализация для автоматической проверки всех коммитов:
```bash
pre-commit install
```

3. Проверка всех файлов:
```bash
pre-commit run --all-files
```


## Репозитории сервисов инфраструктуры онлайн-кинотеатра
В инфраструктуру сервиса онлайн-кинотеатр входят следующие микросервисы:

- **Admin Panel** - панель для администрирования базы фильмов
  - https://github.com/aigt/new_admin_panel_sprint_1

- **API** - сервис предоставляющий интерфейс для работы пользователей с базой фильмов:
  - https://github.com/aigt/Async_API_sprint_2

- **Auth** - сервис авторизации и аутентификации пользователей:
  - https://github.com/aigt/Auth_sprint_1

- **Analitical Data** - сервис обработки больших объёмов аналитической информации:
  - https://github.com/aigt/ugc_sprint_1

- **UGC** - Контент создаваемый пользователями:
  - https://github.com/aigt/ugc_sprint_2

- **Notifications Service** - Сервис оповещений:
  - https://github.com/aigt/notifications_sprint_1

- **Billing Service** - Сервис биллинга:
  - https://github.com/aigt/graduate_work


## Запуск сервиса

1. В директории [env_files](env_files) скопируйте и переименуйте файлы `*.env.example` в `*.env`, внесите в скопированные файлы необходимые правки

2. В корневой дериктории приложения
```commandline
docker-compose up --build -d
```


## Ссылка на данный репозиторий

https://github.com/aigt/graduate_work
