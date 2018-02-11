from bottle import route, run, template

@route('/')
def crack():
    return template('index.tpl')

run(host='localhost', port=8080)
