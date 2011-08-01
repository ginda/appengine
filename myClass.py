
import urllib2
import time

class myClass:
    @staticmethod
    def grabmyurl(url):
        loadtime=0;
        t0 = time.time()
        content = [];
        try:
            filehandle = urllib2.urlopen( url )
            for lines in filehandle.readlines():
                content.append(lines)

            filehandle.close()
        except urllib2.URLError, e:
            handleError(e)
        loadtime = time.time() - t0;
        return loadtime 

