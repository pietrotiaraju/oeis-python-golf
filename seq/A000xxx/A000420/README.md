# A000420

> Powers of 7: a(n) = 7^n.
> — [OEIS A000420](https://oeis.org/A000420)

Offset 0: 1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=7
```

**How it works**

- n starts at 7⁰ = 1 and is multiplied by 7 after every print, so the k-th
  print is 7^k. The value is the whole state: no exponent counter.
- `while[print(n)]:` prints in the loop condition: `print` returns `None`
  and the one-element list `[None]` is true. This is
  [A000400](../A000400/) with 7 in place of 6.

**Notes**

- `while 1:print(n);n*=7`: 25 bytes. A counter with `print(7**n)`: 27.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(5089) is the first term with more than 4300 digits (4301), so Python's
  int-to-str limit stops the printing there; a(5088) has 4300.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000420), CC BY-SA 4.0.
