# A001961

> A Beatty sequence: floor(n * (sqrt(5) - 1)).
> — [OEIS A001961](https://oeis.org/A001961)

Offset 1: 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, …

### Python 3 — 48 bytes

```python
t=3;j=2
while[print(t-2)]:j+=2;t-=~(t*(t+j)<j*j)
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
  This sequence is u₀(n) for k = 4: with A = 2 + √5,
  α = 1 + 1/A = √5 − 1 ≈ 1.236 and m = 4n,
  a(n) = ⌊nα⌋ = ⌊mα/4⌋. This is the title's ⌊n(√5 − 1)⌋.
- **One step at a time.** x(n) = mα/4 grows by α per term and
  1 < α < 2, so u(n) is u(n − 1) + 1 or u(n − 1) + 2, the larger
  exactly when the candidate t = u(n − 1) + 2 is ≤ x(n). The loop keeps
  t, not u, and `t-=~(test)` adds 1 + test (~False = −1, ~True = −2).
- **No square root.** α is the positive root of α² + 2α − 4 = 0, so x(n)
  is the positive root of 4X² + 2mX − m². The other root is not positive,
  so for t > 0 the candidate is below x(n) exactly when 2t(2t + m) < m².
  Equality never happens, because x(n) is irrational for
  m > 0 (5 is not a square).
- **Halving m.** Here m = 2j is even, so the test can be divided by 4:
  with u = ⌊j(√5 − 1)/2⌋ = ⌊j/φ⌋ (φ the golden ratio), x = j/φ is the
  positive root of X² + jX − j², and for t > 0 the candidate is below it
  exactly when t(t + j) < j²: `t*(t+j)<j*j`, with `j+=2` per term.
- The loop starts at n = 1: u(1) = 1, so t = 3 and j = 2; it prints
  t − 2. (In the notation of A005206, a(n) = G(2n − 1).)

**Notes**

- Exact integer arithmetic, with no floats or square roots, so the
  program is right for every n. The title states the formula itself; Connell's
  Theorem 2 only links it to his game.
- `~` on a bool raises a DeprecationWarning (on stderr) from Python 3.12
  on; the value is still −1 or −2.
- The whole b-file (10000 terms) comes in about a tenth of a second; the
  bar is the whole b-file in 60 s.
- `math.isqrt(5*n*n)-n` makes 54 bytes.
- The same loop, with other constants, gives all of Connell's
  sequences here: k = 2: [A001951](../A001951/), [A001952](../A001952/),
  [A001953](../A001953/), [A001954](../A001954/); k = 3:
  [A001956](../A001956/)–[A001960](../A001960/); k = 4:
  [A001961](../A001961/)–[A001968](../A001968/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001961), CC BY-SA 4.0.
