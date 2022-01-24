from connector import DBConnector


class ArticlesModel:
    def __init__(self):
        db = DBConnector().get_instance()
        self.articles_ref = db.collection(u'articles')

    def get(self):
        docs = self.articles_ref.stream()
        articles = []
        for idx, doc in enumerate(docs):
            articles_info = doc.to_dict()
            articles.append([idx + 1, doc.id, articles_info['count']])
        return articles
