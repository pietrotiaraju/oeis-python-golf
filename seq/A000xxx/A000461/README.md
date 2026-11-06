# A000461

> Concatenate n n times.
> — [OEIS A000461](https://oeis.org/A000461)

Offset 1: 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999, 10101010101010101010, …

### Python 3 — 32 bytes

```python
n=0
while 1:n+=1;print(str(n)*n)
```

**How it works**

- Increase n before printing, so the first block is “1”.
  `str(n)*n` repeats the entire decimal text of n exactly n times.
  Multiplying a string means concatenation, not numeric multiplication.
- At n=3 the result is “333”; at n=10 it is ten copies of “10”,
  namely “10101010101010101010”. The code needs no change when
  the block length increases.
- A block starts with a nonzero digit, so the repeated text has no
  leading zero. Printing that text gives exactly the required decimal
  integer representation without constructing the integer itself.

**Notes**

- If d=digits(n), the equivalent numeric formula is
  n·(10^(dn)−1)/(10ᵈ−1). String repetition avoids both these
  powers and their division.
- Each output has exactly n·digits(n) characters. Allocation and
  printing therefore take time proportional to that length, with
  the output string as the main temporary storage.
- The complete output string is never parsed as an integer, so its
  length is not subject to Python's 4300-digit integer conversion
  limit. Compare [A000422](../A000422/) for descending blocks.
- The b-file has 333 terms (indices 1 through 333). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000461), CC BY-SA 4.0.
