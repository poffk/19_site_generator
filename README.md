# Генератор сайтов

## Данный скрипт:

Создает статический сайт на основе наборов статей формата markdown.

Для правильной работы скрипта:

• Статьи должны лежать в папке articles, шаблоны для оформления в папке templates. Html страницы, созданные скриптом, помещяются в папку pages.

• Информация о статьях хранится в файле формата json, путь до которого указывается при запуске скрипта.


## Пример запуска скрипта

	python3.5 site_generator.py [путь до конфига в формате json]

## Зависимости:

Скрипт написан на языке Python 3, поэтому требует его наличия.
Для его правильной работы нужно установить библиотеки jinja2, markdown (см. requirements).

    pip install -r requirements.txt

## Пример результата:

Пример собранного [сайта](https://poffk.github.io/19_site_generator/pages/index.html).

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
