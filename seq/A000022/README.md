# A000022

> Number of centered hydrocarbons with n atoms.
> — [OEIS A000022](https://oeis.org/A000022)

Offset 0: 0, 1, 0, 1, 1, 2, 2, 6, 9, 20, 37, 86, 181, 422, 943, 2223, …

### Python 3 — 247 bytes

```python
n=X=0
while[print(X)]:n+=1;B=1<<9*n+9;M=B**-~n;V=[1]*5*n;S=0;exec('a=V[1];V[:n+1]=[1+B**k*((V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6)for k in range(n+1)];S+=(V[1]-a)*(V[1]-1);'*-~n);f,g,t,q=V[1:5];X=(B*((f**4+6*f*f*g+8*f*t+3*g*g+6*q)%M//24)-S)%M//B**n
```

**How it works**

The count is over carbon skeletons (trees with all degrees ≤ 4) whose
center is a single atom. It follows the method of Rains and Sloane,
[On Cayley's enumeration of alkanes](https://arxiv.org/abs/math/0207176),
the one behind the Mathematica program on the entry:

- Let T_h(x) count rooted ternary trees of height ≤ h, the empty tree
  included, by number of nodes. Then T₋₁ = 1 and
  **T_h = 1 + x·S₃(T_{h−1})**, where S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6
  is the cycle index of S₃ (three unordered branches).
- A centered tree, rooted at its center, is a carbon with four unordered
  branches of which at least two reach the greatest height h. All carbons
  with four branches give x·S₄(T), with S₄(F) = (F⁴ + 6F²F(x²) + 8F·F(x³)
  + 3F(x²)² + 6F(x⁴))/24. The bad ones have one branch of height exactly h,
  counted by T_h − T_{h−1}, and three below it, counted by S₃(T_{h−1}) =
  (T_h − 1)/x. So

  **a(x) = x·S₄(T) − Σ_{h≥0} (T_h − T_{h−1})(T_h − 1),**

  which needs no separate cycle index for the subtracted part.
- Power series are packed into big integers (Kronecker substitution): x
  becomes B = 2^(9n+9), wide enough for every coefficient up to degree n,
  and `%M` with M = B^(n+1) cuts the series at xⁿ. `V[k]` holds
  T_h(x^k), so `V[2*k]` and `V[3*k]` are F(x²) and F(x³) without any
  substitution; entries with k > n stay 1, which is right modulo x^(n+1).
- The divisions by 6 and 24 come after `%M`: the cut series has
  coefficients divisible by 6 (or 24), while the digits above xⁿ are
  incomplete and would spoil the floor division.
- `exec('…'*-~n)` runs the update n + 1 times (h = 0…n, more than the
  height of any tree with n atoms), and `S` collects the subtracted sum.
  `a` keeps the old T_h(x) for the difference.
- The final `B*` multiplies by x, `-S` subtracts, and `%M//B**n` reads off
  the coefficient of xⁿ. Everything is recomputed from scratch for each n.
- `while[print(X)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true. Printing `X` before computing it gives a(0) = 0.

**Golf tricks**

- `-~n` is n + 1, so `B**-~n` and `'…'*-~n` need no parentheses.
- `V=[1]*5*n` is long enough for index 3n and for `V[1:5]` when n = 1.
- The slice assignment `V[:n+1]=[…]` updates T_h(x^k) for k ≤ n in place.

**Notes**

- The program prints 40 terms in about 16 s and 49 in a minute; the bar is
  40 terms in 60 s. The b-file has 61 terms.
- Coefficients of T grow like 2.82ⁿ and those of the products stay far below
  2^(9n+9), so B is wide enough for every n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 247 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000022), CC BY-SA 4.0.
