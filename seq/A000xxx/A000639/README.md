# A000639

> Number of alkyl benzenes with n carbon atoms: C(n)H(2n-6).
> — [OEIS A000639](https://oeis.org/A000639)

Offset 1: 0, 0, 0, 0, 0, 1, 1, 4, 8, 22, …

### Python 3 — 197 bytes

```python
m=2
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((V[1]**6+4*V[2]**3+2*V[3]**2+3*(V[1]*V[2])**2+2*V[6])*X**7//X**m%X//12);m+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6. The
  six ring positions carry radicals up to the dihedral group D₆:
  **a(n) = [x^(n−6)] (B⁶ + 4B(x²)³ + 2B(x³)² + 3B²B(x²)² + 2B(x⁶))/12**,
  the entry's formula.
- The series are packed into integers in base X = 9^m, as on the
  [A000602](../A000602/) page: `V[k]` is B(x^k) evaluated at X and cut
  below X^m, so `V[2*k]`, `V[3*k]` are B(x^(2k)), B(x^(3k)) with no
  substitution, and the padding entries `+P` (k ≥ m) are 1, which is right
  modulo x^m. Each pass applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by
  X^k before the cut keeps only digits of degree < m, all multiples of 6,
  so `//6` is exact digit by digit. Each pass fixes at least one more
  digit, and there are more than m passes.
- m = n + 1, and the D₆ sum is multiplied by X⁷ so that digit m of the
  product is digit n − 6 of the sum, 12aₙ (zero for n < 6); `//12`
  gives aₙ.

**Notes**

- Base width: a tree with child counts at most 3 is fixed by its child
  counts in preorder, so Bⱼ ≤ 4^(j−1) for j ≥ 1, and the update digits
  are at most 6Bₘ₋₁ < 9^m. With B ≤ 1/(1 − 4x) coefficientwise the
  read digits are at most 12·[x^(j−6)](1 − 4x)^(−6), far below 9^m.
  Carries from higher digits only move up.
- Each term is recomputed from scratch with integers of about 3m² bits.
- The reference file has the 100 terms of the OEIS b-file;
  the bar is 40 terms in 60 s (it printed 50 terms in 60 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 197 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000639), CC BY-SA 4.0.
