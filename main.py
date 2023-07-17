import sys
import os
import unittest
import sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__) + '/src')))
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__) + '/tests')))

fire core import main

if__name__ =='__main__':
f=open('packages/tcp.txt','r')
g=open('packages/udp.txt','r')

main(f)

                
