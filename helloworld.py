import myClass

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


#class is now external



class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        x = myClass.myClass()
        self.response.out.write("i got as param -mode-:"+self.request.get("mode")+"<br>\n")
        self.response.out.write("<img src=\"/images/logor.png\"><br>")
        if (self.request.get("mode") == "hello"):
            self.response.out.write("hallo a<br>")
        else:
            #self.response.out.write("vd_: "+str( x.grabmyurl("http://www.vondir.de") )+" seconds to load file<br>\n")
            #self.response.out.write("fb_: "+str( x.grabmyurl("http://www.farmbeds.com") )+" seconds to load file<br>\n")
            #self.response.out.write("fb2: "+str( x.grabmyurl("http://www.farmbeds.com/test.wsgi") )+" seconds to load file<br>\n")
            #self.response.out.write("fbxpy: "+str( x.grabmyurl("http://www.farmbeds.com/xml.wsgi") )+" seconds to load file<br>\n")
            #self.response.out.write("fbxph: "+str( x.grabmyurl("http://www.farmbeds.com/test.php") )+" seconds to load file<br>\n")
            #self.response.out.write("vdpl: "+str( x.grabmyurl("http://www.vondir.de/flash/flash_gallery/help.pl?catid=31") )+" seconds to load file<br>\n")
            #self.response.out.write("gaei: "+str( x.grabmyurl("http://avengo2.appspot.com/images/logor.png") )+" seconds to load file<br>\n")
            self.response.out.write("gaea: o:"+x.dbreadmyurl("http://avengo2.appspot.com/?mode=hello")+" - n:"+str( x.grabmyurl("http://avengo2.appspot.com/?mode=hello") )+" seconds to load file<br>\n")
            




application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
