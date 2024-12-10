from collections import defaultdict, OrderedDict
import json
from pathlib import Path
import re 
class BagOfWords: 
    def __init__(self,s = ''):
        self._text = ''
        self._bag = defaultdict(int)
        if isinstance(s, str) :
            self._text = s
        elif type(s).__name__ == 'TextIOWrapper':
            self._text = s.read()
        words = self._text.split()
        pattern = r'^[a-zA-z]+$'
        for w in words: 
            tmpW = w
            tmpW = self.trimStart(tmpW)
            tmpW = self.trimEnd(tmpW)
            tmpW = self.trimS(tmpW)
            if re.search(pattern, tmpW):
                self._bag[tmpW.lower()] += 1

    def saveToJson(self,*, path,fileName): 
        #sys path join do poprawy albo os 
        fullPath = path + '\\' + fileName + ".json"  
        with open(fullPath, 'w') as file: 
            json.dump(self._bag, file)

    def loadFromJson(self, path): 
        with open(path, 'r') as file: 
            self._bag = json.load(file)


    def trimStart(self, word):
        while not re.search(r'^[a-zA-Z]', word) and len(word) > 0:
            word = word[1:]
        return word

    def trimEnd(self, word):
        
        while not re.search(r'[a-zA-Z]$', word) and len(word) > 0:
            word = word[:len(word) - 1]
        return word
    def trimS(self, word): 
        if re.match(r"^.*'s$", word):
            word = word[ :len(word) - 2]
        return word
    def __repr__(self):
        b = json.dumps( self._bag)
        return str(b)[1:len(b) - 1]

    def __contains__(self, key): 
         return key in self._bag

    def __iter__(self):
        # myKeys = list(self._bag.values())
        # myKeys.sort(reverse=True)
        # return iter(myKeys)
        sorted_items = sorted(self._bag.items(), key=lambda item: item[1], reverse=True)
        return iter(sorted_items)

    def myItems(self): 
        return self._bag.items()
    
    def getText(self):
        return self._text

    def __add__(self, bof2): 
        res = BagOfWords(self._text + ' ' + bof2.getText())
        return res 
    def __getitem__(self, arg): 
        return self._bag[arg]
    def __setitem__(self, key, arg): 
        self._bag[key] = arg




def test1():
    bow = BagOfWords('ala ma kota ala ma ala')
    bow2 = BagOfWords('tomek tez ma kota')
    bow3 = bow + bow2
    #print(bow)
    # print( f'ala in BagOfWords: {'ala' in bow}')
    # for b in bow: 
    #     print(b)
    # print(bow3)
    # print(bow['ala'])
    # print(bow3['ala'])
    # bow3['tomek'] = 10
    # for w in bow3: 
    #     print(w)

def test2(): 
    bow = BagOfWords(open(r'C:\studia\Magisterka\EfektywneProgramowanieWJezykuPython\effective_python\lab07\hamlet.txt', encoding='utf8'))
    print(bow['hamlet'])
    i = 0
    for val in bow:
        print(val)
        if i == 10: 
            break
        i += 1

def zad05(): 
    bow = BagOfWords(open(r'C:\studia\Magisterka\EfektywneProgramowanieWJezykuPython\effective_python\lab07\lab07Files\hamlet.txt', encoding='utf8'))
    bow.saveToJson(path=r'C:\studia\Magisterka\EfektywneProgramowanieWJezykuPython\effective_python\lab07\lab07Files', fileName='hamletDict')

def zad05_2():
    bow = BagOfWords('')
    bow.loadFromJson(r'C:\studia\Magisterka\EfektywneProgramowanieWJezykuPython\effective_python\lab07\lab07Files\hamletDict.json')
    print(bow)

zad05_2()


