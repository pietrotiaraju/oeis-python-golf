# A000440

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-4 places.
> — [OEIS A000440](https://oeis.org/A000440)

Offset 4: 9, 30, 180, 980, 8326, 70272, 695690, 7518720, 89193276, 1148241458, …

The three permutations are the identity, the cyclic shift s and s² (Riordan's
discordant permutations). Call i a hit of p when p(i) − i ∈ {0, 1, 2}
(mod n); a(n) counts the permutations of Z_n with exactly 4 hits.
[A000183](../A000183/) is the case of no hit.

### Python 3 — 150 bytes

```python
n=f=3
while n:=n+1:a=B=n**n;b=3;c=B+2;exec("a,b,c=b,c,(B+2)*c+B*b-a;"*n);print(sum(-~b//B**j%B*(f:=f*j or 1)*(B-1)**(n-j)for j in range(n+1))//B**4%B)
```

**How it works**

- The hits lie on the board of cells (i, i + d mod n), d = 0, 1, 2. If r_K
  is its K-th rook number (ways to put K non-attacking rooks on it), then
  inclusion–exclusion gives the hit polynomial
  H(y) = Σ_p y^(hits of p) = Σ_K r_K·(n−K)!·(y−1)^K (Riordan 1958, ch. 7;
  Stanley, EC1 §2.4), and a(n) is its y⁴ coefficient. This is the formula
  of Margolius on the OEIS page.
- Rook polynomial. Scan the rows i = 0, …, n−1 and keep as state which of
  the columns i, i+1 the rows i−1, i−2 have taken (column i+2 is out of
  their reach). Row i puts no rook, or a rook in column i or i+1 if free,
  or in column i+2. With weight t per rook this is a 4×4 transfer matrix
  T, and since the state at row n is the state at row 0 again (around the
  circle), R_n(t) = Σ_K r_K t^K = tr Tⁿ for n ≥ 3. The characteristic
  polynomial of T is (λ − t)(λ³ − (1+2t)λ² − tλ + t³), so R_n(t) is tⁿ
  plus the n-th power sum of the roots of the cubic; this agrees with
  Margolius's generating function (row n of
  [A061702](https://oeis.org/A061702)).
- The program keeps the reversed polynomial R*_n(t) = tⁿR_n(1/t) =
  Σ_K r_K t^(n−K). With ν = tμ the cubic becomes ν³ − (t+2)ν² − tν + 1,
  so R*_n = 1 + P_n, where P_q is the q-th power sum of its roots. The
  P_q obey P_q = (t+2)P_{q−1} + tP_{q−2} − P_{q−3} for every integer q,
  and P_{−1} = Σ 1/ν = t (the roots multiply to −1 and their pairwise
  products add up to −t), P_0 = 3, P_1 = t+2. So `a=B=n**n;b=3;c=B+2`
  are these three values at t = B, n steps of `a,b,c=b,c,(B+2)*c+B*b-a`
  leave P_n in `b`, and `-~b` is R*_n(B). In the forward direction the
  cubic has a t³ term and P_{−1} = 1/t² is not an integer.
- Packing. B = nⁿ, and r_K ≤ C(n,K)·3^K (choose K rows, then one of the
  three cells in each); these bounds add up to 4ⁿ, so each r_K < 4ⁿ ≤ B
  for n ≥ 4. Hence the base-B digits of R*_n(B) are the rook numbers
  without carries, and `-~b//B**j%B` is r_{n−j}.
- The sum is H(B) = Σ_j r_{n−j}·j!·(B−1)^(n−j). Its coefficients in y are
  the numbers of permutations with i hits: they are non-negative, add up
  to n!, and at least two are nonzero, so each is below n! ≤ nⁿ = B. So
  H(B) also has them as base-B digits, and `//B**4%B` is the one for
  four hits.
- `(f:=f*j or 1)` is the running factorial j!: `f*0 or 1` restarts it at
  1 for every n, so the initial value of `f` does not matter (`n=f=3`
  only defines it). Writing the digit first, `-~b//B**j%B*…`, needs no
  parentheses because `//`, `%` and `*` group left to right.
- `exec("…"*n)` runs the n steps on the same line as the rest, so the
  whole loop body follows `while n:=n+1:` (n = 4, 5, …).

**Notes**

- Same machinery for the siblings: [A000476](../A000476/) (1 hit),
  [A000470](../A000470/) (5), [A000492](../A000492/) (6),
  [A000500](../A000500/) (7) change only the digit and the start.
- Measured alternatives: the n steps as a `for _ in" "*n:` line, 157 bytes;
  `from math import*` with `perm(j)` for j!, 160; the sign-and-binomial
  form `perm(j)*comb(n-j,4)*(-1)**(n-j)` instead of evaluating H at B, 163;
  keeping R*_q itself in the state (seeds t+1, 4, t+3 and an extra −2t in
  each step), 156; the forward polynomial R_n with a correction list for
  the first steps and `(f:=f*(n+k)or 1)` over k in range(−n, 1), 196.
- Exact integer arithmetic, so the program is right for every n ≥ 4.
- About 150 terms in 60 s here. The b-file has 19 terms (up to a(22)); the
  bar is the whole b-file in 60 s.
- a(n) < n!, which reaches 4300 digits only near n = 1750, far beyond what
  the program prints in practice, so the int-to-str limit does not matter.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 240 | first entry |
| 2026-11-06 | Python 3 | 236 | use the three-cells-per-row bound for the packing base |
| 2026-11-06 | Python 3 | 228 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-07 | Python 3 | 150 | reversed rook polynomial by power sums, hit polynomial evaluated at B = nⁿ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000440), CC BY-SA 4.0.
