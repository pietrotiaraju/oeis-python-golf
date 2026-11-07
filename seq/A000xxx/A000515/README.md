# A000515

> a(n) = (2n)!(2n+1)!/n!^4, or equally (2n+1)*binomial(2n,n)^2.
> — [OEIS A000515](https://oeis.org/A000515)

Offset 0: 1, 12, 180, 2800, 44100, 698544, 11099088, 176679360, 2815827300, 44914183600, …

### Python 3 — 43 bytes

```python
a=n=1
while[print(a)]:a=16*a-4*a//n//n;n+=1
```

**How it works**

- From a(n) = (2n+1)·C(2n, n)² the ratio of consecutive terms is
  a(n)/a(n−1) = 4(2n−1)(2n+1)/n² = 16 − 4/n², so
  a(n) = 16·a(n−1) − 4·a(n−1)/n².
- `4*a//n//n` is exact: 4·a(n−1)/n² = 16·a(n−1) − a(n) is an integer, and
  ⌊⌊x/n⌋/n⌋ = ⌊x/n²⌋ for x ≥ 0. Writing the ratio as 16 − 4/n² saves 5
  bytes over `a*4*(4*n*n-1)//(n*n)`, and `//n//n` is as short as `//n**2`.
- `a=n=1` serves both: `a` is a(0) = 1, printed first, and `n` is the index
  of the term the next update makes (12 = 16 − 4 for n = 1).

**Notes**

- The product form `a=a*4*(4*n*n-1)//n//n` in the same loop: 48 bytes;
  `(2*n+1)*math.comb(2*n,n)**2` with `import math`: 62 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The program stops after a(3571):
  a(n) grows like 16^n, and a(3572) is the first term with more than 4300
  digits, the int-to-str limit of Python 3.11+.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |
| 2026-11-07 | Python 3 | 43 | ratio as 16 − 4/n², `a=n=1` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000515), CC BY-SA 4.0.
