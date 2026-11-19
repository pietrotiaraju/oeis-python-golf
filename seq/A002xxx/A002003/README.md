# A002003

> a(n) = 2 * Sum_{k=0..n-1} binomial(n-1, k)*binomial(n+k, k).
> — [OEIS A002003](https://oeis.org/A002003)

Offset 0: 0, 2, 8, 38, 192, 1002, 5336, 28814, 157184, 864146, 4780008, …

### Python 3 — 57 bytes

```python
a=b=n=1
while[print(b-a>>1)]:a,b=-b,6*b+a-(3*b+a)//n;n+=1
```

**How it works**

- With j = n − k and the Vandermonde step C(n+k, n) = Σᵢ C(k, i)·C(n, i),
  the sum becomes a(n) = Σⱼ 2ʲ·C(n, j)·C(n−1, j−1). By Pascal's rule
  C(n−1, j−1) = C(n, j) − C(n−1, j), so a(n) = D(n, n) − D(n, n−1), where
  D(m, k) = Σⱼ 2ʲ·C(m, j)·C(k, j) are the Delannoy numbers.
- As in [A002002](../A002002/), D(n, n) = 2·D(n, n−1) + D(n−1, n−1) (a path
  to (n, n) ends with an east, north or diagonal step). So with the central
  Delannoy numbers D(n) ([A001850](../../A001xxx/A001850/)),
  a(n) = (D(n) + D(n−1))/2 for n ≥ 1.
- D(n) = 6D(n−1) − D(n−2) − (3D(n−1) − D(n−2))/n (from the generating
  function (1 − 6x + x²)^(−1/2); the division is exact). Here `b` is D(n)
  and `a` holds −D(n−1), so the recurrence reads `6*b+a-(3*b+a)//n` and the
  term is `b-a>>1`.
- n = 0 needs D(−1) = −1, i.e. a = 1: then `a=b=n=1` starts everything with
  one assignment and prints a(0) = (1 − 1)/2 = 0. At n = 1 the recurrence
  gives 6b + a − (3b + a) = 3b, so that value never reaches D(1).

**Notes**

- Keeping D(n−1) with its own sign needs `a=-1;b=n=1` (two bytes more).
- Exact integer arithmetic, so the program is right for every n; a(n) has
  about 0.77n digits, so Python's 4300-digit int-to-str limit stops the
  output near n = 5600.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002003), CC BY-SA 4.0.
