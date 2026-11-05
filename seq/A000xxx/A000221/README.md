# A000221

> Take sum of squares of digits of previous term; start with 5.
> — [OEIS A000221](https://oeis.org/A000221)

Offset 1: 5, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58, 89, …

### Python 3 — 49 bytes

```python
n=5
while[print(n)]:n=sum(d*d%96for d in b'%d'%n)
```

**How it works**

- The program applies the definition: each new `n` is the sum of the squares
  of the digits of the old one. It does not rely on the orbit being
  periodic, so it is right for every n.
- `b'%d'%n` is the decimal expansion of `n` as a `bytes` object, and
  iterating over it gives the ASCII codes c = 48 + d of the digits d.
- c² − d² = (c − d)(c + d) = 48(2c − 48) = 96(c − 24), so c² ≡ d² (mod 96).
  Since d² ≤ 81 < 96, `d*d%96` (here `d` is the code c) is exactly the square
  of the digit.
- `96for` makes CPython 3.12 print a `SyntaxWarning` (invalid decimal
  literal) on stderr; the program runs normally.
- `while[print(n)]:` prints in the loop test: `[None]` is a non-empty list,
  so the loop never ends.

**Notes**

- This is the program of [A000218](../A000218/) (start 3) with the start
  changed to 5. From 5 the orbit is 5 → 25 → 29 → 85 → 89 → 145 → 42 → 20
  → 4 → 16 → 37 → 58 → 89, so after four terms it runs round the 8-cycle
  89, 145, 42, 20, 4, 16, 37, 58 (Porges 1945).
- The byte table of [A000216](../A000216/) (`n=b'…'[n%53%9]`, the map
  stored on the orbit) does not pay here. The 12 orbit points have 11
  different successors (only 85 and 58 share one, 89), and 145 has to be
  written `\x91`, so the table is at least 14 bytes; to beat 49 bytes,
  index and table together would have to fit in 21 bytes, so a 7-byte
  index that sends the 12 points into 11 slots. An exhaustive search over
  all index expressions of up to 7 characters (up to three operators among
  `% * // + - >> << & ^ | **`, constants of any length that fits, `-n`
  and `~n`, negative indices allowed; 8.5 million expressions) found none.
  The best overall, `864//n%16` with a 15-byte table, gives 54 bytes.
- Storing the terms instead and walking a position `i` through them
  (`while[print(b'…'[i])]:i=…`) costs the same frame, but needs all 12
  terms (15 bytes) and a step of at most 6 characters whose orbit has a
  4-step tail into an 8-cycle; the same search over all steps of up to 6
  characters (465 thousand expressions) found none.
- A growing queue, `l=[*b'…']` / `for x in l:print(x);l+=l[-8],`, is 53
  bytes.
- The b-file has 100 terms and the program prints them at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000221), CC BY-SA 4.0.
