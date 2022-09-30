from bottle import route, run, static_file

@route('/')
def root():
    return static_file('index.html', root='./static')


@route('/hello')
def hello():
    return "Hello World!"

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')


run(host='localhost', port=8081, debug=True)