# A335332

> Decimal representation of n-th iteration of the one-dimensional cellular
> automaton defined by Rule 954, based on the 4-celled von Neumann
> neighborhood starting with a single black cell.
> — [OEIS A335332](https://oeis.org/A335332)

Offset 1: 1, 11, 81, 699, 5441, 43723, 349265, 2797243, 22368577, …

Each cell of the next row is bit k of 954 = 1110111010₂, where k is the
4-bit number written by four neighbouring cells of the current row, so the row
grows by three cells a step. Read as a binary number s, the next row has bit j
equal to bit `s*8>>j&15` of 954. The rows, in binary:

```
1
1011
1010001
1010111011
1010101000001
1010101011001011
1010101010001010001
```

### Python 3 — 42 bytes

```python
R=1
while[print(R)]:R=~R&R*8|~(R*4|~R^R*2)
```

**How it works**

- The loop simulates the automaton, but a whole row at a time with bitwise
  operations instead of a cell at a time.
- Bit j of R, 2R, 4R and 8R is the cell at j, j − 1, j − 2 and j − 3 of the
  current row; call them A, B, C, D, so k = 8A + 4B + 2C + D.
- Rule 954 is on for k = 1, 3, 4, 5, 7, 8, 9. With A = 1 (k ≥ 8) that is
  k = 8, 9: B = C = 0. With A = 0 it is every odd k, plus k = 4: D = 1, or
  B = 1 and C = 0. Both cases together are **¬A∧D ∨ ¬C∧(A⊕B)**.
- In Python: `~R&R*8` is ¬A∧D, and `~(R*4|~R^R*2)` is ¬C∧¬(¬A⊕B) = ¬C∧(A⊕B)
  (`~R^R*2` parses as `(~R)^(R*2)`).
- `while[print(R)]:` prints in the loop condition (`[None]` is true).

**Why it is right for every n**

- Each bit of the result depends only on the same bit of R, 2R, 4R and 8R,
  and the formula agrees with bit k of 954 on all 16 values of (A, B, C, D),
  so one step of the loop is one step of the automaton, for any row.
- Below bit 0, 2R, 4R and 8R hold zeros, which are the white cells right of
  the row. Above the row all four are 0, and k = 0 gives 0, so the result is
  a non-negative integer: the next row, nothing more.
- Bit 0 of the next row sees (A, B, C, D) = (1, 0, 0, 0), so it is the new
  rightmost cell, and the integer is the row read in binary.

**Notes**

- A plain lookup of the rule,
  `R=sum((954>>(R*8>>j&15)&1)<<j for j in range(n))` with `n+=3`, is 75 bytes.
- From n = 3 on the rows settle into a fixed shape: `10` repeated, then
  `0010` (n odd) or `1110` (n even) repeated, then one of four endings that
  depend on n mod 4 (checked to n = 4999). That gives
  30a(n) = 5·8ⁿ + 128·2ⁿ − 1558, 5·8ⁿ − 64·2ⁿ + 1438, 5·8ⁿ + 128·2ⁿ − 7222
  or 5·8ⁿ − 64·2ⁿ + 382 for n ≡ 0, 1, 2, 3 (mod 4), and Colin Barker's
  recurrence in the OEIS entry, but four constants and the two first terms
  make that longer than the simulation.
- Same family as [A334244](../../A334xxx/A334244/) (Rule 950).
- Exact integer arithmetic. a(4763) is the first term with more than 4300
  digits, where Python 3.11+ stops with a `ValueError` from the int-to-str
  limit, which is not counted as a failure.
- The b-file has the 22 terms of the entry and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A335332), CC BY-SA 4.0.
