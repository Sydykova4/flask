from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user

from app.extensions import db
from app.models.post import Post


post = Blueprint('post', __name__)


@post.route('/', methods=['POST', 'GET'])
def all_no_auth():
    posts = Post.query.order_by(Post.date).all()
    return render_template('post/all_no_auth.html', posts=posts)


@post.route('/all_auth', methods=['POST', 'GET'])
def all_auth():
    posts = Post.query.order_by(Post.date).all()
    return render_template('post/all_auth.html', posts=posts)


@post.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        tag = request.form.get('tag')
        theme = request.form.get('theme')

        post = Post(author_id=current_user.id, title=title, text=text, tag=tag, theme=theme)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('post.my_posts'))
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/create.html')


@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    post = Post.query.qet(id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.text = request.form.get('text')
        post.tag = request.form.get('tag')
        post.theme = request.form.get('theme')

        try:
            db.session.commit()
            return redirect('post/all_auth')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/update.html', post=post)


@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
    post = Post.query.qet(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('post/all_auth')
    except Exception as e:
        print(str(e))
        return str(e)


@post.route('/post/my_posts', methods=['POST', 'GET'])
def my_posts():
    user = current_user.id
    posts = Post.query.filter(Post.author_id == user).order_by(Post.date.desc()).all()
    return render_template('post/my_posts.html', posts=posts, user=user)


# @post.route('/post/<int:id_post>', methods=['POST', 'GET'])
# def post_unique(id):
#     post = Post.query.get(id)
#     content = Post.query.filter_by(Post.id == id).all()
#     return render_template('post/post_unique.html', post=post, content=content, post_id=post.id)
