# A002182

> Highly composite numbers: numbers n where d(n), the number of divisors of n (A000005), increases to a record.
> — [OEIS A002182](https://oeis.org/A002182)

Offset 1: 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, …

### Python 3 — 194 bytes

```python
from heapq import*
H=heappush;h=[(1,1,2,1,9e999)];r=0
while 1:
 x,s,p,e,f=heappop(h);t=s*e
 if t>r:r=t;print(x)
 e<f!=H(h,(x*p,s,p,e+1,f));q=p+1
 while pow(x,q,q)<1:q+=1
 e>1!=H(h,(x*q,t,q,2,e))
```

**How it works**

The record scan d(1), d(2), … is exact but hopeless here: a(40) is
already 1441440 and a(350) has 35 digits. The program only looks at the
numbers whose exponents don't increase from one prime to the next.

- **Only sorted numbers matter.** Call x *sorted* if
  x = 2^(a₁)·3^(a₂)·…·p_k^(a_k) over the first k primes with
  a₁ ≥ a₂ ≥ … ≥ a_k ≥ 1 (and x = 1). Moving the exponents of any y onto
  the smallest primes in non-increasing order gives a sorted y′ ≤ y with
  d(y′) = d(y), and y′ < y unless y is already sorted. So every highly
  composite number is sorted (otherwise y′ would beat it), and a sorted x
  whose d(x) beats every smaller sorted number beats every smaller y (its
  y′ is sorted and no larger). The records of d over the sorted numbers,
  taken in increasing order, are exactly the highly composite numbers.
- **A tree of sorted numbers.** A node is `(x,s,p,e,f)`: p is the last
  prime of x, with exponent e − 1; f − 1 caps that exponent (it is the
  exponent of the previous prime, and f = 9e999, float infinity, for
  p = 2); s is d(x) without the factor of p, so `t=s*e` is d(x). The
  root `(1,1,2,1,9e999)` is x = 1 with exponent 0 at 2. Each node has up
  to two children: x·p (one more p, allowed while `e<f`), and x·q with
  q the next prime, exponent 1 and cap e − 1 (allowed when `e>1`, that
  is when p really divides x; this only stops the root). Every sorted
  number other than 1 has exactly one parent (drop one factor of its
  last prime, or the whole last prime if its exponent is 1), so each is
  made once, and a child is larger than its parent.
- **Increasing order.** The heap pops the nodes in increasing x. If a
  sorted y < x were still unpopped when x is popped, the first unpopped
  node on the path from the root (popped first) to y would be in the
  heap, since its parent is popped, and it would be at most y < x,
  which contradicts x being the smallest. The values x are all
  different, so the tuples never compare beyond x.
- **The next prime.** A node x > 1 is divisible by every prime up to p.
  For p < k < q every prime factor r of k is at most p, and the power
  r^j ∥ k has j < k, so x^k ≡ 0 (mod k); for the prime q, x^q ≢ 0. So
  `q=p+1` and `while pow(x,q,q)<1:q+=1` stop at the next prime, with no
  primality test. (At the root the loop stops at 3, and the push is
  skipped.)
- `e<f!=H(…)` and `e>1!=H(…)` are chained comparisons: the push runs
  only when the first test holds. `H=heappush` saves bytes on the two
  pushes.
- `if t>r:r=t;print(x)` prints each new record of d.

**Notes**

- Exact integers (the float infinity is only compared with exponents):
  right for every n.
- The heap holds the frontier of the tree, which grows fast: 300 terms
  come in about 5 s here with 60 MB, 350 in 14 s with 110 MB and 400 in
  about 40 s with 240 MB (a(400) has 39 digits). The b-file has 10000
  terms; the bar is 300 terms in 20 s, a short timeout that keeps the
  check's memory small.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 194 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002182), CC BY-SA 4.0.
