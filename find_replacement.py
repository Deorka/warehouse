def replacement():
    """
    rejnfreknfjernfer
    :return:
    """
    n = int(input())
    numbers = input().split(" ")
    numbers = list(map(lambda x: int(x), numbers))
    even = -1
    odd = -1
    for i in range(0, n):
        if numbers[i] % 2 != (i + 1) % 2:
            if numbers[i] % 2:
                if odd == -1:
                    odd = i + 1
                else:
                    print("-1 -1")
                    return
            else:
                if even == -1:
                    even = i + 1
                else:
                    print("-1 -1")
                    return
    print(even, odd)


"""На физкультуре происходит разбиение по двум командам. Ребята выстроены в шеренгу, у каждого из них есть свой рост
 ﻿a_iai
​
 ﻿ Разбиение по командам произойдет по принципу «четный-нечетный» — все школьники с четным ростом отправляются в одну
  команду, а нечетные — в другую.

В отличие от привычного урока, ребята не выстроились по росту. Вместо привычного порядка они встали случайно. Теперь 
физрук Яша смотрит на шеренгу и думает — может ли ровно одна пара учеников поменяться местами так, чтобы команды 
оказались такими же, как и по принципу «первый-второй». Иначе говоря, он хочет получить такой порядок, при котором все 
ученики с четным ростом стоят на четных позициях, а с нечетным — на нечетных.

Помогите Яше найти нужную замену.


Формат входных данных

В первой строке находится число ﻿n(2 \leq n \leq 1000)n(2≤n≤1000)﻿ — количество учеников в шеренге.

В следующей строке находится ﻿nn﻿ натуральных чисел ﻿a_i(1\leq a_i \leq 10^9)a 
i
​
 (1≤a 
i
​
 ≤10 
9
 )﻿ — рост учеников.

Формат выходных данных

В единственной строке выведите ﻿ii﻿ и ﻿jj﻿ — номера элементов, которые нужно поменять местами, чтобы добиться заданного условия ﻿(1 \leq i , j \leq n , i \ne j)(1≤i,j≤n,i 

​
 =j)﻿. Если ответов несколько — разрешается вывести любой.

Если не существует способа поменять два элемента местами — выведите ﻿-1 -1−1−1﻿."""

if __name__ == '__main__':
    #replacement()
    print(replacement.__doc__)
