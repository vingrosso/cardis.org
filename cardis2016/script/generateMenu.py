#! /usr/bin/env python2

import sys
import os
import json

def usage ():
    print >> sys.stderr, "Usage: %s 0 <sitelayout> <curSection>" % sys.argv[0]
    print >> sys.stderr, "    Generate navbar for section <curSection>"
    print >> sys.stderr, "Usage: %s 1 <sitelayout> <curSection> [curSubSection]" % sys.argv[0]
    print >> sys.stderr, "    Generate subsection menu for section <curSection> and subsection <curSubSection>"
    print >> sys.stderr, "Usage: %s 2 <sitelayout>" % sys.argv[0]
    print >> sys.stderr, "    Generate site map"
    sys.exit (0)

def constructMenu (sitelayout):
    with open(sitelayout, "r") as f:
        return json.loads (f.read ())

#    f = open (os.path.join (directory, section) + ".name", "r")
#    result = {"name": f.read ()[:-1], "content": {}}
#    f.close ()
#    (_, _, filenames) = os.walk(os.path.join (directory, section)).next()
#    for n in filenames:
#        if n.endswith (".page"):
#            f = open (os.path.join (directory, section, n[:-4]) + "name", "r")
#            result["content"][n[:-5]] = {"name": f.read ()[:-1]}
#            f.close ()
#    return result
# 
# def constructMenu (directory):
#     (_, _, filenames) = os.walk(directory).next()
#     return {f[:-5]: constructSubMenu (directory, f[:-5]) for f in filenames if f.endswith (".page")}

def isSubsec (dic, name):
    if ("page" not in dic.keys () or name != dic["page"]) and "content" in dic.keys ():
        for subdic in dic["content"]:
            if subdic["page"] == name:
                return True
    return False

def printNavBar (menu, args):
    print "                                    <ul class=\"nav navbar-nav\">"
    for dic in menu:
        if "page" in dic.keys () and dic["page"] == "index.html":
            continue
        sys.stdout.write ("                                        <li")
        isSubsection = ("page" in dic.keys () and dic["page"] == args[0]) or isSubsec (dic, args[0])
        if isSubsection:
            sys.stdout.write (" class=\"active\"")
        if "page" in dic.keys ():
            sys.stdout.write ("><a href=\"./%s.html\">%s" % (dic["page"], dic["name"]))
        else:
            sys.stdout.write ("><a href=\"./%s.html\">%s" % (dic["content"][0]["page"], dic["name"]))
        if isSubsection:
            sys.stdout.write ("<span class=\"sr-only\">(current)</span>")
        print "</a></li>"
    print "                                    </ul>"

def printSubMenu (menu, args):
    print "                            <table class=\"submenu\">"
    for dic in menu:
        sys.stdout.write ("                                <tr><td")
        isSubsection = isSubsec (dic, args[0])
        if "page" in dic.keys ():
            section = dic["page"]
        else:
            section = dic["content"][0]["page"]

        if "page" in dic.keys () and dic["page"] == args[0]:
            sys.stdout.write (" class=\"active\"")
        sys.stdout.write ("><a href=\"./%s.html#main-content\"><div style=\"width:100%%;height:100%%;\">" % section)
        if isSubsection:
            sys.stdout.write ("<strong>%s</strong>" % dic['name'])
        else:
            sys.stdout.write (dic['name'])
        print "</div></a></td></tr>"

        if isSubsection:
            for subdic in dic["content"]:
                sys.stdout.write ("                                <tr><td class=\"subsection")
                if args[0] == subdic["page"]:
                    sys.stdout.write (" active")
                print "\"><a href=\"./%s.html#main-content\"><div style=\"width:100%%;height:100%%;\">%s</div></a></td></tr>" % (subdic["page"], subdic['name'])
    print "                            </table>"

def printSiteMap (menu, args):
    print "                    <ul class=\"list-inline\">"
    for dic in menu:
        print "                        <li>"
        if "page" in dic.keys ():
            print "                            <a href=\"./%s.html\">%s</a>" % (dic['page'], dic['name'])
        else:
            print "                            %s" % dic['name']
        if 'content' in dic.keys ():
            print "                            <ul class=\"list-unstyled\">"
            for subdic in dic['content']:
                print "                                <li><a href=\"./%s.html\">%s</a></li>" % (subdic['page'], subdic['name'])
            print "                            </ul>"
        print "                        </li>"
    print "                    </ul>"


if len(sys.argv) < 3:
    usage ()

mode = int(sys.argv[1])
if mode > 2 or ((mode == 0 or mode == 1) and len(sys.argv) < 4):
    usage ()

[printNavBar, printSubMenu, printSiteMap][mode] (constructMenu (sys.argv[2]), sys.argv[3:])
