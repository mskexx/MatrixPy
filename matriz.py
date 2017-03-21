#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def printmat():
    list1 = []
    box = 15
    for r in xrange(0,box):
        list1.append(1)

    #Linea Arriba
    sys.stdout.write("╔═")
    for i in xrange(0,box-1):
        sys.stdout.write("══╦═")
    sys.stdout.write("══╗")

    #Cuerpo
    print("")
    for w in xrange(0,box-1):
        for j in xrange(0,box):
            sys.stdout.write("║ " + str(list1[j])+ " ")
        sys.stdout.write("║")
        print("")
        sys.stdout.write("╠═")
        for i in xrange(0,box-1):
            sys.stdout.write("══╬═")
        sys.stdout.write("══╣")
        print("")

    for j in xrange(0,len(list1)):
        sys.stdout.write("║ " + str(list1[j]) + " ")
    sys.stdout.write("║")

    print("")
    sys.stdout.write("╚═")
    for i in xrange(0,box-1):
        sys.stdout.write("══╩═")
    print("══╝")


if __name__ == '__main__' :
	printmat()
