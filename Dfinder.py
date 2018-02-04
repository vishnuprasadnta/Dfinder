import urllib2,os
class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
rudcol = colors()
while True:

    print ("""
                 ____   __ _           _           
                |  _ \ / _(_)_ __   __| | ___ _ __ 
                | | | | |_| | '_ \ / _` |/ _ \ '__|
                | |_| |  _| | | | | (_| |  __/ |   
                |____/|_| |_|_| |_|\__,_|\___|_| 
                                  #Author: vishnuraj kv 
 
""")
    dir = list(open("dir.txt","r"))
    print (rudcol.yellow +" -  eg  [http://www.site.com] or [https://www.site.com] " + rudcol.end)
    site = raw_input("  domain : ")

    
    if "http://" not in site:
        if "https://" in site:
            site = site.replace("https://","http://")
        else:
            site = "http://"+site
            
    if not site.endswith("/"):
        site = site+"/"
    print("\n")

    xsite = []
    for i in dir:
        try:
            open_site = urllib2.urlopen(site+i)
            if open_site:
                print " *** yeah found it *** : "+site+i 
                xsite.append(site+i)
        except:
            print " [:(] Nopzz : "+i

    print rudcol.bold + rudcol.red + "[*] may be vulnerable test further!!!!" + rudcol.end
    for found in xsite:
        print (found)

    
    print (rudcol.green +" Hi thanks for using my tool  #Author: vishnuraj kv  for more details ping me fb.com/vishnu0002  " + rudcol.end)

# End

