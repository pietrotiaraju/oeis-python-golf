# A000680

> a(n) = (2n)!/2^n.
> — [OEIS A000680](https://oeis.org/A000680)

Offset 0: 1, 1, 6, 90, 2520, 113400, 7484400, 681080400, 81729648000, …

### Python 3 — 37 bytes

```python
a=n=1
while[print(a)]:a*=n*n*2-n;n+=1
```

**How it works**

- a(n) = (2n)!/2ⁿ, so a(n) = a(n−1)·(2n)(2n−1)/2 = a(n−1)·n(2n−1), and
  n(2n−1) = 2n² − n is written `n*n*2-n`.
- `a=n=1` starts at a(0) = 1; each pass prints the current term and then
  multiplies in the factor for the next index.

**Notes**

- Exact integer products, nothing else to rely on.
- Python's 4300-digit limit on int-to-str conversion stops the program after
  818 terms, in about a second.
- The b-file has 101 terms; the bar is all 101 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000680), CC BY-SA 4.0.
