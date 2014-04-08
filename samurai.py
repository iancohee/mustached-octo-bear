#!/usr/bin/python

"""
To install 'easy_install shodan' to install
the shodan libraries
"""
from shodan import WebAPI

#My key. Get your own :)
KEY = ""
api = WebAPI(KEY)
filename = 'ips.txt'

class ShodanScanner(object):

    def __init__(self, KEY):
        self.api = WebAPI(KEY)

    def searchShodan(self, search_string):
        try:
            self.results = self.api.search(search_string)
            for result in self.results['matches']:
                print result['ip'], str(result['latitude']), str(result['longitude'])
                fp = open(filename, 'w');
                fp.write(result['ip'])
                fp.close()
            for name in result['hostnames']:
                print name
                print result['data']
                print '***%s results with \"%s\"***' % (self.results['total'], search_string)
        except Exception, e:
            print 'Error: %s' % e

    def searchExploitDB(self, search_string):
        try:
            self.results = self.api.exploitdb.search(search_string)
            for result in self.results['matches']:
                print result['date']
                print result['platform']
                print result['type']
                print result['description']
                print '#######################################'
                print '***%s results with \"%s\"***' % (self.results['total'], search_string)
        except Exception, e:
            print 'Error: %s' % e

if __name__ == '__main__':
    if KEY == "":
        print "WARNING! Key is ''"
        exit(0)

    while(1):
        print '+----------------------+'
        print '|     Samurai Pie      |'
        print '|       v 0.0.1        |'
        print '|       solidus        |'
        print '+----------------------+'
        print '1. Shodan'
        print '2. Exploit DB'
        print '3. Google Wifi/Skyhook (unimplemented)'
        print '99. Quit\n'
        scanner = ShodanScanner(KEY)

        user_input = raw_input('[>] Enter a number: ')

        if int(user_input) == 1:
            user_string = raw_input('[>] Enter a search string: ')
            scanner.searchShodan(user_string)
        elif int(user_input) == 2:
            user_string = raw_input('[>] Enter a search string: ')
            scanner.searchExploitDB(user_string)
        elif int(user_input) == 3:
            print 'You can\'t read, pick another number!'
        elif int(user_input) == 99:
            print 'Goodbye, Samurai!'
            exit(0)
        else:
            print 'You can\'t read'
