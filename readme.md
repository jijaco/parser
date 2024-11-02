# Анализ задачи

## 1. Что было сделано

Был написан парсер для сбора цитат и их авторов со страницы <https://quotes.toscrape.com/>.

## 2. Откуда были получены данные

Данные были получены через get-запрос с помощью библиотеки requests.

## 3. Как осуществлялся сбор  

Использовалась библиотека Beautiful Soup.

Проанализировав страницу я пришел к выводу что все цитаты находятся по тегу <div class="quote">.

Текст цитаты находится внутри тега <span class="text">, а автор записан внутри тега  <small class="author">.

## 4. Почему был выбран тот или иной метод/инструмент, а не другой

Requests позволяет легко получить данные с сайта — всего лишь одна строчка кода с GET-запросом.

Beautiful Soup использовался по той же причине и, к тому же, обладает интуитивно понятным интерфейсом.
