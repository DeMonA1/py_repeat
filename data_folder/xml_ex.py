import xml.etree.ElementTree as et
from defusedxml.ElementTree import parse


tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag
for child in root:
    print('tag: ', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
len(root)
len(root[0])

et = parse('xmlfile.xml')