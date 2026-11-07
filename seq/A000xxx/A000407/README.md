# A000407

> a(n) = (2*n+1)! / n!.
> — [OEIS A000407](https://oeis.org/A000407)

Offset 0: 1, 6, 60, 840, 15120, 332640, 8648640, 259459200, 8821612800, 335221286400, …

### Python 3 — 33 bytes

```python
a=1;k=6
while[print(a)]:a*=k;k+=4
```

**How it works**

- a(n+1)/a(n) = (2n+3)(2n+2)/(n+1) = 4n + 6, so from a(0) = 1 the terms
  are the running products of 6, 10, 14, … . `k` is the next factor:
  `a*=k;k+=4`.
- `print(a)` sits in the loop condition: `[None]` is a non-empty list, so
  the loop never ends, and a(0) is printed before the first update.

**Notes**

- Same length: `a=k=1` with `a*=k+5;k+=4`, and `a=1;k=2` with
  `k+=4;a*=k`. Moving the update into the print would need a start value
  a(−1) = 1/2.
- Exact integer arithmetic, so the program is right for every n. a(n) is
  also 2ⁿ·(2n+1)!!.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. Every printable term appears in about 0.3 s here.
- a(1309) is the first term with more than 4300 digits, so printing stops
  there.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000407), CC BY-SA 4.0.
