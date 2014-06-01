
"""
*********************************************************************
updateHTML.py
*********************************************************************

Usage:
    updateHTML.py

    This script will re-generate all the static HTML pages

Author: Katherine Huang
Contact: khhuang@broadinstitute.org
-----------------------------------------------------------------------------------------
TODO:

"""
__author__ = "Katherine Huang"

import sys, os
from xml.dom.minidom import parseString

# import In-house modules
#import utils

#import bioUtils
# BioPython v1.55
#sys.path.append("/home/radon00/khhuang/python/lib/lib64/python") #this is where BioPython 1.55 is
#from Bio import SeqIO

# Global variables
HOME_DIR = "/afs/athena.mit.edu/org/a/almlab/web_scripts"
WORK_DIR = HOME_DIR
XML_DIR = "%s/xml" %(WORK_DIR)
HTML_TEMPLATE_FILE = "%s/templates/almSite.template.html" %(WORK_DIR)
HTML_TEMPLATE = open(HTML_TEMPLATE_FILE, 'r').read()

def makeHTML(fn):
    # replace the keywords in the HTML template with the xml content
    # HTML keywords are: _rightPane_, _contentPane_, _footer_ (case sensitive)
    xml_txt = open("%s/%s" %(XML_DIR, fn), 'r').read()
    html_txt = HTML_TEMPLATE
    print "reading %s" %(fn)
    xdom = parseString(xml_txt) # now the file has turned into an xdom object
    for xmlTag in ('Title', 'contentPane', 'rightPane', 'midPane', 'footer'):
        openTag = "<%s>" %xmlTag
        closeTag = "</%s>" %xmlTag
        try:
            paneDom = xdom.getElementsByTagName(xmlTag)[0].toxml().replace(openTag, "").replace(closeTag, "") # itself an xdom object
            #print paneDom
            html_txt = html_txt.replace("_%s_" %(xmlTag), paneDom)
            html_txt = html_txt.encode('ascii', 'ignore')
        except:
            pass
    # generate the HTML file
    html_fn = fn.replace("xml", "html")

    # highlight the page on the menu bar:
    html_txt = html_txt.replace('class="menu" href="%s"' %(html_fn), 'class="current" href="%s"' %(html_fn))

    htmlF=open('%s/%s' %(WORK_DIR, html_fn),'w')
    htmlF.write(html_txt)
    print "  %s generated" %(html_fn)
    return

def main(argv):
    if len(argv) < 1:
        utils.usage(__doc__)

        #how to put the process to sleep:
        #sleep(1) # this will sleep for 1 sec
    # file list
    xmlList=os.listdir(XML_DIR)

    for fname in xmlList:
        makeHTML(fname)

    # debugging
    #pdb.set_trace()


if __name__== '__main__':
    main(sys.argv)
