__author__ = 'blacksun'

import web

db = web.database(dbn='mysql',db='www',user='root',pw='root')

render = web.template.render('templates',cache=False)

web.config.debug = True

config = web.storage(
    email='aaa.com',
    site_name = 'V1.0',
    site_desc = '',
    static= '/static'
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render

allowed = (
    ('test','test'),
)