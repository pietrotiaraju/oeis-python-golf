# A000493

> a(n) = floor(sin(n)).
> — [OEIS A000493](https://oeis.org/A000493)

Offset 0: 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, …

### Python 3 — 126 bytes

```python
s=lambda t,d=1:t and t+s(t*d//(d-~d),d+1)
n=j=0
while 1:
 j+=1;p=2*s(S:=2**j)
 while(q:=n*S//(p+8*j))==n*S//p:print(q%-2);n+=1
```

**How it works**

- For n ≥ 1, sin n is strictly between −1 and 1 and never 0, so its floor
  is 0 when sin n > 0 and −1 when sin n < 0, that is, when ⌊n/π⌋ is even or
  odd. So a(n) = −(⌊n/π⌋ mod 2), and `q%-2` is exactly that: Python's `%`
  takes the sign of the divisor, so q % −2 is 0 or −1.
- π comes from Euler's series π/2 = Σ_{k≥0} k!/(2k+1)!! =
  1 + 1/3 + 1·2/(3·5) + …, whose terms satisfy T_k = T_{k−1}·k/(2k+1).
  `s(t)` adds t, then calls itself on ⌊t·d/(2d+1)⌋ (`d-~d` is 2d + 1)
  until the term is 0.
- **Error bound.** Let S = 2^j and t_k the floored terms. Since
  k/(2k+1) < ½, induction gives 0 ≤ T_k − t_k < 2, and since T_k < S/2^k,
  the first zero term t_K has K ≤ j. The loss is then below 2(K − 1) for the
  terms kept (t₀ = S is exact) plus 2T_K < 4 for the tail, so
  s(S) ≤ Sπ/2 < s(S) + 2j + 2. With p = 2s(S) this gives
  p ≤ Sπ < p + 4j + 4 ≤ p + 8j.
- Hence ⌊nS/(p + 8j)⌋ ≤ ⌊n/π⌋ ≤ ⌊nS/p⌋, and when the two floors agree the
  value is certain. The inner loop prints as many n as the current bounds
  settle; otherwise j grows by one, so the bounds get one bit sharper each
  pass.
- n/π is never an integer for n ≥ 1 (π is irrational), so every n is
  settled once S is large enough; n = 0 gives 0 on both sides.

**Notes**

- Same program with the exact bound `4*j+4`: 128 bytes. `print(-(q%2))`
  costs 4 bytes more than `q%-2`. Machin's formula
  π = 16·atan(1/5) − 4·atan(1/239) with an error allowance: 195 bytes.
- Exact integer arithmetic, so the program is right for every n. `s`
  recurses j levels deep; Python's default recursion limit (1000) would
  only bite for an n whose n/π lies within about 2^−990·n of an integer.
- About 3.3 million terms in 60 s here. The b-file has 10001 terms (up to
  a(10000)); the bar is the whole b-file in 60 s, which takes 0.2 s.
- The terms are 0 and −1, so the 4300-digit int-to-str limit never applies.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 210 | first entry |
| 2026-11-06 | Python 3 | 195 | share the Machin summand and remove multiplication by one |
| 2026-11-07 | Python 3 | 126 | Euler's series k!/(2k+1)!! for π, `q%-2` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000493), CC BY-SA 4.0.
