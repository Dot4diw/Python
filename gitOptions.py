#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Method one
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'The input file is ：', inputfile
   print 'The output file is ：', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])

# OR
    #encoding=utf-8
     
    import getopt
    import sys
     
    def main(argv):
        try:
            options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
        except getopt.GetoptError:
            sys.exit()
     
        for option, value in options:
            if option in ("-h", "--help"):
                print("help")
            if option in ("-i", "--ip"):
                print("ip is: {0}".format(value))
            if option in ("-p", "--port"):
                print("port is: {0}".format(value))
     
        print("error args: {0}".format(args))
     
    if __name__ == '__main__':
        main(sys.argv[1:])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


## Method two
# Use the optparse package to parsing the parameters.
# It can auto generate the usage information about the script!

import optparse
usage="python %prog -u/--user <target user> -p/--password <target password>"
parser=optparse.OptionParser(usage) 
parser.add_option('-u', '--user',dest='User',type='string',help='target user', default='root')
parser.add_option('-p','--password',dest='Pwd',type='string',help='target password')
options, args=parser.parse_args()
print('options为', options)
print("username:", options.User)
print("passwd: ", options.Pwd)
print('args: ', args)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Method three
# Use the argparse package to parsing the arguments.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', dest='User', type=str,default='root', help='target User')
parser.add_argument('-s', '--sex', dest='Sex', type=str, choices=['male', 'female'], default='male', help='target Sex')
parser.add_argument('-n', '--number', dest='Num', nargs=2, required=True,type=int, help='target Two Numbers')
print(parser.parse_args()) 

# OR 
import argparse
parser = argparse.ArgumentParser(description="progrom description")
parser.add_argument('key', help="Redis key where items are stored")
parser.add_argument('--host')
arser.add_argument('--port')
parser.add_argument('--timeout', type=int, default=5)
parser.add_argument('--limit', type=int, default=0)
parser.add_argument('--progress_every', type=int, default=100)
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

key = args.key
host = args.host
port = args.port
timeout = args.timeout
limit = args.limit
progress-every = args.progress_every
verbose = args.verbose


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Method four
from optparse import OptionParser  
  
parser = OptionParser(usage="usage:%prog [options] arg1 arg2")  
parser.add_option("-t", "--timeout",  
                action = "store",  
                type = 'int',  
                dest = "timeout",  
                default = None,  
                help="Specify annalysis execution time limit"  
                )  
parser.add_option("-u", "--url",  
                action = "store_true",  
                dest = "url",  
                default = False,  
                help = "Specify if the target is an URL"  
                )
(options, args) = parser.parse_args() 
if options.url:  
    print(args[0]) 
    
# OR
parser = optparse.OptionParser(version="%prog " + config.version)
# common_group
common_group = optparse.OptionGroup(
    parser, "Common Options",
    "Common options for code-coverage.")
parser.add_option_group(common_group)
common_group.add_option(
    "-l", "--lang", dest="lang", type="string", default="cpp",
    help="module language.", metavar="STRING")
common_group.add_option(
    "--module_id", dest="module_id", type="int", default=None,
    help="module id.", metavar="INT")
cpp_group = optparse.OptionGroup(
    parser, "C/C++ Options",
    "Special options for C/C++.")
# cpp_group
parser.add_option_group(cpp_group)
cpp_group.add_option(
    "--local-compile", action="store_true", dest="local_compile",
    help="compile locally, do not use compile cluster.")
cpp_group.add_option(
    "--module_path", dest="module_path", type="string", default=None,
    help="module path, like app/ecom/nova/se/se-as.", metavar="STRING")
    
options, arguments = parser.parse_args()
lang = options.lang
module_id = options.module_id
local_compile = options.local_compile
module_path = options.local_compile

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Method five
# Use the click package

import click

@click.command()
@click.option('--center', nargs=2, type=float, help='center of the circle')
@click.option('--radius', type=float, help='radius of the circle')
def circle(center, radius):
    click.echo('center: %s, radius: %s' % (center, radius))

if __name__ == '__main__':
    circle()

# Run result:
$ python click_multi_values.py --center 3 4 --radius 10
center: (3.0, 4.0), radius: 10.0

$ python click_multi_values.py --center 3 4 5 --radius 10
Usage: click_multi_values.py [OPTIONS]

Error: Got unexpected extra argument (5)


# OR
import click

@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')

if __name__ == '__main__':
    hello()
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Method six
# Use the fire package
import fire

def hello(name="World"):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  fire.Fire(hello)
  

