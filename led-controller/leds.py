from bottle import (
    Bottle,
    post,
    get,
    put,
    delete,
    run,
    hook
)

ledAPI = Bottle()

@ledAPI.get('/api/v1/led')
def led_collection():
    return "Test"

@ledAPI.post('/api/v1/led')
def led_creation():
    pass

@ledAPI.get('/api/v1/led/<led_id>')
def led_single_get(led_id):
    pass

@ledAPI.put('/api/v1/led/<led_id>>')
def led_single_put():
    pass

@ledAPI.delete('/api/v1/led/<led_id>')
def led_single_delete():
    pass


