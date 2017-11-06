from bottle import (
    Bottle,
    post,
    get,
    put,
    delete,
    run,
    hook
)

stripAPI = Bottle()

@stripAPI.get('/api/v1/strip')
def strip_collection():
    pass

@stripAPI.post('/api/v1/strip')
def strip_creation():
    pass

@stripAPI.get('/api/v1/strip/<strip_name>')
def strip_single_get():
    pass

@stripAPI.put('/api/v1/strip/<strip_name>')
def strip_single_update():
    pass

@stripAPI.delete('/api/v1/strip/<strip_name>')
def strip_single_delete():
    pass
