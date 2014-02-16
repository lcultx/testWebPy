#-*- coding:utf-8 -*
__author__ = 'blacksun'


import web
import re
import base64
from config import setting

render = setting.render

class Index:
    ''' 主页   '''
    def GET(self):
        """ show page       """
        if web.ctx.env.get("HTTP_AUTHORIZATION") is None:
            raise web.seeother('login')
        return render.index("Hello World!")
    def POST(self):
        pass

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic','',auth)
            username,password = base64.decodestring(auth).split(':')
            if(username,password) in setting.allowed:
                raise  web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return
