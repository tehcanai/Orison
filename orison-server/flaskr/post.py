
from flask import (Blueprint, g, request, render_template, jsonify)

from flaskr.db import get_db, query_db

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/', methods=['GET'])
def posts_status():
    db = get_db()
    available = db.execute('SELECT * FROM post').fetchone()

    if available is None :
        return "No posts. Please add new posts."
    else :
        posts = []
        for post in query_db('SELECT * FROM post'):
            posts.append({
            'title': post['title'],
            'body': post['body'],
            })
        return jsonify(posts)

@bp.route('/new', methods=['POST'])
def store_post():
    if request.method == 'POST' :
        post_title = request.form['title']
        post_body = request.form['body']
        
        db = get_db()
        db.execute('INSERT INTO post (title, body) VALUES (?, ?)', (post_title, post_body))
        db.commit()

        return "Post sent"
