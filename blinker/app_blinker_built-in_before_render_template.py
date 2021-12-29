from flask import Flask, g, request, redirect
from flask import before_render_template, render_template
"""
flask内置信号一共10个
1、before_render_template     模板渲染完成之前的信号
"""

app = Flask(__name__, template_folder='./templates')
app.config.from_pyfile('../config.py')


@app.route("/", methods=['get', 'post'])
def index():
    if request.method == 'POST':
        g.name = request.form['params']
        input()
        return redirect('/')
    else:
        return """
                <a>首页<a>
                <form action='/' method='post'>
                    <input type='text' name='params' value=''><br>
                    <input type='submit' value='提交'>
                <form>
                """

def templateRendered(sender, template, context):
    """模板渲染完成之前执行的信号"""
    print(sender)
    print(template)
    print(context)

before_render_template.connect(templateRendered)


@app.route("/result/")
def result():
    data = "江西"
    return render_template("two.html", context = data)


if __name__ == "__main__":
    app.run()
