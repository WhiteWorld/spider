import urllib2,urlparse
import getopt,sys,string,os,re
def usage():
    print """
    Usage:
    -h,--help      display this help and exit
    -d,--deep      define the deep of the spider
    -u,--url       define the start url
    -n,--number    define the number of files downloaded
    -v,--version   output version information and exit
    """
def version():
    print "spider version 1.0\nWritten by liubai"
def realwork(url,deep):
    urllib2.urlopen("http://"+url).read()
    print "deep=",deep
def make_file():
    if (os.path.exists('getall')) == False:
        os.mkdir('getall')
def getURL(url):
    urls=[]
    try: 
        fp=urllib2.urlopen(url)
    except:
        print 'get url exception'
        return []
   # pattern = re.compile("http://*.shtml")
    pattern = re.compile(r'(http://[^///]+)', re.I)  
   
    while 1:
        s=fp.read()
        if not s:
            break
        urls=pattern.findall(s)
    fp.close()
    return urls
        
def downURL(url,filename):
    try: 
        fp=urllib2.urlopen(url)
    except:
        print 'download exception'
        return 0
    op=open('getall'+"/"+filename,"wb")
    while 1:
        s=fp.read()
        if not s:
            break
        op.write(s)
        print "downloaded!"
    fp.close()
    op.close()
    return 1

def BFS(starturl,deep,number):
    urls=[] 
    urlflag=[]
    urls.append(starturl)
    urlflag.append(starturl)
    i=0;
    while 1:
        if i > number:
            break;
        if len(urls)>0:
            url=urls.pop(0)
            print url,len(urls)
            downURL(url,str(i)+'.htm')
            i=i+1
            urllist=getURL(url)
            print 'goto loop....'
            for url in urllist:
              #   print url
                 if urlflag.count(url) == 0:
                    urls.append(url)
                    urlflag.append(url)
        else:
            break
                    

def main():
    try:
        opts,argv=getopt.getopt(sys.argv[1:],"hu:d:n:v",["help","url=","deep=","number=","version"])
    except getopt.GetoptError,err:
        print str(err)
        usage()
        sys.exit(2) 
    deep=1
    number=10
    url="http://sports.sina.com.cn"
    for o,a in opts:
        if o in ("-v"," --version"):
            version() 
            sys.exit()
        elif o in ("-h","--help"):
            usage()
            sys.exit() 
        elif o in ("-u","--url"):
            url=a
        elif o in ("-d","--deep"):
            deep=int(a)
        elif o in ("-n","--number"):
            number=int(a)
        else:
            assert False ,"unhandled option"
    print "url=%s,deep=%d,number=%d" %(url,deep,number)
    make_file()
    #downURL(url,'1.html')
    BFS(url,deep,number) 
if __name__ == "__main__":
    main()
