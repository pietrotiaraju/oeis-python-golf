# A001494

> Numbers k such that phi(k) = phi(k+2).
> — [OEIS A001494](https://oeis.org/A001494)

Offset 1: 4, 7, 8, 10, 26, 32, 70, 74, 122, 146, 308, 314, 386, 512, 554, 572, 626, 635, 728, 794, 842, …

### Python 3 — 115 bytes

```python
D={};a=b=0;k=1
while 1:
 c=k=k+1
 for p in D.pop(k,[k]):c-=c//p;D[k+p]=D.get(k+p,[])+[p]
 a-c or print(k-2);a,b=b,c
```

**How it works**

- **φ by an incremental sieve**, as in [A001274](../A001274/)
  (φ(k) = φ(k + 1)): `D` maps each upcoming number m to the list of primes
  found so far that divide it. A prime p is filed under 2p when it is
  found, and each time its multiple comes up it moves on to the next one
  (`D[k+p]=…+[p]`). So when k is reached, `D.pop(k,…)` gives exactly the
  primes below k that divide k; if k is not in `D`, no smaller prime
  divides it, k is prime and the default `[k]` is its only prime factor.
- `c` starts at k and `c-=c//p` multiplies it by 1 − 1/p for each prime
  factor p, which gives φ(k) = k·∏(1 − 1/p); every step is exact, since
  after dividing out some of the primes the others still divide `c`.
- **Two behind.** Before k is handled, `a` = φ(k − 2) and `b` = φ(k − 1);
  `a-c or print(k-2)` prints k − 2 exactly when φ(k − 2) = φ(k), then
  `a,b=b,c` moves the window on. The loop starts at k = 2 with both set to
  0 (a stand-in for φ(0) and φ(1)): the tests at k = 2 and 3 compare 0 with
  φ(2) = 1 and φ(3) = 2, so nothing spurious is printed, and 1 is rightly
  left out since φ(1) = 1 ≠ φ(3) = 2. From k = 4 on every pair (k − 2, k) is
  tested with the true values, in order, forever.

**Notes**

- Each k costs a dictionary lookup and one step per distinct prime factor;
  `D` holds one entry per prime found (about 100 MB at the bar). The
  10000-term b-file (up to 5231234) takes about 25 s on a slow PC; the bar
  is the whole b-file in 60 s.
- Counting `sum(math.gcd(k,j)<2for j in range(k))` with `import math` and
  the same two-behind window is 99 bytes, but each k then costs time
  proportional to k: about 110 terms in 30 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 115 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001494), CC BY-SA 4.0.
