Feature: API-Статьи-Поиск статей по названию с сортировкой

  Scenario Outline: Поиск статей по названию с сортировкой
    Given URL API-запрос "https://startupium.ru/api/blogs"
    And Заданы параметры
      | ключ          | значение     |
      | sortBlogsBy   | <sort>       |
      | titleBlog     | <title>      |
    When Пользователь отправляет GET-запрос с параметрами
    Then Получен статус-код 200
    And В ответе есть данные статьи/статей: id, title и status

    Examples:
      | sort                 | title        |
      | Свежее               | Интеллект    |
      | Популярное           | Блоги        |
