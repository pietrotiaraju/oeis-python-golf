# A001677

> Number of series-parallel networks with n edges.
> — [OEIS A001677](https://oeis.org/A001677)

Offset 2: 1, 2, 3, 6, 12, 26, 59, 146, 368, 976, 2667, 7482, 21440, …

### Python 3 — 144 bytes

```python
A=[1,n:=1]
while 1:n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,;print(2*A[n]-(sum(map(int.__mul__,A,A[::-1]))+~n%2*A[n//2])//2)
```

**How it works**

- The entry's formula:
  **a(n) = s(n) − ½·Σ_{i=1..n−1} s(i)·s(n−i) − ½·s(n/2)**, the last
  term only for even n, where s is [A000084](../../A000xxx/A000084/)
  (series-parallel networks with n edges). The subtracted part is the
  number of unordered pairs {N₁, N₂} of networks with n edges in all, the
  coefficient of xⁿ in (S(x)² + S(x²))/2.
- The first half of the loop body is the A000084 program unchanged: `A`
  holds s(0) = 1, s(1), …, and `A+=…` appends s(n) from the Euler
  transform recurrence n·s(n) = Σ_{d<n} 2d·b(d)·Σ_{j≥1} s(n − jd), with
  b = A000669 (see that page for why `d` runs over 1, 1, 2, …, n − 1).
- `sum(map(int.__mul__,A,A[::-1]))` is the full convolution
  Σ_{i=0..n} s(i)·s(n−i). Its two end terms are s(0)·s(n) = s(n) each, so
  it equals P + 2s(n) with P the sum in the formula, and
  a(n) = s(n) − (P + e)/2 = 2s(n) − (conv + e)/2 with e = s(n/2) for even
  n and 0 for odd n.
- `~n%2*A[n//2]` is that e: `~n%2` is (−n−1) mod 2 = 1 exactly when n is
  even, and binds tighter than `*`.
- `A=[1,n:=1]` sets s(0) = s(1) = 1 and n = 1; the first pass computes
  s(2) and prints a(2).

**Notes**

- Exact integer arithmetic, so the program is right for every n:
  P + e = 2·Σ_{i<n/2} s(i)s(n−i) + s(n/2)(s(n/2) + 1) (last term for even
  n) is even, hence so is conv + e, and `//2` is exact.
- Each term costs O(n log n) additions for s(n) and n multiplications for
  the convolution; the whole b-file (499 terms, up to a(500)) prints in
  about half a second. The bar is the whole b-file in 60 s.
- s(n) grows like 3.56ⁿ, so from about n = 7800 Python's 4300-digit
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 144 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001677), CC BY-SA 4.0.
