# Commonly Used Rules


def np_contains_m(n, m, p):
    n **= p
    str_n = str(n)
    str_m = str(m)
    return str_n.count(str_m)


def n2_contains_m(n, m):
    return np_contains_m(n, m, 2)


def n3_contains_m(n,m):
    return np_contains_m(n, m, 3)