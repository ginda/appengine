import shutil
import os
import datetime
import math
import time

import myClass

from array import array


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):

    def get(self):
       self.response.headers['Content-Type'] = 'text/plain'
       x = myClass.myClass()
       self.response.out.write("vd_: "+str( x.grabmyurl("http://www.vondir.de") )+" seconds to load file\n")
       self.response.out.write("fb_: "+str( x.grabmyurl("http://www.farmbeds.com") )+" seconds to load file\n")
       self.response.out.write("fb2: "+str( x.grabmyurl("http://www.farmbeds.com/test.wsgi") )+" seconds to load file\n")




application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
