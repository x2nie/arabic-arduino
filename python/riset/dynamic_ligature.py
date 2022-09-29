import re
breakers = ['ا', 'ر', 'د', 'و', 'ذ', '\\s']
BREAKERS = "[%s]+" % "".join(breakers)
# BREAKERS = "(%s)" % "|".join(map(re.escape, breakers))

lig1 = ''.join( [' ', 'ا',  'ي', 'ا' ],)
lig2 = ''.join( [' ', 'ن', 'ا', ],)
kamus = {
    lig1: 'IY',
    lig2: 'NA'
}
print(kamus)

txt1 = 'اِيَّاكَ نَعْبُدُ وَاِيَّاكَ نَسْتَعِيْنُ'
txt1 = 'اياك نعبد واياك نستعين'


def multiple_replace(adict:dict, text:str): 

    """ Replace in 'text' all occurences of any key in the given
    dictionary by its corresponding value.  Returns the new tring.""" 
    # newDict = {k.replace(' ', BREAKERS) :v for k,v in adict.items()}
    newDict = {}
    for k,v in adict.items():
        if k.startswith(' ') and k[1] in BREAKERS:
            k = k.replace(' ', BREAKERS.replace(k[1],''))
            newDict[k] = v
        else:
            k = k.replace(' ', BREAKERS)
            newDict[k] = v
    print('newdict:', newDict)

    # Create a regular expression  from the dictionary keys
    # pattern = "(%s)" % "|".join(map(re.escape, newDict.keys()))
    # pattern = "(%s)" % "|".join(["(%s)" % k for k in newDict.keys()])
    pattern = "|".join(["(%s)" % k for k in newDict.keys()])
    print('pattern:', pattern)
    regex = re.compile(pattern)

    # For each match, look-up corresponding value in dictionary
    # return regex.sub(lambda mo: newDict[mo.string[mo.start():mo.end()]], text) 

    def art(found):
        print('found:',found)
        return '--new--'
    return regex.sub(art, text) 


print(multiple_replace(kamus, txt1))