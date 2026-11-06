# A000348

> Number of ways to pair up {1^2, 2^2, ..., (2n)^2 } so sum of each pair is
> prime.
> — [OEIS A000348](https://oeis.org/A000348)

Offset 1: 1, 1, 2, 4, 12, 9, 72, 160, 428, 2434, 3011, 10337, 126962, …

### Python 3 — 157 bytes

```python
f=lambda s:s<{0}or sum(f(s-{o})for o in s if{o*o+4*len(s)**2}-C)
n=1
while R:=range(3,4*n*n,2):C={a*b for a in R for b in R};print(f({*range(1,2*n,2)}));n+=1
```

**How it works**

- The frame of [A000341](../A000341/) with squares. Two odd squares or two
  even squares add up to an even number of at least 10, so every pair is
  an odd square o² and an even square, and a(n) counts the perfect
  matchings between o = 1, 3, …, 2n − 1 and 2, 4, …, 2n with o² + e² prime.
- `s` is the set of free odd numbers; the even numbers are matched from the
  top down, so the next one is 2·len(s) and the sum is o² + 4·len(s)².
  `s<{0}` is true only for the empty set, which counts 1.
- `C` is the set of products of two odd numbers from 3 up to 4n² − 1. Every
  odd composite up to the largest sum, (2n − 1)² + (2n)² < 8n², is such a
  product (its larger factor is at most a third of it), so an odd sum is
  prime exactly when it is not in `C`, and `{…}-C` is then a non-empty set,
  hence true.
- The range is named in the loop condition; it is never empty (it is {3}
  for n = 1).

**Notes**

- Exact integers, a direct count of the matchings.
- A set of primes by trial division up to 9n²,
  `Q:={p for p in range(9*n*n)if all(p%d for d in range(2,p))}` in the loop
  condition and `…in Q` in the test, is 168 bytes.
- The search has no memo, so its time grows with the number of partial
  matchings: a(14) prints within 10 s and a(15) = 783550 at about 26 s.
  The bar is 12 terms in 60 s; the b-file is the 31 terms of the OEIS entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 157 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000348), CC BY-SA 4.0.
