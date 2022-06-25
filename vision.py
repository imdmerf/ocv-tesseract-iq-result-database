import cv2
import pytesseract
import os, os.path
from database import Database
import nltk
import pymorphy2

db = Database('persons.db')
DIR = "./images"
config = r'--oem 3 --psm 7'
coonfig_for_names = r'--oem 3 --psm 13'
prob_thresh = 0.9
morph = pymorphy2.MorphAnalyzer()
nltk.download('punkt')



def get_iq_name():
    count = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    for i in range(1, count + 1):  
        full_path = DIR + "/img" + str(i)
        img = cv2.imread(full_path)
        cropped = img[5:19, 51:224]
        cropped2 = img[28:48, 8:45]
        img = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(cropped2, cv2.COLOR_BGR2RGB)
        iq_value = pytesseract.image_to_string(img2, config=config, lang ='rus')
        iq_name = pytesseract.image_to_string(img, config=coonfig_for_names, lang ='rus').split()
        for word in nltk.word_tokenize(iq_name[0]):
            for p in morph.parse(word):
                if 'Name' in p.tag and p.score >= prob_thresh:
                    db.add_person(word.capitalize(), iq_value)
                    db.database_verify()