# A002196

> Denominators of coefficients for numerical integration.
> — [OEIS A002196](https://oeis.org/A002196)

Offset 0: 1, 12, 720, 60480, 3628800, 95800320, 2615348736000, …

### Python 3 — 126 bytes

```python
from fractions import*
w=[]
while w:=[y:=Fraction(j:=1,len(w)+1)]+[y:=(y/j-j*x)/(4*(j:=j+1)-2)for x in w]:print(y.denominator)
```

**How it works**

- **Definition used.** These are Salzer's coefficients for integration
  with central differences ([A002195](../A002195/)/A002196 are the
  numerators and denominators in lowest terms). The program uses the
  entry's integral formula (Emeric Deutsch):
  c(n) = (2/(2n+1)!)·∫₀¹ t·∏_(k=1..n) (t² − k²) dt, which reproduces all
  17 listed numerators and all 13 listed denominators (c(1) = −1/12,
  c(2) = 11/720, …).
- **Moments.** With u = t² (so 2t dt = du),
  c(n) = (1/(2n+1)!)·∫₀¹ ∏_(k≤n) (u − k²) du. Let
  I_j(m) = ∫₀¹ u^m·∏_(k≤j) (u − k²) du. Then I₀(m) = 1/(m + 1) and,
  multiplying out the last factor, I_j(m) = I_(j−1)(m+1) − j²·I_(j−1)(m).
  Scaling by the factorial, K_j(m) = I_j(m)/(2j+1)! satisfies
  K_j(m) = (K_(j−1)(m+1)/j − j·K_(j−1)(m))/(4j + 2), since
  (2j+1)! = 2j·(2j+1)·(2j−1)!. The answer is c(n) = K_n(0).
- **Anti-diagonals.** `w` holds K₀(L−1), K₁(L−2), …, K_(L−1)(0) (j + m
  constant). The next diagonal starts with the seed K₀(L) = 1/(L + 1) and
  builds each K_j(L−j) from the entry just made (`y`, moment one higher)
  and the old entry at the same j − 1 (`x`); its last entry is
  K_L(0) = c(L), whose denominator is printed. Each pass adds one term, so
  the output never stops, with exact `Fraction` arithmetic throughout.
- **Golf.** `while w:=[…]:` rebuilds the diagonal in the loop test (it is
  never empty). `Fraction(j:=1,len(w)+1)` resets the counter j while making
  the seed, and `4*(j:=j+1)-2` equals 4j + 2 and advances j at its last
  use, so no `enumerate` is needed. The walrus `y` carries the previous
  entry along the comprehension.

**Notes**

- The b-file is the entry's 13 terms (n = 0 to 12), the bar; they take a
  fraction of a second, and the program prints several hundred terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 126 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002196), CC BY-SA 4.0.
