from datetime import datetime
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect

from aitest import db
from aitest.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')
grpid = 1

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/create/', methods=('POST',))
def create():
    qst = request.form['question']
    answer = request.form['answer']
    question = Question(grpid=grpid, question=qst, answer=answer, create_date=datetime.now())
    db.session.add(question)
    db.session.commit()
    return redirect(url_for('question._list'))