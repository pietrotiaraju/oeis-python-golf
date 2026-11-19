# A001964

> v-pile positions of the 4-Wythoff game with i=1.
> — [OEIS A001964](https://oeis.org/A001964)

Offset 0: 1, 6, 11, 17, 22, 27, 32, 37, 43, 48, 53, 58, 64, 69, 74, …

### Python 3 — 54 bytes

```python
t=2;m=1
while[print(t+m-2)]:m+=4;t-=~(2*t*(2*t+m)<m*m)
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
  This sequence is v₁(n) for k = 4, with A = 2 + √5 and
  1 + A = 3 + √5. Since (1 + A) − (1 + 1/A) = k, v(n) = u(n) + m
  with m = 4n + 1 (Connell's identity (6)), where
  u(n) = ⌊mα/4⌋ and α = 1 + 1/A = √5 − 1 ≈ 1.236.
- **One step at a time.** x(n) = mα/4 grows by α per term and
  1 < α < 2, so u(n) is u(n − 1) + 1 or u(n − 1) + 2, the larger
  exactly when the candidate t = u(n − 1) + 2 is ≤ x(n). The loop keeps
  t, not u, and `t-=~(test)` adds 1 + test (~False = −1, ~True = −2).
- **No square root.** α is the positive root of α² + 2α − 4 = 0, so x(n)
  is the positive root of 4X² + 2mX − m². The other root is not positive,
  so for t > 0 the candidate is below x(n) exactly when 2t(2t + m) < m²:
  `2*t*(2*t+m)<m*m`. Equality never happens, because x(n) is irrational for
  m > 0 (5 is not a square).
- `m+=4` comes before the test, which is about the new n. The loop
  starts with t = 2, m = 1 and prints v = t − 2 + m.

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n. Connell's Theorem 2 is needed only to match the
  formula with the game in the title; the formula itself is computed
  exactly.
- `~` on a bool raises a DeprecationWarning (on stderr) from Python 3.12
  on; the value is still −1 or −2.
- The whole b-file (10001 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `3*m+math.isqrt(5*m*m)>>2` makes 59 bytes.
- The same loop, with other constants, gives all of Connell's
  sequences here: k = 2: [A001951](../A001951/), [A001952](../A001952/),
  [A001953](../A001953/), [A001954](../A001954/); k = 3:
  [A001956](../A001956/)–[A001960](../A001960/); k = 4:
  [A001961](../A001961/)–[A001968](../A001968/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001964), CC BY-SA 4.0.
