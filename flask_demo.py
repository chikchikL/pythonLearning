from flask import Flask
from flask import request, render_template

# 模板使用的是jinja2，{{xxx}}表示一个需要替换的变量，{%...%}表示指令
app = Flask(__name__)


# 通过装饰器在内部匹配url和函数
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    # 从request对象读取提交的表单内容
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='输入有误啊', username=username)


if __name__ == '__main__':
    app.run()
