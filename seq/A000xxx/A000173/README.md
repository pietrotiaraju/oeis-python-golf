# A000173

> Unitary-sociable numbers (smallest member of each cycle).
> — [OEIS A000173](https://oeis.org/A000173)

Offset 1: 30, 1482, 2418, 24180, 35238, 263820, 395730, 473298, …

### Python 3 — 135 bytes

```python
import math
n=1
while 1:
 m=n=n+1;v=[]
 while n<=(m:=sum(math.lcm(d,m//d)//m*d for d in range(1,m)))not in v:v+=m,;n in v[2:]==print(n)
```

**How it works**

- The map is s\*(m) = σ\*(m) − m, the sum of the unitary divisors d < m
  (d | m with gcd(d, m/d) = 1). A term is the smallest member of a cycle
  of s\* of length at least 3; lengths 1 and 2 are the unitary perfect
  and unitary amicable numbers. Example: 30 → 42 → 54 → 30.
- Unitary-divisor test without a divisibility check: for every d < m,
  lcm(d, ⌊m/d⌋) ≤ d·⌊m/d⌋ ≤ m, with equality exactly when d | m and
  gcd(d, m/d) = 1. So `math.lcm(d,m//d)//m*d` is d for a unitary divisor
  and 0 otherwise.
- For each start n the orbit goes into `v` while the chained test
  `n<=m not in v` holds. It stops when a value drops below n (then n is
  not the smallest member of any cycle), or when a value repeats.
- The `<=` lets n itself go into `v` once when the orbit comes back to
  it; the next value is then the first one of the orbit, already in `v`,
  and the loop ends. So n is a term exactly when it shows up in `v[2:]`
  (cycle length ≥ 3), and `n in v[2:]==print(n)` prints it at that
  moment: the chained comparison calls `print` only when the first test
  is true.
- An orbit that falls into another cycle, all of whose members are
  above n, stops at the first repeated value without n ever entering
  `v`.

**Notes**

- Exact integer arithmetic. The program halts on every start n whose
  orbit drops below n, comes back to n, or repeats a value; it would hang
  on a start whose unitary aliquot sequence grows forever while staying
  above n. Whether unbounded unitary aliquot sequences exist is not known
  (H. J. J. te Riele, *Unitary aliquot sequences*, Mathematisch Centrum,
  Amsterdam, 1972–73; R. K. Guy, *Unsolved Problems in Number Theory*,
  B8), so correctness for every n rests on that open question; every
  printed number is a term regardless.
- Each step costs O(m) `lcm` calls. On the machine that set the bar,
  a(1)…a(3) come out in about 4 s and a(4) = 24180 had not appeared
  after 400 s, so the bar is 3 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 135 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000173), CC BY-SA 4.0.
