# A000297

> a(n) = (n+1)*(n+3)*(n+8)/6.
> — [OEIS A000297](https://oeis.org/A000297)

Offset −1: 0, 4, 12, 25, 44, 70, 104, 147, 200, 264, 340, 429, 532, 650, …

### Python 3 — 39 bytes

```python
m=0
while[print(m*(m+2)*(m+7)//6)]:m+=1
```

**How it works**

- With m = n + 1 the formula is m(m + 2)(m + 7)/6, and m starts at 0 for
  the offset n = −1.
- The division is exact: m and m + 2 have the same parity and m + 7 the
  other, so one factor is even, and m, m + 2, m + 7 ≡ m + 1 cover all three
  residues mod 3.
- `while[print(…)]:` prints at the top of every pass; `[None]` is a
  non-empty list, so the loop never stops on its own.

**Notes**

- Same length with k = n + 2 from 1: `(k*k-1)*(k+6)//6`. Starting at
  n = −1 with `-~n*(n+3)*(n+8)//6` is 42.
- Exact integer arithmetic; the whole b-file (1002 terms) prints in well
  under a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000297), CC BY-SA 4.0.
