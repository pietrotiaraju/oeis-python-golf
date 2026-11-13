# A001633

> Numbers with an odd number of digits.
> — [OEIS A001633](https://oeis.org/A001633)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 101, 102, 103, 104, 105, 106, …

### Python 3 — 41 bytes

```python
n=0
while[len(str(n))%2and print(n)]:n+=1
```

**How it works**

- A filter: every n ≥ 0 is tried in order and printed when its decimal
  string has odd length. `len(str(n))%2and print(n)` prints only then; the
  list around it is always true, so the loop never stops.
- 0 counts as a one-digit number, as in the OEIS data (offset 1 starts
  with 0).

**Notes**

- Jumping over whole decades (`n+=1;n*=len(str(n))%2or 10`, so 10 → 100,
  1000 → 10000) avoids trying the even-length numbers but is 46 bytes.
- The filter costs time only on the skipped blocks: the 1000 b-file terms
  (up to 10089) come at once. Correct for every n by definition.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001633), CC BY-SA 4.0.
