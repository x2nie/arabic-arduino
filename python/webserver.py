import os
from bottle import route, run, static_file

# cwd = os.getcwd()
cwd = os.path.dirname(os.path.realpath(__file__))
print(cwd)
static_dir = os.path.join(cwd, 'static')
print('static_dir:', static_dir)

@route('/')
def root():
    return static_file('index.html', root=static_dir)


@route('/hello')
def hello():
    return "Hello World!"

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root=static_dir)


run(host='localhost', port=8081, debug=True)