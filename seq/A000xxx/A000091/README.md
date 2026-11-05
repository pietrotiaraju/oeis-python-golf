# A000091

> Multiplicative with a(2^e) = 2 for k >= 1; a(3) = 2, a(3^e) = 0 for
> k >= 2; a(p^e) = 0 if p > 3 and p == -1 (mod 3); a(p^e) = 2 if p > 3 and
> p == 1 (mod 3).
> — [OEIS A000091](https://oeis.org/A000091)

Offset 1: 1, 2, 2, 2, 0, 4, 2, 2, 0, 0, 0, 4, 2, 4, 0, 2, 0, 0, 2, 0, 4, 0, 0, 4, 0, 4, …

### Python 3 — 89 bytes

```python
n=0
while 1:R=range(n:=n+1);print(sum(x*x%n==x for x in R)*any((x*x+3<<n)%n<1for x in R))
```

**How it works**

- Every factor in the definition is 2 or 0. So a(n) = 2^ω(n) (ω = number
  of distinct primes) when n is *allowed*, meaning n = 2ᵃ·3ᵇ·m with b ≤ 1
  and every prime of m ≡ 1 (mod 3). Otherwise a(n) = 0. The program
  multiplies those two parts.
- 2^ω(n) is the number of idempotents mod n. x² ≡ x (mod pᵉ) means
  pᵉ | x(x − 1), and x and x − 1 are coprime, so x ≡ 0 or 1 mod each pᵉ. By
  the Chinese remainder theorem that gives 2^ω(n) residues, which
  `sum(x*x%n==x for x in R)` counts.
- n is allowed exactly when −3 is a square modulo the odd part of n:
  - For a prime p > 3, −3 is a square mod p iff p ≡ 1 (mod 3) (quadratic
    reciprocity), and Hensel's lemma lifts the root to every pᵉ.
  - Mod 3, x = 0 is a root. Mod 9 there is none: x would have to be a
    multiple of 3, so x² ≡ 0, not 6.
- The power of 2 must not count, since any exponent is allowed. `<<n`
  multiplies by 2ⁿ, which covers any 2ᵛ dividing n (2ᵛ ≤ n < 2ⁿ). So
  `(x*x+3<<n)%n<1` holds iff the odd part of n divides x² + 3. Since x runs
  over every residue mod n, it also runs over every residue mod the odd
  part, and `any` gives the 0/1 factor.
- x² + 3 tests the same thing as x² + x + 1 (the congruence of
  [A000086](https://oeis.org/A000086)): the discriminant of x² + x + 1 is
  −3. It is 2 bytes shorter.
- `R=range(n:=n+1)` steps n and names the range once for both
  comprehensions. A walrus cannot be the iterable of a comprehension:
  `for x in(R:=range(n))` is a SyntaxError. The usual
  `n=1` / `while[print(…)]:n+=1` with `range(n)` written twice is 91 bytes.

**Notes**

- Exact integer arithmetic, and the argument above (CRT, reciprocity,
  Hensel) holds for every n. The terms are at most 2^ω(n), far from the
  int-to-str limit.
- Each term costs 2n steps on numbers of about n bits. The whole b-file
  (2000 terms) prints in about 1 s, and about 10 000 terms print in 60 s.
  The bar is the whole b-file in 60 s.
- No single polynomial count works. Counting the roots of one quadratic
  mod n cannot give 2 at every 2ᵉ: that needs a discriminant ≡ 1 (mod 8),
  but the primes p > 3 force a discriminant of −3·k². It also cannot give
  2 roots mod 3 and none mod 9, because two distinct roots mod 3 are simple
  and lift. A computer search over `x in range(K*n)`, modulus `M*n` and
  small coefficients found nothing either.
- Tried and longer: `sum(any(…)for x in R if x*x%n==x)` (+2), `0in{…}`
  instead of `any` (+1, because of the parentheses), and a set of pairs
  `len({x for x in R for y in R if…})` (+3, and quadratic time).

### Python 3 + sympy — 80 bytes

```python
from sympy import*
n=1
while[print(is_quad_residue(-3*4**n,n)<<primenu(n))]:n+=1
```

- The same two parts. `primenu(n)` is ω(n), and `True<<k` is 2ᵏ while
  `False<<k` is 0.
- `is_quad_residue(a,n)` handles composite n: it checks each prime power.
  4ⁿ is a square that is a unit mod the odd part, so the test there is
  "−3 is a square". Mod 2ᵛ the number −3·4ⁿ is 0, which is always a
  square. This is the same test as the plain program's.
- `2**primenu(n)*…` is 82 bytes.
- The whole b-file prints in about 1.5 s, and about 140 000 terms print
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 89 | first entry |
| 2026-11-05 | Python 3 + sympy | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000091), CC BY-SA 4.0.
