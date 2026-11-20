# A002033

> Number of perfect partitions of n.
> — [OEIS A002033](https://oeis.org/A002033)

Offset 0: 1, 1, 1, 2, 1, 3, 1, 4, 2, 3, 1, 8, 1, 3, 3, 8, 1, 8, 1, 8, 3, 3, 1, …

### Python 3 — 76 bytes

```python
a=[0,1];n=1
while[print(a[n])]:n+=1;a+=sum(a[d]for d in range(1,n)if n%d<1),
```

**How it works**

- MacMahon's perfect partitions of n are in one-to-one correspondence
  with the ordered factorizations of n + 1 (the entry's comments, and
  Riordan): if the distinct parts are 1 = s₀ < s₁ < … with sⱼ used
  mⱼ times, perfection forces sⱼ₊₁ = (mⱼ + 1)·sⱼ, so the partition is
  fixed by the ordered list of factors mⱼ + 1 ≥ 2, whose product is
  n + 1. So a(n) = H(n + 1), where H counts ordered factorizations.
- The last factor of an ordered factorization of m > 1 is some divisor
  m/d > 1, and the rest is an ordered factorization of d < m, so
  H(m) = Σ H(d) over the divisors d < m of m, with H(1) = 1 (the empty
  product).
- `a[m]` holds H(m) (`a[0]` is a dummy). Each pass prints H(n), the
  term a(n − 1), then appends H(n + 1) from the stored values.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10000 terms (n = 0 to 9999); the bar is the whole
  b-file in 60 s, about 6 s here: the divisor scan makes it quadratic.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002033), CC BY-SA 4.0.
