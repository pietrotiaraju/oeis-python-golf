# A000372

> Dedekind numbers or Dedekind's problem: number of monotone Boolean functions of n variables, number of antichains of subsets of an n-set, number of elements in a free distributive lattice on n generators, number of Sperner families.
> — [OEIS A000372](https://oeis.org/A000372)

Offset 0: 2, 3, 6, 20, 168, 7581, 7828354, 2414682040998, 56130437228687557907788, …

### Python 3 — 72 bytes

```python
M=0,1
while[print(len(M))]:M=[a-b*~M[-1]for b in M for a in M if a&~b<1]
```

**How it works**

- A Boolean function of n variables is stored as its truth table: an
  integer whose bit x is f(x), for the 2ⁿ points x = 0 … 2ⁿ − 1. It is
  monotone when x ⊆ y (as bit sets) implies f(x) ≤ f(y).
- Split a function g of n + 1 variables by its last variable: a = g with
  x_{n+1} = 0 and b = g with x_{n+1} = 1. Then g is monotone exactly when a
  and b are monotone and a ≤ b pointwise, that is `a&~b<1`. Its truth
  table is a + b·2^(2ⁿ), because the last variable is the top bit of the
  point index.
- So the initial tuple M of monotone functions of n variables gives the list for
  n + 1 as all such pairs, and `len(M)` is a(n). M = [0, 1] is n = 0: the
  two constants.
- `M[-1]` is the all-ones table 2^(2ⁿ) − 1, the constant 1. It is last for
  n = 0, and the last pair built is (M[-1], M[-1]), the all-ones table of
  the next size. So `-b*~M[-1]` = b·2^(2ⁿ), and `a-b*~M[-1]` puts b above a
  with no carries, 2 bytes under `a|b<<k` with `k=1` and `k*=2`.

**Memory and the loop order**

- After a(6) the program starts on the list for n = 7, which would have
  2 414 682 040 998 entries. With `b` as the outer loop each b adds only
  the functions below it, and the first b in the list are the smallest
  functions (b = 0 adds one entry), so the list grows by almost nothing
  before the timeout. With `a` outside, a = 0 alone would add all 7 828 354
  functions at once and memory would grow by gigabytes per minute.
- The list for n = 6 holds 7 828 354 integers of up to 64 bits: the process
  peaks at about 430 MB.

**Notes**

- Exact integer counting, nothing else: every term printed is right. a(6)
  costs 7581² = 57 million subset tests and appears after about 23 s here;
  a(7) is out of reach for any enumeration. The bar is 7 terms in 60 s; the
  b-file has 10 (n = 0 to 9, a(9) from 2023).
- A version that never builds the 7.8-million list uses
  a(n + 2) = Σ_{a,b} |[a, b]|², the sum over pairs of monotone functions of
  n variables of the squared number of h with a ≤ h ≤ b (split by the
  last two variables, a monotone function of n + 2 variables is
  a ≤ h, g ≤ b with h and g free in between). It
  prints a(6) in 4 s with a few MB, but with `print('2\n3')` in front it is
  139 bytes.
- `a&~b<1`, `a|b==b` and `a&b==a` are the same length; `a|b*-~M[-1]` is 1
  byte longer than `a-b*~M[-1]`, which ends in `]` and needs no space
  before `for`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |
| 2026-11-06 | Python 3 | 72 | use a tuple for the initial M state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000372), CC BY-SA 4.0.
