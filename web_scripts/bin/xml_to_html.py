#!/usr/bin/env python

"""
This script will re-generate a static HTML page

Author: Katherine Huang, Scott Olesen
"""

import sys, os, argparse, re
from xml.dom.minidom import parseString

def xml_to_html(xml_txt, template_txt, html_fn):
    '''
    xml and template to new html
    
    parameters
    xml_txt : str
      text of the xml file
    template_txt : str
      text of the template html
    html_fn : str
      filename to look for when doing "current" menu

    returns : str
      html content
    '''

    # replace the keywords in the HTML template with the xml content
    # HTML keywords are: _rightPane_, _contentPane_, _footer_ (case sensitive)
    html_txt = template_txt
    xdom = parseString(xml_txt) # convert xml to xdom object
    for xmlTag in ('Title', 'contentPane', 'rightPane', 'midPane', 'footer'):
        openTag = "<%s>" %xmlTag
        closeTag = "</%s>" %xmlTag
        try:
            paneDom = xdom.getElementsByTagName(xmlTag)[0].toxml().replace(openTag, "").replace(closeTag, "") # itself an xdom object
            html_txt = html_txt.replace("_%s_" %(xmlTag), paneDom)
            #html_txt = html_txt.encode('ascii', 'ignore')
        except:
            pass

    html_txt = html_txt.replace('class="menu" href="{}"'.format(html_fn), 'class="current" href="{}"'.format(html_fn))
    return html_txt

if __name__== '__main__':
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('xml', type=argparse.FileType('r'), help='xml filename')
    p.add_argument('output', help='output html')
    p.add_argument('-t', '--template', type=argparse.FileType('r'), help='html template filename', default='template.html')
    args = p.parse_args()

    xml_content = args.xml.read()
    template_content = args.template.read()
    html_content = xml_to_html(xml_content, template_content, args.output)

    # write the html content out
    with open(args.output, 'w') as f:
        f.write(html_content)
