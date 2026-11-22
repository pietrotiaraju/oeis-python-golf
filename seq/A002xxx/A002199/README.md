# A002199

> Least negative primitive root of n-th prime.
> — [OEIS A002199](https://oeis.org/A002199)

Offset 1: 1, 1, 2, 2, 3, 2, 3, 4, 2, 2, 7, 2, …

The least g ≥ 1 such that −g is a primitive root of the n-th prime p;
the program is the [A001918](../../A001xxx/A001918/) one with g replaced
by −g.

### Python 3 — 98 bytes

```python
P=k=1
while[any(sum((-g)**e%k<2for e in range(k))<3!=print(g)for g in range(1,P%k*k))]:P*=k*k;k+=1
```

**How it works**

- Modulo a prime p, (−g)^e ≡ 1 holds exactly at the multiples of the
  order of −g, so among e = 0, 1, …, p − 1 it holds at e = 0 and
  e = p − 1 only when −g has order p − 1, and at least three times
  otherwise. So −g is a primitive root exactly when
  `sum((-g)**e%k<2for e in range(k))<3`. For 1 ≤ g < p, (−g)^e is never
  0 mod p, and Python's `%` returns a value in [0, p) for the negative
  odd powers too, so `<2` means ≡ 1.
- For p = 2, −1 ≡ 1 passes (e = 0 and e = 1), and for p = 3, −1 ≡ 2 is a
  primitive root: a(1) = a(2) = 1, as in the data.
- `any(c<3!=print(g)for g in range(1,…))` tries g = 1, 2, … in order. The
  chained comparison calls `print` only when c < 3, and `3!=None` is
  true, so `any` stops right after printing the least g. Every prime has
  a primitive root r, and −g = r for g = p − r, so exactly one value is
  printed per prime.
- Composites are skipped with Wilson's theorem, squared:
  P = ((k − 1)!)², and `P%k` is 1 when k is prime and 0 when k is
  composite (k = 4 included: 36 ≡ 0) or 1, so `range(1,P%k*k)` is
  1, …, k − 1 for primes and empty otherwise.

**Notes**

- Wilson's theorem and exact integers: right for every n.
- Every candidate g costs p powers: 500 terms (p ≤ 3571) arrive in 9
  reference seconds (15 s here). The b-file has 10000 terms; the bar is
  500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002199), CC BY-SA 4.0.
