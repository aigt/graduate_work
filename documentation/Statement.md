# Биллинг - проектное задание

**Сложность**: высокая

**Команда**: ~4 человека

Выполните проект «Биллинг».
- Нужно сделать два метода работы с картами:
  - оплатить подписку
  - вернуть за неё деньги

- При этом система должна быть устойчивой к перебоям:
  - не должно происходить двойных списаний
  - у пользователя всегда была гарантия, что операция выполнилась

- Помимо реализации системы, интегрируйте эту систему с админкой Django, чтобы:
  - вы могли контролировать оплату подписок клиентами


## Основные сценарии работы с сервисом

### Оплатить подписку

```mermaid

sequenceDiagram
  actor User as User Client
  participant Billing as Billing Service
  participant PDB as Payment DB
  participant PAPI as Payment Service API
  participant PP as Payment Page
  participant Auth as Auth API
  participant NS as Notification Service


  rect rgb(31, 97, 141)

    note right of Billing: Пользователь решил оплатить подписку.

    User ->> Billing: Оплати подписку

    Billing ->> PAPI: Создать платёж

    PAPI ->> Billing: Данные платежа

    Billing ->> PDB: Занести данные созданного платежа
    PDB ->> Billing: Done

    Billing ->> User: Перенаправление


  end

  User ->> PP: Данные платежа
  PP -->> User: Выбор нужного способа оплаты
  User -->> PP: Способ оплаты
  PP -->> User: Запрос подтверждения
  User -->> PP: Подтверждение

  par
    PP ->> User: Перенаправление на страницу кинотеатра
  and

    PP ->> PAPI: Платёж прошёл

    rect rgb(25, 111, 61)

      note right of Billing: Платёжная система оповещает о проведённом платеже.

      PAPI ->> Billing: Оповещение о проведённом платеже

      Billing ->> PDB: Получить данные по платежу
      PDB ->> Billing: Данные

      Billing ->> Auth: Добавить пользователю статус подписчика
      Auth ->> Billing: Готово

      Billing ->> NS: Отправить пользователю оповещение оп платеже

    end
  end


```

### Вернуть деньги за подписку

```mermaid

sequenceDiagram
  actor User as User Client
  participant Billing as Billing Service
  participant PDB as Payment DB
  participant PAPI as Payment Service API
  participant Auth as Auth API
  participant NS as Notification Service

  note right of Billing: Пользователь решил вернуть деньги.

  User ->> Billing: Верни деньги

  Billing ->> PDB: Запрос данных платежа пользователя
  PDB ->> Billing: Данные

  Billing ->> PAPI: Создать возврат (payment_id и amount)
  PAPI ->> Billing: Данные возврата

  Billing ->> PDB: Обнови данные платежа
  PDB ->> Billing: Done

  Billing ->> Auth: Отмени подписку (user_id)
  Auth ->> Billing: Done

  Billing ->> NS: Отправь уведомление о возврате
  NS ->> Billing: Done

  Billing ->> User: Done

```
### Payments history DB

Схема в БД для данных: `payments_history`


Данные по истории платежей:

```mermaid
erDiagram

    payments {
        user_id uuid
        amount decimal
        external_id uuid
        external_payment jsonb
        refunded boolean
        system_id uuid
    }

    subscribers {
        user_id uuid
        subscriber_status boolean
        date_subscribe date
    }

```
