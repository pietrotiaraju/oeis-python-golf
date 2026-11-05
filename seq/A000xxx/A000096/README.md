# A000096

> a(n) = n*(n+3)/2.
> — [OEIS A000096](https://oeis.org/A000096)

Offset 0: 0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, …

### Python 3 — 31 bytes

```python
m=3
while[print(m*m//8-1)]:m+=2
```

**How it works**

- Put m = 2n + 3. Then m² = 4n² + 12n + 9, so n(n+3)/2 = (m² − 9)/8.
- m is odd, so m² ≡ 1 (mod 8) and `m*m//8` is (m² − 1)/8, one more than
  a(n). `-1` takes it back.
- m starts at 3 (n = 0) and steps by 2, so the loop prints a(0), a(1), …
  forever. `while[print(…)]` is always true because `[None]` is a non-empty
  list, as in [A000027](../A000027/).

**Notes**

- Exact integer arithmetic, so it is right for every n.
- The direct formula, `n=0` + `while[print(n*n+3*n>>1)]:n+=1`, is 33 bytes,
  and so is the recurrence a(n) = a(n−1) + n + 1 as `a=0;k=2` +
  `while[print(a)]:a+=k;k+=1`.
- No square of a step-linear m works without the `-1`: if m = kn + c and
  the quotient is m²/d, matching n²/2 + 3n/2 forces d = 2k² and c = 3k/2,
  which leaves the constant c²/d = 9/8 and makes `m*m//d` equal to
  a(n) + 1 every time.
- A brute-force search over every integer expression in `m` of up to 7
  bytes (operators `** * // % + - >> << & ^ |`, unary `-` and `~`,
  constants 0–99), with any start value and any step from −19 to 19, found
  nothing. So the `m=…` / `while[print(…)]:m+=…` shape needs at least the 8
  bytes of `m*m//8-1` (or `m*m-9>>3`).
- The whole b-file (10 001 terms) prints in a fraction of a second; the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000096), CC BY-SA 4.0.
