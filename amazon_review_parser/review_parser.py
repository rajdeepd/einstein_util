negative_review_path= '/Users/rdua/Downloads/sorted_data/automotive/negative.review'
postive_review_path= '/Users/rdua/Downloads/sorted_data/automotive/positive.review'

import xml.etree.ElementTree as ET

file =  file =open('./amz_automobile_reviews.csv','w')

def init():
    pass

def parse(path, sentiment):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser=parser)
    root = tree.getroot()


    for child in root:

        review_text = child.find('review_text').text.strip()
        review_text = review_text.replace(',','').replace('\n','').lower().encode('ascii', 'ignore').replace('"','')
        file.write(review_text + ', ' + sentiment + '\n')

def clean():
    file.close()

def main():
    init()
    parse(negative_review_path, 'negative')
    parse(postive_review_path, 'positive')
    clean()

if __name__ == '__main__':
    main()