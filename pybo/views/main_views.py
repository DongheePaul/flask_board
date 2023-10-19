from flask import Blueprint

"""
main은 별칭. 후에 url_for 함수에서 사용.
url_prefix는 라우팅 함수의 애너테이션 url 앞에 기본으로 붙일 접두어 url을 의미.
"""
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello_pybo():
    return "Hello, Pybo!"


@bp.route("/")
def index():
    return "Pybo index"
