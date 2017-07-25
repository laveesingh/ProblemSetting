import random

def random_single_query_type(size=1, elem_size=1):
    """
    dependencies: random
    """
    if size==1:  # small
        n = random.randint(1, 15)
        q = random.randint(1, 15)
    elif size==2:  # medium
        n = random.randint(1, 1500)
        q = random.randint(1, 1500)
    elif size==3:  # large
        n = random.randint(1, 5 * 10**5)
        q = random.randint(1, 5 * 10**5)
    else:
        raise Exception("Please specify test data size")
    if elem_size==1:  # small
        ai = 15
    elif elem_size==2:  # medium
        ai = 1500
    elif elem_size==3:  # large
        ai = 5 * 10**5
    else:
        raise Exception("Please specify element data size")
    array = [random.randint(1, ai) for _ in xrange(n)]
    queries = []
    for _ in xrange(q):
        i = random.randint(1, n)
        if random.choice([0, 1]):
            m = n
            while m > 1:
                i = random.choice([i, random.randint(1, m)])
                m /= 32
        j = random.randint(i, n)
        if random.choice([0, 1]):
            m = n
            while m > i:
                j = random.choice([j, random.randint(i, m)])
                m /= 32
        queries.append("%d %d\n" % (i, j))
    nq_str = "%d %d\n" % (n, q)
    arr_str = " ".join(str(s) for s in array) + "\n"
    q_str = "".join(queries)
    return nq_str + arr_str + q_str


def random_single_query_type2(size=1, elem_size=1, test_cases=1):
    if test_cases == 1:
        t = 1
    elif test_cases == 2:
        t = 10
    else:
        raise Exception("Please specify a valid test cases size")
    tests = []
    for _ in xrange(t):
        tests.append(random_single_query_type(size, elem_size))
    t_string = "%d\n" % t
    tests_string = "".join(s for s in tests)
    return t_string + tests_string

