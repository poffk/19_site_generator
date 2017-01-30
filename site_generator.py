import json
import os.path
import jinja2
import argparse
import re
from markdown import markdown
from html import escape
from urllib.parse import quote


def argparser():
    parser = argparse.ArgumentParser(description='Генератор сайтов')
    parser.add_argument('path_to_config',
                        help='Введите путь до конфига в формате json')
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return json.load(data_file)


def read_from_file(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return data_file.read()


def config_content_ext_change(config):
    new_config = config
    for topic in new_config['topics']:
        for article in new_config['articles']:
            if topic['slug'] == article['topic']:
                original_root, original_ext = os.path.splitext(article['source'])
                article['source'] = escape('{}.html'.format(original_root))
    return new_config


def load_article(path):
    with open(path, encoding='UTF-8') as data_file:
        return markdown(data_file.read(), extensions=['codehilite', 'fenced_code'])


def get_article_url(source):
    source_with_dir = os.path.join('pages', source)
    original_root, original_ext = os.path.splitext(source_with_dir)
    source = '{}.{}'.format(original_root, 'html')
    return source


def directory_create(path):
    if not os.path.exists(os.path.split(path)[0]):
        os.makedirs(os.path.split(path)[0])


def compile_page(config, path_to_template, path_to_save):
    html_page = read_from_file(path_to_template)
    template = jinja2.Template(html_page)
    with open(path_to_save, 'w', encoding='utf-8') as f:
        f.write(template.render(info=config))


def compile_article(config, path_to_template):
    for topic in config['topics']:
        for article in config['articles']:
            if topic['slug'] == article['topic']:
                path_to_save = get_article_url(article['source'])
                directory_create(path_to_save)
                article_text = load_article(os.path.join('articles', article['source']))
                article_content = {'title': article['title'],
                                   'content': article_text}
                compile_page(article_content, path_to_template, path_to_save)


if __name__ == '__main__':
    parser = argparser()
    all_articles_information = load_data(parser.path_to_config)
    compile_article(all_articles_information, 'templates/article.html')
    all_articles_information_formatted = config_content_ext_change(all_articles_information)
    compile_page(all_articles_information_formatted, 'templates/index.html', 'pages/index.html')
