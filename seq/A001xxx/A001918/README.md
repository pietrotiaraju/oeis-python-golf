# A001918

> Least positive primitive root of n-th prime.
> — [OEIS A001918](https://oeis.org/A001918)

Offset 1: 1, 2, 2, 3, 2, 2, 3, 2, 5, 2, 3, 2, 6, 3, 5, 2, 2, 2, 2, 7, 5, 3, 2, 3, …

### Python 3 — 95 bytes

```python
P=k=1
while[any(sum(g**e%k<2for e in range(k))<3!=print(g)for g in range(1,P%k*k))]:P*=k*k;k+=1
```

**How it works**

- Modulo a prime p, g^e ≡ 1 holds exactly at the multiples of ord_p(g),
  so among e = 0, 1, …, p − 1 it holds at e = 0 and e = p − 1 only when g
  has order p − 1, and at least three times otherwise. So g is a
  primitive root exactly when `sum(g**e%k<2for e in range(k))<3`
  (for 1 ≤ g < p, g^e mod p is never 0, so `<2` means `==1`).
- For p = 2 the group is trivial and g = 1 passes (e = 0 and e = 1), which
  is the OEIS convention a(1) = 1.
- `any(c<3!=print(g)for g in range(1,…))` tries g = 1, 2, … in order. The
  chained comparison calls `print` only when c < 3, and `3!=None` is
  true, so `any` stops right after printing the least primitive root.
  Every prime has a primitive root, so exactly one value is printed per
  prime.
- Composites are skipped with Wilson's theorem, squared:
  P = ((k − 1)!)², and `P%k` is 1 when k is prime and 0 when k is
  composite (k = 4 included: 36 ≡ 0) or 1, so `range(1,P%k*k)` is 1..k − 1
  for primes and empty otherwise.

**Notes**

- Wilson's theorem and exact integers: right for every n.
- `pow(g,e,k)` instead of `g**e%k` is 4 bytes longer and faster.
- Every candidate g costs p powers, and most primes need only a few
  candidates (the least primitive root is usually 2, 3 or 5): about 530
  terms (p = prime(530) = 3821) in 24 s here. The b-file has 10000 terms;
  the bar is 500 terms (p = 3571) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001918), CC BY-SA 4.0.
