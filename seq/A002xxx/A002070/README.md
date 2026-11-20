# A002070

> Coefficient of x^p (p = n-th prime) in x * Product_{k>=1} (1-x^k)^2*(1-x^11k)^2.
> — [OEIS A002070](https://oeis.org/A002070)

Offset 1: -2, -1, 1, -2, 1, 4, -2, 0, -1, 0, 7, 3, …

### Python 3 — 111 bytes

```python
P=m=1;a=[1]
while 1:a+=2*sum(d*sum(a[d::d])<<(d%11<1)for d in range(-m,0))//m,;P*=m*m;m+=1;P%m and print(a[-1])
```

**How it works**

- **The series.** Let Π_{k≥1} (1 − x^k)²(1 − x^{11k})² = Σ b(m)·x^m. The
  coefficient of x^p in x times it is b(p−1), so the program prints
  b(m−1) whenever m is prime.
- **The recurrence.** The product is Π (1 − x^k)^c(k) with c(k) = 2, or 4
  when 11 divides k. The logarithmic derivative gives

  m·b(m) = −Σ_{k≥1} k·c(k)·(b(m−k) + b(m−2k) + b(m−3k) + …),

  so the floor division by m is exact.
- **Negative steps** (as in [A002107](../A002107/)): the list `a` holds
  b(0), …, b(m−1). For d = −k, `a[d::d]` is b(m−k), b(m−2k), …, and the
  sum over d = −m, …, −1 is −Σ k·(…); the factor `2*` and `//m` with a
  positive m give the right sign. `<<(d%11<1)` doubles the term when
  11 | k (c(k) = 4); a shift binds looser than `*`, so it acts on the whole
  `d*sum(…)`.
- **The primes.** After `P*=m*m;m+=1`, `P` is ((m−1)!)², so by Wilson's
  theorem `P%m` is 1 when m is prime and 0 when it is not (m = 4: 36 ≡ 0),
  and `a[-1]` is then b(m−1).

**Notes**

- Exact integer arithmetic, so the program is right for every n. This is
  the weight-2 newform of level 11 (the elliptic curve 11a), but the
  program only uses the product that defines the sequence.
- Every coefficient up to the prime is needed, at about m·ln m slice
  additions and m Python steps each, so the cost grows like p². The
  b-file has 10000 terms (up to p = 104729); the bar is 900 terms in 60 s
  (p = 6997), about 21 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002070), CC BY-SA 4.0.
