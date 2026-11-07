# A000571

> Number of different score sequences that are possible in an n-team round-robin tournament.
> — [OEIS A000571](https://oeis.org/A000571)

Offset 0: 1, 1, 1, 2, 4, 9, 22, 59, 167, 490, …

By Landau's theorem (1953), a(n) counts the nondecreasing integer sequences
s_1 ≤ … ≤ s_n with Σ_{i≤k} s_i ≥ C(k, 2) for every k and equality at k = n.

### Python 3 — 144 bytes

```python
from math import*
R=[n:=1];B=[]
while[print(R[0])]:B+=sum((-1)**(n+(g:=gcd(j,n)))*comb(2*g-1,g)for j in range(n))//n,;R=[sumprod(B,R)//n]+R;n+=1
```

**How it works**

- **The recursion.** Claesson, Dukes, Franklín and Stefánsson (*Counting
  tournament score sequences*, arXiv:2209.03925, 2022) proved Paul D. Hanna's
  2013 conjecture from the entry:

  a(n) = (1/n) Σ_{k=1}^{n} e(k)·a(n−k),  a(0) = 1,

  where e(k) = A145855(k) is the number of size-k multisets in Z_k with sum
  ≡ C(k, 2) (mod k), equivalently of k-subsets of {1, …, 2k−1} with sum
  divisible by k. Equivalently Σ a(n)xⁿ = exp(Σ e(k)x^k/k).
- **The weights.** Alekseyev (2008) proved
  e(k) = (1/(2k)) Σ_{d|k} (−1)^(k−d) φ(k/d) C(2d, d). The program uses
  C(2d, d) = 2·C(2d−1, d) to drop the 2, and Σ_{d|k} φ(k/d)·F(d) =
  Σ_{j=0}^{k−1} F(gcd(j, k)) (exactly φ(k/d) of the j in 0, …, k−1 have
  gcd(j, k) = d; j = 0 gives gcd k) to drop the divisor loop and the
  totient: e(k) = (1/k) Σ_{j=0}^{k−1} (−1)^(k+g) C(2g−1, g), g = gcd(j, k).
- **The code.** `B` is e(1), …, e(n), oldest first, and `R` is a(n−1), …,
  a(0), newest first, so `sumprod(B,R)` (math, Python 3.12) is exactly
  Σ e(k)·a(n−k). `R=[n:=1]` sets a(0) and n together.
- **Exactness.** Both `//n` divide exactly: the first because e(n) is an
  integer (Alekseyev's identity is exact), the second because the theorem
  gives n·a(n) = Σ e(k)·a(n−k) with a(n) an integer.

**Notes**

- Other versions that print the same terms: `sum(map(int.__mul__,B,R))`
  instead of `sumprod`: 157 bytes; `comb(2*g,g)` with `//2//n`: 145 bytes;
  the divisor sum with a gcd count for φ and a forward-ordered list: 220 bytes.
- Exact integer arithmetic; correctness for every n rests on the theorem of
  Claesson et al. and Alekseyev's formula, both proved.
- The b-file has 1676 terms (up to a(1675)); the bar is 1000 terms in 60 s.
  The whole b-file prints in about 8 s here, and about 3100 terms in 60 s.
- a(n) ~ c·4ⁿ/n^(5/2) has about 0.6·n digits, so the 4300-digit int-to-str
  limit would stop the printing near n = 7160, well past a 60-s run.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 220 | first entry |
| 2026-11-07 | Python 3 | 144 | gcd sum over j for the divisor sum, C(2g−1, g), newest-first list and `sumprod` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000571), CC BY-SA 4.0.
