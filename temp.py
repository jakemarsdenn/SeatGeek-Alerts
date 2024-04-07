__all__ = ['temp']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['getEvents', 'test', 'CLIENT_ID'])
@Js
def PyJsHoisted_getEvents_(performer, this, arguments, var=var):
    var = Scope({'performer':performer, 'this':this, 'arguments':arguments}, var)
    var.registers(['axios', 'performer', 'url'])
    var.put('axios', var.get('require')(Js('axios')))
    var.put('url', (((Js('https://api.seatgeek.com/2/events?performers.slug=')+var.get('performer'))+Js('&client_id='))+var.get('CLIENT_ID')))
    @Js
    def PyJs_anonymous_0_(error, this, arguments, var=var):
        var = Scope({'error':error, 'this':this, 'arguments':arguments}, var)
        var.registers(['error'])
        var.get('console').callprop('error', var.get('error'))
        return Js('[]')
    PyJs_anonymous_0_._set_name('anonymous')
    @Js
    def PyJs_anonymous_1_(response, this, arguments, var=var):
        var = Scope({'response':response, 'this':this, 'arguments':arguments}, var)
        var.registers(['eventData', 'response', 'eventsWithIds'])
        var.put('eventData', var.get('response').get('data'))
        @Js
        def PyJs_anonymous_2_(event, this, arguments, var=var):
            var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
            var.registers(['event'])
            return Js({'id':var.get('event').get('id'),'title':var.get('event').get('title'),'datetime_utc':var.get('event').get('datetime_utc')})
        PyJs_anonymous_2_._set_name('anonymous')
        var.put('eventsWithIds', var.get('eventData').get('events').callprop('map', PyJs_anonymous_2_))
        var.get('console').callprop('log', var.get('eventsWithIds'))
        return var.get('JSON').callprop('stringify', var.get('eventsWithIds'))
    PyJs_anonymous_1_._set_name('anonymous')
    return var.get('axios').callprop('get', var.get('url')).callprop('then', PyJs_anonymous_1_).callprop('catch', PyJs_anonymous_0_)
PyJsHoisted_getEvents_.func_name = 'getEvents'
var.put('getEvents', PyJsHoisted_getEvents_)
@Js
def PyJsHoisted_test_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('console').callprop('log', Js('hello'))
PyJsHoisted_test_.func_name = 'test'
var.put('test', PyJsHoisted_test_)
var.get('require')(Js('dotenv')).callprop('config')
var.put('CLIENT_ID', var.get('process').get('env').get('CLIENT_ID'))
pass
var.get('getEvents')(Js('drake'))
pass
pass


# Add lib to the module scope
temp = var.to_python()