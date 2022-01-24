from flask import Flask, render_template
from articles_controller import ArticlesController, get_col_name, get_posts_cnt

app = Flask(__name__)


@app.route("/")
@app.route('/views')
def views():
    controller = ArticlesController()
    print(get_col_name(), controller.get())
    return render_template('views.html',
                           title='瀏覽次數',
                           table={'head': get_col_name(),
                                  'data': controller.get()},
                           read={'all': get_posts_cnt(), 'read': controller.count()},
                           views_sum=controller.get_views_sum())


if __name__ == '__main__':
    app.run()
