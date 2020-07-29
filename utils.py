def my_search(l, f):
    l2 = []
    for i in range(len(l)):
        if f(l[i]):
            l2.append(l[i])
    return l2


def my_filter(l, f):
    return list(filter(lambda x: f(x), l))


def my_sort(l, f):
    i = len(l)
    while i > 1:
        for j in range(i - 1):
            if not (f(l[j], l[j + 1])):
                l[j], l[j + 1] = l[j + 1], l[j]
        i -= 1
    return l


def is_consistent(l, f, sol):
    for i in range(1, len(sol)):
        if not f(l.get_patient_by_index(sol[i]), l.get_patient_by_index(sol[0])):
            return False
    return True


def my_backtracking(l, f, group_size):
    domain = [i for i in range(0, l.get_size())]
    k = 0
    sol = [-1]
    while k >= 0:
        is_selected = False
        while is_selected == False and sol[k] < len(domain) - 1:
            sol[k] = sol[k] + 1
            is_selected = is_consistent(l, f, sol)
        if is_selected:
            if len(sol) == group_size:
                yield sol
            else:
                k += 1
                sol.append(-1)
        else:
            sol.pop()
            k -= 1
