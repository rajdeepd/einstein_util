review_path= '/Users/rdua/Downloads/sorted_data/automotive/positive.review'

import xml.etree.ElementTree as ET

file =  file =open('./amz_automobile_reviews_unlabeled.csv','w')

def parse(path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser=parser)
    root = tree.getroot()


    for child in root:

        review_text = child.find('review_text').text.strip()
        review_text = review_text.replace(',','').replace('\n','').lower().encode('ascii', 'ignore').replace('"','')
        file.write(review_text + '\n')

def clean():
    file.close()
def main():
    parse(review_path)
    clean()

if __name__ == '__main__':
    main()