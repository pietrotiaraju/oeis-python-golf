# A000216

> Take sum of squares of digits of previous term, starting with 2.
> — [OEIS A000216](https://oeis.org/A000216)

Offset 1: 2, 4, 16, 37, 58, 89, 145, 42, 20, 4, …

### Python 3 — 44 bytes

```python
n=2
while[print(n)]:n=b'\x91:*Y%'[n%53%9]
```

The table holds three raw control bytes (0x04, 0x10 and 0x14) that a browser
does not show. Byte for byte, the second line is

```text
while[print(n)]:n=b'\x91:<04>*<10>Y<14>%'[n%53%9]
```

where `<04>` stands for the single byte 0x04, and so on. With those three
bytes escaped, `n=b'\x91:\4*\20Y\24%'[n%53%9]`, the program is 49 bytes.

**How it works**

- Let S(m) be the sum of the squares of the digits of m. From 2 the orbit is
  2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4, so after the first term the
  sequence runs round the 8-cycle 4, 16, 37, 58, 89, 145, 42, 20 forever
  (Porges 1945). By induction every term is one of these nine numbers, so S
  only has to be known on them, and the table is S restricted to that set:
  nine values of the map, not terms copied from the b-file.
- `n%53%9` sends 2, 4, 16, 37, 58, 89, 145, 42, 20 to the slots
  2, 4, 7, 1, 5, 0, 3, 6, 2. Only 2 and 20 share a slot, and both have
  S = 4, so the table has one byte per distinct successor: slot 0 holds
  S(89) = 145, then S(37) = 58 (`:`), S(2) = S(20) = 4, S(145) = 42 (`*`),
  S(4) = 16, S(58) = 89 (`Y`), S(42) = 20 and S(16) = 37 (`%`). Eight is the
  least possible length, since the eight successors are all different.
- Indexing a `bytes` object gives an `int`, so no `ord` is needed. A bytes
  literal may hold only ASCII, so 145 is written `\x91` (4 bytes); 4, 16 and
  20 go in as raw bytes, which Python accepts inside a literal (only NUL,
  the line breaks, the backslash and the quote are not allowed there).
- `while[print(n)]:` prints in the loop test: `[None]` is a non-empty list,
  so the loop never ends, and the body moves `n` one step along the orbit.

**Notes**

- Computing S itself, `n=2` / `while[print(n)]:n=sum(int(d)**2for d in str(n))`,
  is 51 bytes.
- A `str` table read with `ord` would hold 145 as a raw character, but that
  is 2 bytes in UTF-8 and `ord()` is 5, against 1 for the `b` and 4 for
  `\x91`: the bytes table wins by 2.
- Printing by position (a counter and a table of terms) is longer: a(1) = 2 is
  the only term off the cycle, so the index needs a special case such as
  PARI's `n%8+8^(n<2)`.
- A search over index expressions with one or two operators (`n` op c
  op c with c < 100, or c op `n` op c with c < 1000; negative indices
  allowed) found nothing shorter than `n%53%9` with its eight-byte table:
  next come `n%50%9`, `~n%53%9` (one byte more), then `106%n%9` and
  `267//n%8`; a single `n%k` needs k = 15 and a 15-byte table.
- The b-file has 100 terms and the program prints them at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000216), CC BY-SA 4.0.
