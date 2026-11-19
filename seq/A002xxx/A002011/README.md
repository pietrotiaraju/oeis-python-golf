# A002011

> a(n) = 4*(2n+1)!/n!^2.
> — [OEIS A002011](https://oeis.org/A002011)

Offset 0: 4, 24, 120, 560, 2520, 11088, 48048, 205920, 875160, 3695120, …

### Python 3 — 39 bytes

```python
a=k=4
while[print(a)]:a=4*a+8*a//k;k+=4
```

**How it works**

- a(n)/a(n−1) = (2n + 1)·2n/n² = 4 + 2/n, so
  a(n) = 4a(n−1) + 2a(n−1)/n, and 2a(n−1)/n = a(n) − 4a(n−1) is an
  integer: the floor division is exact.
- The loop keeps k = 4n instead of n, so the step is `a=4*a+8*a//k;k+=4`
  and both variables start at 4: `a=k=4`.

**Notes**

- Keeping n itself (`a=4;n=1`, `a=4*a+2*a//n;n+=1`) is two bytes longer;
  `4*(2*n+1)*comb(2*n,n)` with an import is longer still.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 7140.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002011), CC BY-SA 4.0.
