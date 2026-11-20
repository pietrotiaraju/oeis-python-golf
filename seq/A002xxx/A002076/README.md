# A002076

> Number of equivalence classes of base-3 necklaces of length n, where necklaces are considered equivalent under both rotations and permutations of the symbols.
> — [OEIS A002076](https://oeis.org/A002076)

Offset 0: 1, 1, 2, 3, 6, 9, 26, 53, 146, 369, 1002, 2685, …

### Python 3 — 117 bytes

```python
import math
print(n:=1)
while[print(sum(3**(g:=math.gcd(k,n))*(6-(d:=n//g)*-d%6)+d%2*3for k in range(n))//6//n)]:n+=1
```

**How it works**

- **Burnside over C_n × S₃.** The 6n pairs (ρᵏ, σ) act on words
  c: Z_n → {0, 1, 2}, and c is fixed by (ρᵏ, σ) when c(i + k) = σ(c(i))
  for all i. Rotation by k splits Z_n into g = gcd(k, n) cycles of length
  d = n/g; along a cycle each letter is σ of the one before, so the cycle
  is fixed by its first letter x, which must satisfy σᵈ(x) = x. So the
  pair fixes (number of fixed points of σᵈ)^g words.
- **Summing over σ.** The identity gives 3^g; each of the three
  transpositions gives 3^g if d is even and 1^g = 1 if d is odd; each of
  the two 3-cycles gives 3^g if 3 | d and 0 otherwise. Together
  3^g·c(d) + 3·[d odd], where c(d) = 1 + 3[2 | d] + 2[3 | d] is the number
  of σ with σᵈ = 1: 6, 1, 4, 3, 4, 1 for d ≡ 0, …, 5 (mod 6).
- So a(n) = (1/6n) Σ_{k=0}^{n−1} (3^g·c(n/g) + 3·[n/g odd]), the
  formula of the OEIS entry with the divisor sum written over k.
- **c(d) in eight bytes.** d² mod 6 runs 0, 1, 4, 3, 4, 1, so
  6 − (−d²) mod 6 runs 6, 1, 4, 3, 4, 1 = c(d): `6-d*-d%6` (Python's `%`
  is never negative here). `d%2*3` adds the transpositions' 1s for odd d.
- `print(n:=1)` prints a(0) = 1 (the empty necklace) and starts the loop
  at n = 1; `while[print(…)]:n+=1` prints a(n) and steps n.

**Notes**

- Exact integer arithmetic; Burnside's sum is a multiple of 6n, so the
  floor divisions are exact, and the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes about 0.15 s.
- [A002075](../A002075/) counts the classes of primitive period n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002076), CC BY-SA 4.0.
