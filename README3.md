# Дипломная работа: Биллинг
![python](https://img.shields.io/badge/python-3.10-blue)
[![CI](https://github.com/aigt/graduate_work/actions/workflows/main.yml/badge.svg)](https://github.com/aigt/graduate_work/actions/workflows/main.yml)  
Сервис для оплаты подписок в онлайн-кинотеатре.

## Содержание

- [Описание проекта](#Описание)
- [Состав репозитория](#Состав)
- [Технологии](#Технологии)
- [Запуск сервиса](#Запуск)
- [Архитектура сервиса](#Архиектура)
- [Репозитории сервисов инфраструктуры онлайн-кинотеатра](#Репозитории)



## <a name="Описание">Описание проекта</a>
Сервис представляет собой платежную систему, при помощи которой пользователи могут оплачивать кредитными картами подписку в онлайн-кинотеатре. Дополнительно сервис дает возможность пользователям отказаться от подписки в любой удобный для них момент. Также в проекте присутствует панель администратора, через которую персонал может наблюдать за активностью пользователей, их подписками, и на основе этих данных проводить аналитику.
## <a name="Состав">Состав репозитория</a>

- [Administarton Panel](admin_panel) - Панель для администраторов.
- [Billng API](billing) - API платежной системы.
- [Documentation](documentation) - Документация проекта.
- [Environment variables](env_files) - Переменные окружения.
- [Nginx Configuration](nginx) - Конфигурация Nginx.
- [Database](payment_db) - База данных с информацией по платежам.
- [Scheduler](scheduler) - Сервис автоматической отмены истекших подписок.
## <a name="Технологии">Технологии</a>
* **Django** - предоставляет удобный интерфейс панели администраторов.
* **PostgreSQL** - NoSQL база.
* **Stripe** - Система обработки интернет-платежей.
* **aiohttp** - Асинхронный фреймворк для создания API платежной системы.
* **Nginx** - База данных для хранения информации о платежах.

## <a name="Запуск">Запуск сервиса</a>
1. В директории [env_files](env_files) скопируйте и переименуйте файлы `*.env.example` в `*.env`, внесите в скопированные файлы необходимые правки

2. В корневой дериктории приложения
```commandline
docker-compose up --build -d
```

## <a name="Архиектура">Архитектура сервиса</a>
![схема](https://raw.githubusercontent.com/aigt/graduate_work/main/documentation/Project_Context_Schema.png?token=GHSAT0AAAAAAB5GR53VGVHMHZX2CUPF7W2IY7HYSHA)

## <a name="Репозитории">Репозитории сервисов инфраструктуры онлайн-кинотеатра</a>
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