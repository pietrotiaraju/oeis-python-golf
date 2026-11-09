# A001181

> Number of Baxter permutations of length n (also called Baxter numbers).
> — [OEIS A001181](https://oeis.org/A001181)

Offset 0: 1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202, 326240, 1882960, 11140560, 67329992, 414499438, 2593341586, …

### Python 3 — 75 bytes

```python
a=b=1;k=3
while[print(a)]:a,b=((k-3)*(7*k*a+8*(k-4)*b)+12*a)//k//-~k,a;k+=1
```

**How it works**

- R. L. Ollerton's D-finite recurrence from the OEIS entry,
  (n+2)(n+3)·a(n) = (7n²+7n−2)·a(n−1) + 8(n−1)(n−2)·a(n−2), with
  a(0) = a(1) = 1. It is a recurrence of the closed form
  a(n) = Σₖ C(n+1,k−1)·C(n+1,k)·C(n+1,k+1) / (C(n+1,1)·C(n+1,2))
  (Chung, Graham, Hoggatt and Kleiman, 1978), a sum of hypergeometric
  terms, of the kind Zeilberger's algorithm certifies.
- Written with k = n + 2 the coefficients factor:
  k(k+1)·a(n) = (k−3)·(7k·a(n−1) + 8(k−4)·a(n−2)) + 12·a(n−1).
  The division `//k//-~k` is exact because the right side is k(k+1)
  times an integer.
- The loop starts at k = 3, which computes a(1) from a(0) = 1. There the
  factor k − 3 kills the a(n−2) term, so `b` can start at any value:
  `a=b=1` sets both.

**Notes**

- Two big-integer products per term: the whole b-file prints in a
  fraction of a second. The closed form needs `from math import*` and a
  special case for n = 0 (C(1,1)·C(1,2) = 0), and comes out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001181), CC BY-SA 4.0.
