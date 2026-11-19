# A002002

> a(n) = Sum_{k=0..n-1} binomial(n,k+1) * binomial(n+k,k).
> — [OEIS A002002](https://oeis.org/A002002)

Offset 0: 0, 1, 5, 25, 129, 681, 3653, 19825, 108545, 598417, 3317445, …

### Python 3 — 56 bytes

```python
a=b=n=1
while[print(b-a>>1)]:a,b=b,6*b-a-(3*b-a)//n;n+=1
```

**How it works**

- Write D(m, k) = Σⱼ 2ʲ·C(m, j)·C(k, j) for the Delannoy numbers (lattice
  paths from (0, 0) to (m, k) with steps east, north and north-east). The
  term is a(n) = D(n, n−1): with j = k + 1 the sum is
  Σⱼ C(n, j)·C(n−1+j, n), and Vandermonde's
  C(n−1+j, n) = Σᵢ C(j, i)·C(n−1, n−i) together with
  Σⱼ C(n, j)·C(j, i) = C(n, i)·2ⁿ⁻ⁱ turns it into
  Σᵢ 2ⁿ⁻ⁱ·C(n, i)·C(n−1, n−i), which is D(n, n−1) after i ↦ n − i.
- A path to (n, n) ends with an east, a north or a diagonal step, so
  D(n, n) = D(n−1, n) + D(n, n−1) + D(n−1, n−1) = 2·D(n, n−1) + D(n−1, n−1).
  With the central Delannoy numbers D(n) = D(n, n)
  ([A001850](../../A001xxx/A001850/)) this gives
  a(n) = (D(n) − D(n−1))/2, also for n = 0 if D(−1) = 1.
- D(n) has the generating function (1 − 6x + x²)^(−1/2), so
  n·D(n) = 3(2n − 1)·D(n−1) − (n − 1)·D(n−2), written as
  D(n) = 6D(n−1) − D(n−2) − (3D(n−1) − D(n−2))/n with an exact `//n`
  (see A001850). `a`, `b` hold D(n−1), D(n) and `b-a>>1` prints a(n).
- Starting from D(−1) = D(0) = 1 with n = 1 is safe: at n = 1 the
  recurrence gives 6b − a − (3b − a) = 3b, so the value of D(−1) only
  matters for the first printed term, 0. Incrementing n after the step
  lets `a=b=n=1` set everything in one assignment.

**Notes**

- The double sum with `math.comb` is longer, and so are the order-2
  recurrence for a(n) itself (coefficients of degree 2 in n) and the
  order-3 one.
- Exact integer arithmetic, so the program is right for every n; a(n) has
  about 0.77n digits, so Python's 4300-digit int-to-str limit stops the
  output near n = 5600.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002002), CC BY-SA 4.0.
