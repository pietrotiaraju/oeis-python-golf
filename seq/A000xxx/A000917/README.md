# A000917

> a(n) = (2n+3)!/(n!*(n+2)!).
> — [OEIS A000917](https://oeis.org/A000917)

Offset 0: 3, 20, 105, 504, 2310, 10296, 45045, 194480, 831402, 3527160, 14872858, 62403600, …

### Python 3 — 44 bytes

```python
b=k=1
while 1:k+=1;b=4*b-2*b//k;print(b*k-b)
```

**How it works**

- (2n+3)!/(n!(n+2)!) = (n+1)·(2n+3)!/((n+1)!(n+2)!) = (n+1)·C(2n+3, n+1).
- With k = n+2, b = C(2k−1, k−1) is half the central binomial coefficient
  C(2k, k), and b(k)/b(k−1) = (4k−2)/k = 4 − 2/k. So `b=4*b-2*b//k`:
  2b/k = 4b − b(k) is an integer, so the floor is exact. The term is
  (k−1)·b = `b*k-b`.
- The loop starts one step early, at k = 1 with b = C(1, 0) = 1, so the
  start is the single chain `b=k=1`; the print comes after the update, so
  the first line is k = 2: 1·C(3, 1) = 3.

**Notes**

- Other versions: printing in the loop header needs the start `b=3;k=2`,
  45 bytes; `math.comb(2*n+3,n+1)*-~n` in a counting loop is 59.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms; they print at once. The bar is the whole
  b-file in 60 s. a(7138) is the first term with more than 4300 digits, so
  printing stops there with a ValueError (about 1.3 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000917), CC BY-SA 4.0.
