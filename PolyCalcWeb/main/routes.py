from flask import render_template, request, Blueprint
from PolyCalcWeb.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/economy")
def economy():
    return render_template('economy.html')

@main.route("/forum")
def forum():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('forum.html', posts=posts)