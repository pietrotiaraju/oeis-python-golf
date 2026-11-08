# A000965

> Numerators of expansion of e.g.f. sinh(x) / sin(x) (even powers only).
> — [OEIS A000965](https://oeis.org/A000965)

Offset 0: 1, 2, 4, 104, 272, 3104, 79808, 631936, 1708288, 7045156352, 1413417032704, …

### Python 3 — 135 bytes

```python
from math import*
F=[];P=k=1
while 1:X=P-sum(comb(k,j)*F[j]for j in range(k-1));F=[-e*k for e in F]+[-X,0];P*=k;print(X//gcd(X,P));k+=2
```

**The recurrence**

Write sinh x / sin x = Σ b(m)·x²ᵐ/(2m)!; a(m) is the numerator of b(m)
in lowest terms (the OEIS formula: numerator of (2m)! times the
coefficient), so b = 1, 2/3, 4/3, 104/21, 272/9, …

Take the coefficient of x²ᵐ⁺¹/(2m+1)! in T(x)·sin x = sinh x. The
derivatives of sin at 0 are 0, 1, 0, −1, …, so

Σ_{j ≤ m} (−1)ᵐ⁻ʲ·C(2m+1, 2j)·b(j) = 1,

and the j = m term is (2m+1)·b(m). Hence

b(m) = (1 − Σ_{j<m} (−1)ᵐ⁻ʲ·C(2m+1, 2j)·b(j)) / (2m+1),

and by induction b(j)·(2m+1)!! is an integer for every j ≤ m, where
(2m+1)!! = 1·3·5⋯(2m+1).

**How it works**

- `k` = 2m+1 and `P` = (2m−1)!! before the step. `F` holds the integers
  (−1)ᵐ⁻ʲ·b(j)·P at the even places 2j, with 0 at the odd places, so the
  list index is the binomial's lower index and `comb(k,j)` needs no `2*`
  (the zeros add nothing).
- `X=P-sum(…)` is then P·(2m+1)·b(m) = (2m+1)!!·b(m), an integer.
- For the next m every sign flips and the scale grows by k:
  `F=[-e*k for e in F]+[-X,0]` (the new entry has sign (−1)¹), and
  `P*=k`. Now b(m) = X/P, so its numerator is `X//gcd(X,P)` (b(m) > 0,
  since x/sin x and sinh x/x have positive coefficients).

**Notes**

- Exact integer arithmetic, correct for every n.
- `fractions.Fraction` with the same recurrence costs the second import,
  `Fraction(k)` and `.numerator`: over 160 bytes. Indexing `F` by j with
  `comb(k,2*j)` and `range(k//2)` is 1 byte longer than the zero padding.
- Step m does m binomials on numbers of thousands of digits: 918 terms
  print in about a minute, and then a(918) has more than 4300 digits, so
  `str()` stops the program with a `ValueError` (Python 3.11+ limit).
- The b-file has 101 terms (n = 0 to 100); they print in 0.1 s. The bar
  is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 135 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000965), CC BY-SA 4.0.
