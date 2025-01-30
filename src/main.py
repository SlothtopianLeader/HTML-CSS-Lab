import cherrypy
import mako.template
import mako.lookup
import os.path
import random
import names
import dates
import views

#we have modules for each page we're displaying 
import page_signup
import page_test

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)]
)

class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(names.names)
        t = lookup.get_template("page_index.html")
        return t.render(name=n)
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        d = random.choice(dates.dates)
        v = random.choice(views.views)
        o = lookup.get_template("page_posts.html")
        return o.render(date=d, view=v)
    @cherrypy.expose
    def test(self):
        return page_test.get()
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
