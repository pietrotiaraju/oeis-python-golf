# A001637

> Numbers with an even number of digits.
> — [OEIS A001637](https://oeis.org/A001637)

Offset 1: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, …

### Python 3 — 40 bytes

```python
n=0
while[len(str(n))%2or print(n)]:n+=1
```

**How it works**

- A filter: every n ≥ 0 is tried in order and printed when its decimal
  string has even length: `len(str(n))%2or print(n)` calls print only
  when the length is even. The list around it is always true, so the loop
  never stops.
- The twin of [A001633](../A001633/), with `or` instead of `and`.

**Notes**

- Jumping from 100 straight to 1000 by multiplying is longer than letting
  the filter scan the odd-length block.
- The 1000 b-file terms (up to 1909) come at once. Correct for every n by
  definition.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001637), CC BY-SA 4.0.
