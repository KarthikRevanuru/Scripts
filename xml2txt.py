import xml.etree.ElementTree as ET
import glob, os

current_dir = os.path.dirname(os.path.abspath(__file__))

for pathAndFilename in glob.iglob(os.path.join(current_dir+"/Labelled_Data_XML/", "*.xml")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    tree = ET.parse('Labelled_Data_XML/'+title+'.xml')
    root = tree.getroot()
    file = open('Labelled_Data_TXT/'+title+'.txt', 'w')
    num=len(root)
    for i in range(6,num):
        file.write('{}\n'.format(int(root[5].text ) + 1))
        file.write('{},{},{},{}\n'.format(int(root[i][4][0].text),int(root[i][4][1].text),int(root[i][4][2].text),int(root[i][4][3].text)))
