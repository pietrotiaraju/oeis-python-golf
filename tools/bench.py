"""Fixed benchmark that tools/verify.py runs, like a program, to measure how fast a machine is.

It mixes what the records spend their time on: small-int loops, set and dict
comprehensions, complex numbers, big integers, strings and frozensets. It prints
the fastest of five rounds, in seconds; verify.py divides every timing by
(that time / REF_BENCH), so timings are in reference seconds on any machine.
Changing this file changes every verdict: keep it fixed, or re-measure REF_BENCH.
"""
import time


def work():
    s = 0
    for i in range(720000):
        s += i * i % 7
    squares = {x * x + 4 * y * y for x in range(500) for y in range(500)}
    d = {}
    for i in range(360000):
        d[i % 997] = d.get(i % 997, 0) + i
    z = sum(complex(i, -i) * 1j for i in range(180000))
    f = 1
    for i in range(1, 5000):
        f *= i
    words = sorted(str(i * 7919) for i in range(180000))
    shapes = {frozenset((i, j, i + j)) for i in range(300) for j in range(300)}
    return s, len(squares), len(d), z, f % 1000, words[0], len(shapes)


best = float("inf")
for _ in range(5):
    t = time.perf_counter()
    work()
    best = min(best, time.perf_counter() - t)
print(best)
