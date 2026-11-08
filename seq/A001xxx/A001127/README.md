# A001127

> Trajectory of 1 under map x->x + (x-with-digits-reversed).
> — [OEIS A001127](https://oeis.org/A001127)

Offset 0: 1, 2, 4, 8, 16, 77, 154, 605, 1111, 2222, 4444, 8888, …

### Python 3 — 40 bytes

```python
x=1
while[print(x)]:x+=int(str(x)[::-1])
```

**How it works**

- Reverse and add: `int(str(x)[::-1])` is x with its digits reversed
  (`int` drops the leading zeros that trailing zeros become), added to x
  each step. The OEIS keeps going after palindromes (1111, 2222, …), and so
  does the program.

**Notes**

- The terms gain about 0.4 digits per step; the whole b-file (1001 terms)
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001127), CC BY-SA 4.0.
