# A001966

> v-pile counts for the 4-Wythoff game with i=2.
> — [OEIS A001966](https://oeis.org/A001966)

Offset 0: 2, 7, 13, 18, 23, 28, 34, 39, 44, 49, 54, 60, 65, 70, 75, …

### Python 3 — 51 bytes

```python
w=8;j=1
while[print(w-6)]:j+=2;w+=5+(w*(3*j-w)>j*j)
```

**How it works**

- **The game.** In I. G. Connell's *k*-Wythoff game (A generalization of
  Wythoff's game, Canad. Math. Bull. 2 (1959), 181–190) a move takes the
  same number of matches from both piles or a positive multiple of *k*
  matches from one pile, and a player who cannot move loses. With
  A = (k + √(k² + 4))/2 Connell defines, for i = 0, …, k − 1 and n ≥ 0,
  uᵢ(n) = ⌊(n + i/k)(1 + 1/A)⌋ and vᵢ(n) = ⌊(n + i/k)(1 + A)⌋, and his
  Theorem 2 says that the winning pairs (the positions where the player
  who just moved wins) are exactly the pairs (uᵢ(n), vᵢ(n)).
  This sequence is v₂(n) for k = 4: with A = 2 + √5, 1 + A = 3 + √5 = 2φ²
  (φ the golden ratio), so a(n) = ⌊(n + 1/2)(3 + √5)⌋ = ⌊jφ²⌋ with
  j = 2n + 1; it is also [A001950](../A001950/)(2n + 1).
- **One step at a time.** jφ² grows by 2φ² ≈ 5.236 per term, so a(n) is
  a(n − 1) + 5 or a(n − 1) + 6, the larger exactly when the candidate
  w = a(n − 1) + 6 is ≤ jφ².
- **No square root.** φ² and 1/φ² are the roots of X² − 3X + 1, so jφ²
  and j/φ² are the roots of X² − 3jX + j². The candidate lies above the
  small root (w > (j − 2)φ² + 5 > j/φ²), so it is below jφ² exactly when
  w² − 3jw + j² < 0: `w*(3*j-w)>j*j`. Equality would make φ² rational.
- The loop starts from a(0) = ⌊φ²⌋ = 2, so w = 8 and j = 1; `j+=2` comes
  before the test, and it prints w − 6.

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n. Connell's Theorem 2 is needed only to match the
  formula with the game in the title; the formula itself is computed
  exactly.
- The whole b-file (10001 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `3*j+math.isqrt(5*j*j)>>1` makes 59 bytes, and the loop of
  [A001965](../A001965/) printing `t+2*j-2` makes 52.
- The same loop, with other constants, gives all of Connell's
  sequences here: k = 2: [A001951](../A001951/), [A001952](../A001952/),
  [A001953](../A001953/), [A001954](../A001954/); k = 3:
  [A001956](../A001956/)–[A001960](../A001960/); k = 4:
  [A001961](../A001961/)–[A001968](../A001968/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001966), CC BY-SA 4.0.
