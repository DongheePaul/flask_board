from flask import Flask


# 함수명을 create_app 대신 다른 이름으로 사용하면 정상적으로 작동하지 않는다. 플라스크 내부에서 정의된 함수명. create_app 함수 = 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)

    from .views import main_views

    app.register_blueprint(main_views.bp)

    return app
