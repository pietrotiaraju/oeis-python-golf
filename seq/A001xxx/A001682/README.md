# A001682

> Numbers k such that 3^k, 3^(k+1) and 3^(k+2) have the same number of digits.
> — [OEIS A001682](https://oeis.org/A001682)

Offset 1: 0, 21, 42, 65, 86, 109, 130, 151, 174, 195, 218, 239, 262, 283, …

### Python 3 — 56 bytes

```python
p=1;k=0
while 1:p*=10**(p<=3**k);9*3**k<p!=print(k);k+=1
```

**How it works**

- **The power of ten above 3^k.** p is kept equal to the smallest power of
  10 above 3^k, that is 10^d when 3^k has d digits. It starts at 1, and
  `p*=10**(p<=3**k)` multiplies it by 10 whenever 3^k has caught up. Once is
  enough: before the step p > 3^(k−1), so 3^k < 3p < 10p; and since p only
  grows by 10 when p ≤ 3^k, p/10 ≤ 3^k stays true.
- **The test.** 3^k ≥ 10^(d−1), so 3^(k+1) and 3^(k+2) have at least d
  digits too, and all three have exactly d digits when 3^(k+2) = 9·3^k < p.
- **The chain.** In `9*3**k<p!=print(k)` the second comparison, and with it
  the `print`, runs only when 9·3^k < p; `p!=None` is then true and thrown
  away.

**Notes**

- Exact integer arithmetic and no `str`, so the 4300-digit limit on
  int-to-str conversion never comes up: correct for every k. Comparing
  `len(str(3**k))` with `len(str(3**k*9))` is 59 bytes and stops with a
  `ValueError` after 413 terms (the last is k = 9002), once 3^(k+2) passes
  4300 digits.
- Keeping x = 3^k in a variable that is tripled every pass is 57 bytes, one
  more than computing `3**k` twice.
- The b-file has 1000 terms (up to k = 21831, where 3^k has 10417 digits);
  the bar is the whole b-file in 60 s, which takes a few seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001682), CC BY-SA 4.0.
