# TURDEAN PAULA-FLORINA PROBLEMELE: SET1 PROBLEMA 6 si SET2 PROBLEMA 13
from typing import List


def citire_lista():
    """
    Formeaza lista necesara prin citirea numarului de elemente si a elementelor propiu-zise.
    :return: Returneaza lista citita.
    """
    lst = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst


def toate_elementele_div_k(lst: list[int], k: int):
    """
    Determina daca toate elementele dintr-o lista sunt divizibile cu un numar dat
    :param lst: Lista verificata
    :param k: Numarul intreg cu care se verifica divizibilitatea
    :return: Returneaza True daca toate elementele din lista sunt divizibile cu k si False in caz contrar
    """
    for x in lst:
        if x % k != 0:
            return False
    return True


def test_toate_elementele_div_k():
    assert toate_elementele_div_k([2, 4, 6], 2) is True
    assert toate_elementele_div_k([10, 5, 25, 74], 5) is False
    assert toate_elementele_div_k([2, 4, 8], 3) is False


def get_longest_div_k(lst: list[int], k: int) -> list[int]:
    """
    Determina cea mai lunga subsecventa de numere divizibile cu k (dintr-o lista)
    :param lst: Lista initiala
    :param k: Numarul intreg cu care se verifica divizibilitatea
    :return: Returneaza o lista de numere divizibile cu k (cea mai lunga)
    """
    subsecventa = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if toate_elementele_div_k(lst[i:j + 1], k) is True and len(lst[i:j + 1]) > len(subsecventa):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_div_k():
    assert get_longest_div_k([10, 2, 20, 30, 45, 50, 110, 100], 10) == [50, 110, 100]
    assert get_longest_div_k([1, 3, 5, 7, 9, 11], 2) == []
    assert get_longest_div_k([1, 3, 4, 5, 7, 9], 2) == [4]


def is_prime(n):
    """
    Verifica daca un numar intreg este prim sau nu.
    :param n: Un numar intreg
    :return: Returneaza True daca numarul este prim si False in caz contrar.
    """
    copie = int(n)
    if copie < 2:
        return False
    else:
        for i in range(2, copie // 2):
            if copie % i == 0:
                return False
        return True


def test_is_prime():
    assert is_prime(23) is True
    assert is_prime(14) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False


def format_din_cifre_prime(x: int):
    """
    Verifca daca un numar este format doar din cifre prime
    :param x: Numarul intreg verificat
    :return: Returneaza True daca x e foamat doar din cifre prime si False in caz contrar
    """
    copie = x
    while copie != 0:
        cifra = copie % 10
        if is_prime(cifra) is False:
            return False
        copie = copie // 10
    return True


def test_format_din_cifre_prime():
    assert format_din_cifre_prime(357) is True
    assert format_din_cifre_prime(123) is False
    assert format_din_cifre_prime(2357) is True
    assert format_din_cifre_prime(104689) is False


def toate_elementele_au_doar_cifre_prime(lst: list[int]):
    """
    Verifica daca toate elementele dintr-o lista sunt formate din cifre prime
    :param lst: Lista verificata
    :return: Returneaza True daca lista are toatele elementele din cifre prime si False in caz contrar
    """
    for x in lst:
        if format_din_cifre_prime(x) is False:
            return False
    return True


def test_toate_elementele_au_doar_cifre_prime():
    assert toate_elementele_au_doar_cifre_prime([357, 22, 577, 732]) is True
    assert toate_elementele_au_doar_cifre_prime([357, 22, 577, 732, 200]) is False
    assert toate_elementele_au_doar_cifre_prime([]) is True


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga secventa de numere formate doar din cifre prime
    :param lst: Lista initiala
    :return: Returneaza o lista formata din elemente care au doar cifre prime (cea mai lunga)
    """
    subsecventa = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if toate_elementele_au_doar_cifre_prime(lst[i:j + 1]) is True and len(lst[i:j + 1]) > len(subsecventa):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([357, 22, 577, 732, 200, 222, 235]) == [357, 22, 577, 732]
    assert get_longest_prime_digits([1234, 4321, 575, 5678, 8765, 2, 3]) == [2, 3]
    assert get_longest_prime_digits([]) == []


def main():
    test_toate_elementele_div_k()
    test_get_longest_div_k()
    test_is_prime()
    test_format_din_cifre_prime()
    test_toate_elementele_au_doar_cifre_prime()
    test_get_longest_prime_digits()
    shouldRun = True
    while shouldRun:
        print("1)Citire lista.")
        print("2)Determinare cea mai lunga secventa de numere divizibile cu un numar dat.")
        print("3)Determinare cea mai lunga secventa...")
        print("x)Iesire")
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            nr = int(input("Dati numarul pentru verificare: "))
            print(get_longest_div_k(lst, nr))
        elif optiune == "x":
            print("Ati iesit din program")
            shouldRun = False


main()
