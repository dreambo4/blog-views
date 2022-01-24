import json

from articles_model import ArticlesModel


def get_col_name():
    return ['no.', '文章', '瀏覽次數']


def get_posts_cnt():
    file = open('config/config.json')
    data = json.load(file)
    return data['posts_cnt']


class ArticlesController:
    def __init__(self):
        model = ArticlesModel()
        self.articles = model.get()

    def get(self):
        return self.articles

    def count(self):
        return len(self.articles)

    def get_views_sum(self):
        views_sum = 0
        for article in self.articles:
            views_sum = views_sum + article[2]
        return views_sum
