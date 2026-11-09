# A001274

> Numbers k such that phi(k) = phi(k+1).
> — [OEIS A001274](https://oeis.org/A001274)

Offset 1: 1, 3, 15, 104, 164, 194, 255, 495, 584, 975, 2204, 2625, 2834, …

phi is Euler's totient function ([A000010](../../A000xxx/A000010/)).

### Python 3 — 107 bytes

```python
D={};a=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 a-b or print(k-1);a=b
```

**How it works**

- An incremental sieve that keeps every prime factor: `D` maps each
  upcoming number m to the list of primes found so far that divide it.
  A prime p is filed under 2p when it is found, and each time its multiple
  comes up it moves on to the next one (`D[k+p]=…+[p]`). So when k is
  reached, `D.pop(k,…)` gives exactly the primes below k that divide k.
- If k is not in `D`, no smaller prime divides it, so k is prime and the
  default `[k]` is its only prime factor; filing it under 2k starts its
  walk.
- `b` starts at k and `b-=b//p` multiplies it by 1 − 1/p for each prime
  factor p, which gives φ(k) = k·∏(1 − 1/p). Every step is exact: after
  dividing out some of the primes, the others still divide `b`.
- `a` holds φ(k − 1), so `a-b or print(k-1)` prints k − 1 exactly when
  φ(k − 1) = φ(k); then `a=b`. The loop starts with a = φ(1) = 1 and
  k = 1, so the first test is k = 1 against 2, and every k is tested in
  order, forever.

**Notes**

- Each k costs a dictionary lookup and one step per distinct prime factor,
  so the time grows almost linearly; `D` holds at most one entry per prime found.
  Here a(115) = 5577825 arrives after about 15 reference seconds.
- The plain count `sum(gcd(k+1,j)<2for j in range(k+1))` with
  `from math import*` is 90 bytes but takes time proportional to k for
  each k, so it reaches only about 20 terms. A totient sieve over a list
  that doubles its length every round is about 150 bytes and needs much
  more memory.
- The b-file has 42499 terms (up to 999628162357724), far out of reach;
  the bar is 115 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001274), CC BY-SA 4.0.
