# A001679

> Number of series-reduced rooted trees with n nodes.
> — [OEIS A001679](https://oeis.org/A001679)

Offset 0: 1, 1, 1, 0, 2, 2, 4, 6, 12, 20, 39, 71, 137, 261, 511, 995, …

### Python 3 — 168 bytes

```python
A=[m:=-1,m,1];print(1)
for x in A:print(-(sum(map(int.__mul__,A,A[::-1]))+m%2*A[m//2-1])//2);A+=sum(d*A[1-d]*sum(A[d:1:d]+A[d-1:1:d])for d in range(m,0))//m-A[-1],;m-=1
```

**How it works**

- The entry's g.f.: 1 + ((1 + x)f(x) − (f(x)² + f(x²))/2)/x, with f the
  g.f. of [A001678](../A001678/) (series-reduced planted trees). The
  root may not have exactly two children: (1 + x)f/x counts a root with
  any multiset of planted subtrees, (f² + f(x²))/2 the two-element
  multisets. So for n ≥ 1, with a = A001678,
  **c(n) = a(n+1) + a(n) − ½(Σ_i a(i)·a(n+1−i) + a((n+1)/2))**, the last
  term only for odd n.
- The list and its growth are the [A001678](../A001678/) program: at the
  start of the pass for n (`m` = −n) `A` holds a(0), …, a(n+1), and the
  pass appends a(n+2) through the Euler transform of b(k) = a(k+1)
  (see that page; d = −k runs negative).
- Sentinels: `A` starts as [−1, −1, 1] instead of [0, 0, 1]. For n ≥ 2
  the full convolution Σ_{i=0..n+1} A(i)·A(n+1−i) then equals the true
  one minus 2a(n+1) (from i = 0 and i = n+1) minus 2a(n) (i = 1 and
  i = n), so c(n) = −(conv + e)/2 with e = A((n+1)/2) for odd n: the
  a(n+1) + a(n) term costs nothing. For n = 1 the sentinels give
  −(−1 − 1)/2 = 1 directly.
- The Euler step must not see them: its slices stop before index 1
  (`A[d:1:d]`, `A[d-1:1:d]`); the true a(0) = a(1) = 0 add nothing there,
  and the weights `A[1-d]` only read index 2 and up.
- `m%2*A[m//2-1]` is e: with m = −n, `m//2-1` = −(n+3)/2 counts from the
  end of the n+2 entries to index (n+1)/2. `print(1)` gives c(0) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the
  pair count (Σ a(i)a(n+1−i) + e)/2 is an integer, so `//2` is exact.
- The whole b-file (1001 terms, up to a(1000)) takes about 1.4 reference
  seconds; the bar is the whole b-file in 60 s.
- c(n) grows like 2.19ⁿ, so the 4300-digit int-to-str limit is reached
  only near n = 12600.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001679), CC BY-SA 4.0.
