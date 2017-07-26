import random
import os

def case(n, ai):
    n = random.randint(1, n)
    q = random.randint(1, n)
    k = random.randint(1, max(1, n/2))
    if random.choice([0, 1]):
        k = random.randint(max(1, n/2), n)
    ai = random.randint(1, ai)
    return "%d %d %d\n%s\n%s\n" % (
        n,
        q,
        k,
        " ".join(str(random.randint(1, ai)) for _ in xrange(n)),
        "\n".join(str(random.randint(k, n)) for _ in xrange(q))
    )


ind = 0
for n, ai in [
    (10, 10),
    (100, 20),
    (1000, 10**5),
    (10**6, 10**5),
    (5*10**6, 10**5),
]:
    for _ in xrange(3):
        ifindex = str(ind).zfill(2)
        ifname = "tests/input/input%s.txt" % ifindex
        ind += 1
        fh = open(ifname, 'w+')
        test_data = case(n, ai)
        fh.write(test_data)
        fh.close()
        print "%s file created" % ifname


os.system("g++ -std=c++11 -o a solution.cc")
for index in xrange(ind):
    ofindex = str(index).zfill(2)
    ifname = "tests/input/input%s.txt" % ofindex
    ofname = "tests/output/output%s.txt" % ofindex
    os.system("time -p ./a < %s > %s" % (ifname, ofname))
    print "%s file created" % ofname


os.system("zip -r tests.zip tests") 
