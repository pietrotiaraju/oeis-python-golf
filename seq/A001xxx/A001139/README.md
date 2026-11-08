# A001139

> Number of stable feedback shift registers with n stages.
> — [OEIS A001139](https://oeis.org/A001139)

Offset 2: 1, 3, 21, 6615, 64595475, …

### Python 3 — 117 bytes

```python
M=3
while 1:
 P=1;R={*range(M//2+1,M)}
 for w in R:S=R&{w*2**i%M for i in R};P*=w<max(S)or~-2**len(S)
 print(P);M-=~M
```

**What is counted**

- The entry has only the title and five terms, from C. L. Liu's 1966 paper
  (not online, not checked here). An n-stage register maps the state
  (x₁,…,xₙ) to (x₂,…,xₙ,f(x₁,…,xₙ)); call it stable when every state runs
  into 0ⁿ. Over all feedback functions f that count is 2^(2ⁿ−n−1)
  (2, 16, 2048, …: spanning trees of the de Bruijn graph, by the BEST
  theorem), so that is not this sequence; neither are the symmetric,
  monotone or threshold f, nor "every cycle is a fixed point".
- What fits the data is feedback of the form f = x₁·g(x₂,…,xₙ): a 1 can
  only enter when a 1 leaves. A brute force over all g gives 1, 3, 21, 6615
  for n = 2…5, and the formula below gives 64595475 for n = 6, so the page
  follows the data with this reading.

**How it works**

- With f = x₁·g the weight never goes up: it drops by one exactly when
  x₁ = 1 and g = 0. A cycle keeps its weight, so along a cycle every bit
  that enters equals the bit that leaves, and the cycle is the rotation
  orbit of a state. Hence the register is stable if and only if every
  nonzero necklace (rotation class of n-bit words) has a rotation 1y with
  g(y) = 0.
- Each y belongs to exactly one word 1y, so g can be chosen necklace by
  necklace: a(n) = Π_C (2^k(C) − 1) over the nonzero necklaces C, where
  k(C) is the number of distinct rotations of C that start with 1. For
  n = 6 that is 3·3²·7³·15²·31 = 64595475 (the 1…1 necklace gives 1).
- With M = 2ⁿ − 1, doubling mod M rotates an n-bit word (other than 1…1)
  by one place, so the rotations of w are w·2^i mod M. `R` is the set of
  words that start with 1, except 1…1, and `S=R&{…}` is the set of
  rotations of w that start with 1, so |S| = k(C). Only the largest one,
  w = max(S), multiplies `P` by 2^|S| − 1 (`~-2**len(S)`); the others
  multiply it by `True`. `M-=~M` steps M to 2M + 1.
- `i` runs over `R` too, saving a `range(n)` (and `n` itself): `R` has
  2ⁿ⁻¹ − 1 ≥ n consecutive values for n ≥ 3, so every rotation shows up;
  for n = 2, R = {2} and the one word 10 is its own only 1-rotation.

**Notes**

- `i` over `R` makes the work about 4ⁿ: 11 terms (up to a(12)) in 60 s
  here. `for w in range(1,M):S={r for i in range(n)if(r:=w*2**i%M)>M/2}…`
  with `n` kept is 131 bytes and much faster. Python's 4300-digit
  int-to-str limit would stop either one at a(15) (4918 digits).
- The next terms are a(7) = 646749185523721875 and
  a(8) = 1045578483705985916072727189343359375.
- The b-file has the 5 terms of the entry (a(2) to a(6), synthesized); the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001139), CC BY-SA 4.0.
