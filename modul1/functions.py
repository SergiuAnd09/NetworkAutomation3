print('hey', 'sdkf', 'skdfj', 'hai la python', sep=' ', end='\n')

#data type string

string1 = 'Hello Python'
string2 = u"Hello Python\n"
#u in fata sau nimic e acelasi lucru, acela semnificand ca ia stringul ca unicode
print(string2)
string3 = '''Hello 
            Python'''
string4 = """Hello 
            Python"""
print(string4)
string5 = r"Hello Python\n"
#practic raw string nu mai are nevoie de nici un escape la cacractere speciale gen newline
print(string5)
string6 = f"Hello Python6\n{string1}"
#f permite folosirea variabilelor in cadrul stringului, f e cel mai rapid tip de formatare, si al usurintei prin care putem citi un text si
#intelege ce e acolo, si majoritatea e de acord ca asta e cea mai buna varianta, si o sa si folosim destul de des
print(string6)

#pe scurt cu comentariile

# def x():
#     x = 3
#     """
#     comment
#     :return:
#     """

#deci daca e primul string din definirea unei functii sau al unui modul, atunci e docstring, altfel nu, deci ghilimelele triple n-au legatura
#daca ceva e sau nu docstring