# A000414

> Numbers that are the sum of 4 nonzero squares.
> — [OEIS A000414](https://oeis.org/A000414)

Offset 1: 4, 7, 10, 12, 13, 15, 16, 18, 19, 20, …

### Python 3 — 71 bytes

```python
n=0
while 1:
 m=n=n+1
 while m%8<1:m//=4
 2199560276590>>m&1or print(n)
```

**How it works**

- The positive integers that are not sums of four positive squares are
  1, 3, 5, 9, 11, 17, 29, 41 and 2·4ᵏ, 6·4ᵏ, 14·4ᵏ for k ≥ 0 (Grosswald,
  *Representations of Integers as Sums of Squares*, 1985, Theorem 3 on
  pp. 74–75; quoted in [A000534](../A000534/)).
- Write n = 4ᵏ·u with 4 ∤ u. `while m%8<1:m//=4` divides by 4 only while 8
  divides the number, so it stops at u when k = 0 or u ≡ 2 (mod 4), and
  at 4u when k ≥ 1 and u is odd. The exceptions therefore land exactly on
  E = {1, 2, 3, 5, 6, 9, 11, 14, 17, 29, 41}: 2·4ᵏ, 6·4ᵏ and 14·4ᵏ go to
  2, 6 and 14, and the odd exceptions have k = 0. Every other n lands
  outside E: a multiple of 4 is never in E, u ≡ 2 (mod 4) is in E only if
  u is 2, 6 or 14, and for k = 0 the result is n itself.
- 2199560276590 is Σ_{e∈E} 2ᵉ, so `2199560276590>>m&1` is 1 exactly when
  m ∈ E (for m > 41 the shift leaves 0). `…or print(n)` prints the other n.
- `m=n=n+1` steps n and copies it into m in one statement.

**Notes**

- `m in b'…'` with the eleven values as raw bytes is 1 byte longer and
  needs control characters in the source. A direct search with
  `{n-a-b-c for a in s for b in s for c in s}&s` (the
  [A000408](../A000408/) layout) is 101 bytes but costs about n^1.5 per
  term: 1400 terms in 10 s here. The previous record kept sets of sums of
  one, two and three squares (143 bytes).
- Integer arithmetic; correctness for every n rests on the theorem above.
  The output matches a direct search for every n < 60 000.
- About 70 000 terms in 5 s here. The b-file has 10000 terms (up to
  a(10000) = 10026); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 143 | first entry |
| 2026-11-07 | Python 3 | 71 | Grosswald's exception list as a bitmask |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000414), CC BY-SA 4.0.
