#everything in python is an object or keyword

print(print)
#print e un obiect, si va fi tratat ca orice alt obiect, cu actiuni executabile si proprietati accesibile
#in python obiectele suporta dot notation, prin dot luand atribute(metode, proprietati)

# print(print.__name__)

'Hello Python {}'.format('from afar')
#are metode acest string, printe care avem metoda format

#toate keywords apar cu o culoare galbena
pass
#sunt si situatii cand un keyword e si obiect

#True si False sunt si obiect si keywords, referind chiar obiectele boolene, cu atributele lor

#True.

#in python 0 si 1 sunt interschimbabile cu True si False in multe situatii
#si numerele mostenesc object, au atribute

#atingem tipuri de date
#in python definim si numere, definim fara ghilimele

#types
var1 = 1
var2 = '1'

print(type(var1), type(var2))

# methods
print(var1.bit_length())
#print(1.bit_length())

#1.method() nu merge pentru ca se asteapta la zecimal

print((-3).bit_length())
#si la negative la fel vine facut

#python considera lungimea fiind doar bitii necesari stocarii valorii



#operations

print(1 + 2)
print((1).__add__(2))
print("1" + "2")
print("1".__add__("2"))

#in pyton fiecare obiect are definit ce face fiecare operator pentru el, si atunci vedem in __add__ ce face plus
#uneori se mai fac si chekuri(adunar cu float, complex, impartire cu 0) etc.

print(3 ** 2 ** 3)
print((3).__pow__(2))

print(3 // 2)
print(3 / 2)
print(3 % 6)

print(type(10/3))
print(type(3 % 2))

print(3 * '34')#singurul tip de operatie suportat pe python intre un int si un string, altfel primim typeerror

#in python acele operatii nu sunt stricte, ci sunt ce au definite a fi cel mai intuitiv rezultat

#de evitat impartirea, ca e pagubasa, caci nu imparte cum trebuie, si sa incercam sa folosim inmultiri, adunari etc.

print(True * 2)
#merge cu True, ca bool mosteneste obiect de tip int, cu niste atribute in plus

#pentru data viitoare, o observatie interesanta

print(True and False)
print("a" and "b")#operatia ia doar valoarea lor de adevar care e interschimbabila cu obiectul si aplica urmatoarea logica:
#daca a e adevarat, atunci valoarea lui b dicteaza daca e adevarat sau fals rezultatul, si e suficient sa returneze a doua valoare, si aia e egala
#cu rezultatul meu, si la fel e si pentru 'or', si prin urmare rezultatul este 'b'

print("" and 'b')#aici returneaza nimic, ca il vede din start ca in and da rau

#and nu e operatia and booleana care o stim, si e implementarea efectiva ce tine de limbaj