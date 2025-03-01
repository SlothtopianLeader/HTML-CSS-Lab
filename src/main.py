import cherrypy
import mako.template
import mako.lookup
import os.path
import random
import names
import datetime
import views
import PIL.Image
import io

#we have modules for each page we're displaying 
import page_signup
import page_test

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)]
)

def get_random_time():
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = x.seconds // 3600
    minutesago = (x.seconds-hoursago * 3600) // 60
    return f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago"

BASEDIR=os.path.abspath( os.path.dirname(__file__) )

class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(names.names)
        t = lookup.get_template("page_index.html")
        return t.render(name=n)
    @cherrypy.expose
    def signup(self):
        t = lookup.get_template("page_signup.html")
        return t.render()
    @cherrypy.expose
    def posts(self):
        v = random.choice(views.views)
        timestamps = [get_random_time() for _ in range(10)]
        o = lookup.get_template("page_posts.html")
        return o.render(timestamps=timestamps, view=v)
    @cherrypy.expose
    def makepost(self):
        with open(f"{BASEDIR}/../src/page_makepost.html") as fp:
            return fp.read()
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def do_update(self, title, pic):
        print("name is:",title)
        print("pic is:",pic)
        tmp = pic.file.read()
        #just print first 10 bytes
        print("pic is:",tmp[:10])
        return {"ok": True }
    @cherrypy.expose
    def mostrecent(self, image_path):
        full_path = os.path.join(BASEDIR, image_path)

        if not os.path.isfile(full_path):
            cherrypy.response.status = 404
            return "Image not found"

        with open(full_path, "rb") as f:
            data = f.read()
            
        cherrypy.response.headers["Content-Type"] = "image/jpeg"
        return data
    @cherrypy.expose
    def test(self):
        return page_test.get()
    def checkImage( data ):
        try:
            MAXSIZE=4096
            tmp = io.BytesIO(data)
            with PIL.Image.open(tmp, formats=["JPEG","PNG"]) as img:
                if img.width > MAXSIZE or img.height > MAXSIZE:
                    return False
            return True
        except PIL.UnidentifiedImageError:
            return False
        except PIL.DecompressionBombError:
            return False
        
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