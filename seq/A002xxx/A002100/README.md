# A002100

> a(n) = number of partitions of n into semiprimes (more precisely, number of ways of writing n as a sum of products of 2 distinct primes).
> — [OEIS A002100](https://oeis.org/A002100)

Offset 1: 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, …

### Python 3 — 123 bytes

```python
a=[1];*P,F,n=1,1
while 1:P+=F%n*[n];F*=n*n;a+=sum(p*q*sum(a[-p*q::-p*q])for p in P for q in P if p<q)//n,;print(a[-1]);n+=1
```

**How it works**

- The parts are the products pq of two distinct primes p < q
  ([A006881](https://oeis.org/A006881)), each usable any number of times, so
  the generating function is ∏ 1/(1 − x^(pq)) and, by its logarithmic
  derivative, n·a(n) = Σ_{pq ≤ n} pq·Σ_{j ≥ 1} a(n − j·pq).
- `P` holds the primes up to n, and the generator runs over the pairs
  p < q of it. `a[-p*q::-p*q]` lists a(n − pq), a(n − 2pq), … from the list
  a(0), …, a(n − 1); when pq > n the start lies before the list, Python
  clamps it, and the slice is empty, so pairs with pq > n add nothing.
  `//n` divides exactly.
- Primes come from Wilson's theorem, as in the [A000607](../../A000xxx/A000607/)
  record: F = ((m − 1)!)², so F mod m is 1 when m is prime and 0 otherwise
  (also for m = 1, and for m = 4, where F = 36); `F*=n*n` then moves F on
  to (m!)².
- The offset is 1: a(0) = 1 stays in the list but is never printed, because
  each term is printed after it is appended. The starred assignment sets
  P = [], F = 1, n = 1.

**Notes**

- About π(n)²/2 pairs per term, most of them giving empty slices: the
  whole b-file, 1000 terms (n = 1 to 1000), takes about 3 s here, so the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 123 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002100), CC BY-SA 4.0.
