# A000276

> Associated Stirling numbers.
> — [OEIS A000276](https://oeis.org/A000276)

Offset 4: 3, 20, 130, 924, 7308, 64224, 623376, 6636960, 76998240, 967524480, …

### Python 3 — 47 bytes

```python
w=1;f=2;m=3
while[print(m*w)]:w=w*m+f;f*=m;m+=1
```

**How it works**

- a(n) counts the derangements of n elements with exactly two cycles. If
  the cycle through 1 has length k (2 ≤ k ≤ n−2), there are
  C(n−1,k−1)·(k−1)!·(n−k−1)! = (n−1)!/(n−k) of them, so
  a(n) = (n−1)!·(H(n−2) − 1), Jovovic's formula on the OEIS page.
- Let w(k) = k!·(H(k) − 1). Then a(n) = (n−1)·w(n−2), and w obeys the
  A000254 recurrence w(k) = k·w(k−1) + (k−1)!: it is A000254 minus k!, and
  k! solves the same recurrence without the (k−1)! term.
- At the top of each round `w` = w(m−1), `f` = (m−1)! and m = n−1, so the
  header prints m·w(m−1) = a(n). The body is the A000254 update:
  `w=w*m+f` gives w(m), `f*=m` gives m!, `m+=1` moves on.
- The start is w(2) = 1, 2! = 2, m = 3, and the first line is
  3·1 = 3 = a(4).

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file (447
  terms) prints at once; the program stops after a(1558), when the next
  term passes the 4300-digit int-to-str limit of Python 3.11+. The bar is
  the whole b-file in 60 s.
- Ties at 47 bytes: `w=5;f=2;m=3` / `while[print(w-f)]:f*=m;m+=1;w=w*m+f`
  (a(n) = w(n−1) − (n−2)!), and `w=1;f=m=2` / `while[print(-~m*w)]:m+=1;w=w*m+f;f*=m`,
  where m one lower lets f and m start together but costs `-~` in the print.
- The direct recurrence a(n) = (n−1)·(a(n−1) + (n−3)!) is 48 bytes,
  `a=0;f=1;m=3` / `while[print(a:=m*(a+f))]:f*=m-1;m+=1`: its factorial
  lags the multiplier by two, so the update needs `m-1`. Mathar's order-2
  recurrence (proved on the OEIS page) divides by n−2, and the monic
  order-3 one carries quadratic coefficients.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000276), CC BY-SA 4.0.
