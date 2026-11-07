# A000625

> Number of n-node steric rooted ternary trees; number of n carbon alkyl radicals C(n)H(2n+1) taking stereoisomers into account.
> — [OEIS A000625](https://oeis.org/A000625)

Offset 0: 1, 1, 1, 2, 5, 11, 28, 74, 199, 551, …

### Python 3 — 118 bytes

```python
from math import*
Q=1,;*C,n=0,
while[print(Q[-1])]:C+=sumprod(Q[::3],r:=Q[::-3]),;Q+=0,0,(sumprod(C,r)+2*Q[n])//3;n+=1
```

**How it works**

- Let T(x) = ΣTₙxⁿ count steric radicals, with T₀ = 1 for the empty
  branch (a hydrogen). The radical carbon carries three branches in a
  cyclic order seen from the free valence; only the rotations (the
  cyclic group C₃) give the same molecule, so Pólya's theorem gives
  **T(x) = 1 + x(T(x)³ + 2T(x³))/3**.
- `Q` holds T spread out with two zeros between terms: Q[3e] = Tₑ.
  Then `Q[::3]` is T₀,…,Tₙ, `Q[::-3]` is the same list backwards, and
  `Q[n]` is the coefficient of xⁿ in T(x³) (zero unless 3 | n), so
  there is no divisibility test.
- `C[n]` caches [xⁿ]T(x)² = `sumprod(Q[::3],r:=Q[::-3])`; the walrus
  keeps the reversed list for the next line, where `sumprod(C,r)` is
  [xⁿ]T(x)³. Then Tₙ₊₁ = ([xⁿ]T³ + 2Tₙ/₃)/3 is appended with its two
  zeros.
- `while[print(Q[-1])]:` prints Tₙ before each step ([None] is true).

**Notes**

- Exact integer arithmetic. The division by 3 is exact: it counts
  orbits, and P(x)³ ≡ P(x³) (mod 3) for every integer polynomial.
- O(n) operations per term. The reference file has the 1931 terms of
  the OEIS b-file; the bar is all 1931 in 60 s (the program needs about
  13 s here). Python's 4300-digit limit for printing integers would
  stop it near n ≈ 8300.
- The same lists give [A000620](../A000620/), [A000622](../A000622/)
  and [A000623](../A000623/); the unrooted count is
  [A000628](../A000628/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000625), CC BY-SA 4.0.
