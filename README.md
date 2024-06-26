<h1> Тестирование онлайн кинотеатра Start.ru</h1>

> <a target="_blank" href="https://start.ru/">Ссылка на сайт</a>

![This is an image](images/main_page.png)

#### Список проверок, реализованных в автотестах:
* ✅ Проверка кликабельности кнопки "Фильмы"
* ✅ Проверка возможности выбрать сериал с определенным жанром
* ✅Проверка перехода на форму регистрации
* ✅ Проверка работоспособности поиска
* ✅ Проверка кнопки сброса фильтра
* ✅ Проверка сортировки
* ✅ Проверка кнопки ТВ
* ✅ Проверка информации в разделе "Где смотреть"
#### API тесты:
* ✅ Проверка запуска трейлера
* ✅ Проверка работы поиска по сайту
* ✅ Проверка возможности изменения языка в пользовательском соглашении
* ✅ Проверка переключения на детский режим
* ✅ Проверка перехода на раздел TV

----
## Технологии и инструменты
<p  align="center">
<img src="images/logos/python-original.svg" width="50" title="Python"> <img src="images/logos/pytest.png" width="50" title="Pytest"> <img src="images/logos/intellij_pycharm.png" width="50" title="PyCharm"> <img src="images/logos/selene.png" width="50" title="Selene"> <img src="images/logos/selenium.png" width="50" title="Selenium"> <img src="images/logos/selenoid.png" width="50" title="Selenoid"> <img src="images/logos/jenkins.png" width="50" title="Jenkins"> <img src="images/logos/allure_report.png" width="50" title="Allure Report"> <img src="images/logos/allure_testops.png" width="50" title="Allure TestOps"> <img src="images/logos/tg.png" width="50" title="Telegram"> <img src="images/logos/jira.png" width="50" title="Jira"> <img src="images/logos/github.png" width="50" title="GitHub">
</p>

----
### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/start_project/">Ссылка на проект в Jenkins</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/start_project/">Проект в Jenkins</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT
4. Указать комментарий в поле COMMENT
5. Выбрать браузер в BROWSER_NAME
6. Указать версию браузера в BROWSER_VERSION 
7. Нажать кнопку `Build`
8. Результат запуска сборки можно посмотреть в отчёте Allure

<img alt="This is an image" src="images/Allure_start.png" width="900"/>

----
### Allure-отчет


#### Общие результаты
![This is an image](images/allure_owerview.png)
#### Список тест-кейсов
![This is an image](images/Allure_test_cases.png)

----
### Allure TestOps

#### Общий список всех кейсов, имеющихся в системе
![This is an image](images/testops_test_cases.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](images/testops_dash.png)

----
### Интеграция с Jira
![This is an image](images/jira.png)

----
### Оповещение о результатах прохождения тестов в Telegram

<img alt="This is an image" height="250" src="images/tg_notifications.png"/>

### Пример видео прохождения автотеста
![autotest_gif](images/autotestgif.gif)
