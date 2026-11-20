# A001962

> A Beatty sequence: floor(n * (sqrt(5) + 3)).
> — [OEIS A001962](https://oeis.org/A001962)

Offset 1: 5, 10, 15, 20, 26, 31, 36, 41, 47, 52, 57, 62, 68, 73, 78, …

### Python 3 — 51 bytes

```python
w=5;n=1
while[print(w+3*n-3)]:n+=1;w+=2+(w*w<5*n*n)
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
  This sequence is v₀(n) for k = 4: with A = 2 + √5, 1 + A = 3 + √5, so
  a(n) = ⌊n(3 + √5)⌋, the title.
- **One step at a time.** a(n) = 3n + s(n) with s(n) = ⌊n√5⌋. As
  √5 ≈ 2.236, s(n) is s(n − 1) + 2 or s(n − 1) + 3, the larger exactly
  when the candidate w = s(n − 1) + 3 is ≤ n√5, that is w² ≤ 5n²; equality
  would make √5 rational, so the test is `w*w<5*n*n`.
- The loop keeps w (from s(1) = 2, so w = 5), adds 2 + test, and prints
  a(n) = 3n + w − 3.

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n. Connell's Theorem 2 is needed only for the game
  reading in the OEIS comment; the title is the formula itself.
- The whole b-file (10000 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `3*n+math.isqrt(5*n*n)` makes 56 bytes, and the loop of
  [A001961](../A001961/) printing `t+2*j-2` makes 52.
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
Sequences](https://oeis.org/A001962), CC BY-SA 4.0.
