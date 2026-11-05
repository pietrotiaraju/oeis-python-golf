# A334244

> Decimal representation of n-th iteration of the one-dimensional cellular
> automaton defined by Rule 950, based on the 4-celled von Neumann
> neighborhood starting with a single black cell.
> — [OEIS A334244](https://oeis.org/A334244)

Offset 1: 1, 15, 81, 959, 5185, 61391, 331857, 3929023, 21238849, …

Each cell of the next row is bit k of 950 = 1110110110₂, where k is the
4-bit number written by four neighbouring cells of the current row, so the row
grows by three cells a step. Read as a binary number s, the next row has bit j
equal to bit `s*8>>j&15` of 950. The rows, in binary:

```
1
1111
1010001
1110111111
1010001000001
1110111111001111
1010001000001010001
```

### Python 3 — 46 bytes

```python
x=4
while[print((674+x%3*622)*x//4095|1)]:x*=8
```

**How it works**

- Row n has 3n − 2 cells and follows a fixed pattern:
  - n odd: `1`, then the first 3n − 3 digits of `010001000001` repeated;
  - n even: `1110`, then the first 3n − 6 digits of `111111001110`
    repeated, with the last digit set to 1.
- Read as binary fractions, `1.010001000001…` is 5184/4095 and
  `1110.111111001110…` is 61376/4095. Taking the first 3n − 2 digits gives
  **a(n) = ⌊M·8ⁿ/4095⌋**, with M = 648 for odd n and M = 959 for even n, and
  `|1` sets the last digit, which is always 1.
- x = 2³ⁿ⁻¹ = 8ⁿ/2, starting at 4. Its residue mod 3 is 1 for odd n and 2
  for even n, so `674+x%3*622` is 1296 = 2·648 or 1918 = 2·959, and
  multiplied by x it gives M·8ⁿ.
- `while[print(...)]:` prints in the loop condition (`[None]` is true).

**Why the pattern holds for every n**

- Each cell of row n + 1 depends on four neighbouring cells of row n. In the
  middle of the row those are in the repeating part and depend only on the
  position mod 12; near either end they see the fixed start or the end of the
  row. The row grows by 3 cells a step, so the end comes back to the same
  place in the period every 4 rows.
- Row n + 4 is therefore row n with 12 more cells of the period in the middle,
  and the step from row n + 4 to n + 5 is the step from row n to n + 1 with 12
  more cells of the period in the middle. Once the ends are far enough apart
  not to touch the same window (from about n = 10), checking four consecutive
  steps proves every later one. Simulating the automaton gives the pattern for
  every n up to 1000, and the b-file in full.

**Notes**

- The same pattern proves Colin Barker's recurrence in the OEIS entry,
  a(n) = 64a(n−2) + a(n−4) − 64a(n−6): a(n) − 64a(n−2) runs through
  1, 15, 17, −1 forever.
- With x = 8ⁿ the multiplier is `1270-x%3*311`, 47 bytes. A pair of
  variables, `a,b=b,a*64` with `a//4095|1`, is 49. Simulating the automaton
  directly, `s=sum((950>>(s*8>>j&15)&1)<<j for j in range(len(bin(s))+1))`,
  is 80.
- Exact integer arithmetic. a(4763) is the first term with more than 4300
  digits, where Python 3.11+ stops with a `ValueError` from the int-to-str
  limit, which is not counted as a failure.
- The b-file has 1000 terms and prints at once; the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A334244), CC BY-SA 4.0.
