# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext
from math import ceil, factorial

def pi(n):
    n += 2 #т.к. первый символ не считаются, мы же только после запятой указываем нужное кол-во, а последний мы срезаем, чтобы не было округлений
    getcontext().prec = n
    num_iterations = ceil(n / 14)
    constant_term = 426880 * Decimal(10005).sqrt()
    exponential_term = 1
    num = 13591409
    partial_sum = Decimal(num)
                
    for i in range(1, num_iterations):
        num1 = factorial(6 * i) // (factorial(3 * i) * factorial(i) ** 3)
        num = num + 545140134
        exponential_term = exponential_term * -262537412640768000
        partial_sum += (num1 * num) / exponential_term
    return str(Decimal(constant_term / partial_sum))[:-1]

print('Добро пожаловать! Мы тут вычисляем число пи. Точность вычисления зависит только от вас!')

while True:
    n = int(input('Введите нужное количество цифер после запятой: '))
    if n <= 0:
        print('Если не нужно вычислять пи - можно выйти из программы, зачем отрицательные числа-то вводить... Для выхода из программы напишите 0, чтобы остаться - нажмите Enter')
        decision = int(input())
        if decision == 0:
            print('До новых встреч!')
            break
    else:
        print(pi(n))
        
        
def test():
    a = int(input())
    pi_const = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674"
    var_from_def = pi(a)
    i = 0
    while i <= a:
        for i in range(0, len(var_from_def)):
            if var_from_def[i] == pi_const[i]:
                continue
            else:
                print(f"ошибка в {i - 1} цифре после запятой")
        i += 1

"""
Created on Wed Oct 20 01:42:38 2021

@author: anast
"""
