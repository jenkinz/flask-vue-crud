from flask import Blueprint
from flask import jsonify
from flask import request
from werkzeug.exceptions import abort

# from flask import flash
# from flask import g
# from flask import redirect
# from flask import render_template

# from flask import url_for

# from server.auth import login_required
# from server.db import get_db

bp = Blueprint("books", __name__)

BOOKS = [
    {"title": "On the Road", "author": "Jack Kerouac", "read": True},
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "read": False,
    },
    {"title": "Green Eggs and Ham", "author": "Dr. Seuss", "read": True},
]


@bp.route("/books", methods=["GET", "POST"])
def all_books():
    response = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append(
            {
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "read": post_data.get("read"),
            }
        )
        response["message"] = "Book added!"
    else:
        response["books"] = BOOKS
    return jsonify(response)


@bp.route("/")
def index():
    abort(404)


#     db = get_db()
#     posts = db.execute(
#         "SELECT p.id, title, body, created, author_id, username"
#         " FROM post p JOIN user u ON p.author_id = u.id"
#         " ORDER BY created DESC"
#     ).fetchall()
#     return render_template("blog/index.html", posts=posts)

# @bp.route("/create", methods=("GET", "POST"))
# @login_required
# def create():
#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None
#
#         if not title:
#             error = "Title is required."
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "INSERT INTO post (title, body, author_id)"
#                 " VALUES (?, ?, ?)",
#                 (title, body, g.user["id"]),
#             )
#             db.commit()
#             return redirect(url_for("blog.index"))
#
#     return render_template("blog/create.html")


# def get_post(id, check_author=True):
#     post = (
#         get_db()
#             .execute(
#             "SELECT p.id, title, body, created, author_id, username"
#             " FROM post p JOIN user u ON p.author_id = u.id"
#             " WHERE p.id = ?",
#             (id,),
#         )
#             .fetchone()
#     )
#
#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")
#
#     if check_author and post["author_id"] != g.user["id"]:
#         abort(403)
#
#     return post


# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# @login_required
# def update(id):
#     post = get_post(id)
#
#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None
#
#         if not title:
#             error = "Title is required."
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "UPDATE post SET title = ?, body = ?" " WHERE id = ?",
#                 (title, body, id),
#             )
#             db.commit()
#             return redirect(url_for("blog.index"))
#
#     return render_template("blog/update.html", post=post)


# @bp.route("/<int:id>/delete", methods=("POST",))
# @login_required
# def delete(id):
#     get_post(id)  # ensures post exists and belongs to logged-in user
#     db = get_db()
#     db.execute("DELETE FROM post WHERE id = ?", (id,))
#     db.commit()
#     return redirect(url_for("blog.index"))
