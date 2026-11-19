# A001953

> a(n) = floor((n + 1/2) * sqrt(2)).
> — [OEIS A001953](https://oeis.org/A001953)

Offset 0: 0, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 16, 17, 19, 20, …

### Python 3 — 46 bytes

```python
t=2;m=1
while[print(t-2)]:m+=2;t-=~(2*t*t<m*m)
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
  This sequence is u₁(n) for k = 2: with A = 1 + √2,
  α = 1 + 1/A = √2 ≈ 1.414 and m = 2n + 1,
  a(n) = ⌊(n + 1/2)α⌋ = ⌊mα/2⌋. This is the title's ⌊(n + 1/2)√2⌋.
- **One step at a time.** x(n) = mα/2 grows by α per term and
  1 < α < 2, so u(n) is u(n − 1) + 1 or u(n − 1) + 2, the larger
  exactly when the candidate t = u(n − 1) + 2 is ≤ x(n). The loop keeps
  t, not u, and `t-=~(test)` adds 1 + test (~False = −1, ~True = −2).
- **No square root.** α is the positive root of α² − 2 = 0, so x(n)
  is the positive root of 2X² − m². The other root is not positive,
  so for t > 0 the candidate is below x(n) exactly when 2t² < m²:
  `2*t*t<m*m`. Equality never happens, because x(n) is irrational for
  m > 0 (2 is not a square).
- `m+=2` comes before the test, which is about the new n. The loop
  starts from u(0) = 0, that is t = 2 with m = 1, and prints t − 2.

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n. The title states the formula itself; Connell's
  Theorem 2 only links it to his game.
- `~` on a bool raises a DeprecationWarning (on stderr) from Python 3.12
  on; the value is still −1 or −2.
- The whole b-file (10001 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `math.isqrt(m*m//2)` makes 53 bytes.
- The same loop, with other constants, gives all of Connell's
  sequences here: k = 2: [A001951](../A001951/), [A001952](../A001952/),
  [A001953](../A001953/), [A001954](../A001954/); k = 3:
  [A001956](../A001956/)–[A001960](../A001960/); k = 4:
  [A001961](../A001961/)–[A001968](../A001968/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001953), CC BY-SA 4.0.
