# A000837

> Number of partitions of n into relatively prime parts. Also aperiodic partitions.
> — [OEIS A000837](https://oeis.org/A000837)

Offset 0: 1, 1, 1, 2, 3, 6, 7, 14, 17, 27, 34, 55, 63, 100, 119, 167, 209, 296, …

### Python 3 — 131 bytes

```python
*a,n=1,0;b=[]
while[print(x:=a[-1]-sum(b[d]for d in range(1,-n)if n%d<1))]:b+=x,;n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- Dividing each part of a partition of n by the gcd g of its parts gives a
  partition of n/g into relatively prime parts, so p(n) = Σ_{d | n} a(d) for
  n ≥ 1 (the OEIS formula ∏ 1/(1−qᵏ) = 1 + Σ a(n)qⁿ/(1−qⁿ)). Hence
  a(n) = p(n) − Σ a(d) over the divisors d < n, and a(0) = p(0) = 1.
- The partition numbers come from the [A000041](../A000041/) program: `a`
  is [p(0), …, p(m)] and `n` is −m; with d negative, `a[d::d]` walks back
  from the end, and Σ d·sum(a[d::d]) over d = −m … −1 is −m·p(m) by the
  identity m·p(m) = Σ σ(k)·p(m−k).
- `b` lists a(0), …, a(m−1). The print computes
  `x:=a[-1]-sum(b[d]for d in range(1,-n)if n%d<1)` (the divisor test
  `n%d<1` works with negative n) and `b+=x,` stores it.
- For m = 0 and 1 the divisor range is empty, which gives a(0) = a(1) = 1.
- The walrus in the print is 2 bytes under keeping `b` one term ahead and
  printing `b[-1]`.

**Notes**

- Exact integer arithmetic, correct for every n.
- Term m costs about m·ln m additions for p(m) and m remainders for the
  divisor sum: 8000–9700 terms in 60 s on the test machine.
- The b-file has 10001 terms (up to a(10000)); the bar is 6500 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000837), CC BY-SA 4.0.
