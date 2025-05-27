Feature: API-Статьи-Поиск статей по категориям с сортировкой

  Scenario Outline: Поиск статей по категориям с сортировкой
    Given URL API-запрос "https://startupium.ru/api/blogs"
    And Заданы параметры
      | ключ          | значение    |
      | searchBlogsBy | <search>    |
      | sortBlogsBy   | <sort>      |
    When Пользователь отправляет GET-запрос с параметрами
    Then Получен статус-код 200
    And В ответе есть данные статьи/статей: id, title и status

    Examples:
      | search                | sort   |
      | Всё                   | name   |
      | Финансы и инвестиции  | date   |
      | Стартыпы и проекты    | name   |    
      | Технологии            | date   |
      | Разработка            | name   |
      | Дизайн                | date   |
      | Маркетинг             | name   |
      | Инновации             | date   |
      | PR                    | name   |
      | Менеджмент            | date   |
      | Медиа                 | name   |
      | CEO                   | date   |
      | Брендинг              | name   |
      | Образование           | date   |
      | Аналитика             | name   |
      | Data Science          | date   |