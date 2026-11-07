# A000476

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-1 places.
> — [OEIS A000476](https://oeis.org/A000476)

Offset 5: 15, 72, 609, 4960, 46188, 471660, 5275941, 64146768, 842803767, 11902900380, …

The three permutations are the identity, the cyclic shift s and s² (Riordan's
discordant permutations). Call i a hit of p when p(i) − i ∈ {0, 1, 2}
(mod n); a(n) counts the permutations of Z_n with exactly one hit.
[A000183](../A000183/) is the case of no hit.

### Python 3 — 147 bytes

```python
n=f=4
while n:=n+1:a=B=n**n;b=3;c=B+2;exec("a,b,c=b,c,(B+2)*c+B*b-a;"*n);print(sum(-~b//B**j%B*(f:=f*j or 1)*(B-1)**(n-j)for j in range(n+1))//B%B)
```

**How it works**

- The program is the one of [A000440](../A000440/) (4 hits) with another
  digit and start; the proofs are on that page. Inclusion–exclusion over
  the board of cells (i, i + d mod n), d = 0, 1, 2, with rook numbers r_K
  gives the hit polynomial H(y) = Σ_K r_K·(n−K)!·(y−1)^K, and a(n) is its
  y coefficient (Margolius's formula on the OEIS page).
- A 4×4 transfer matrix over the columns i, i+1 already taken shows that
  the reversed rook polynomial Σ_K r_K t^(n−K) is 1 + P_n, where P_q is the
  q-th power sum of the roots of ν³ − (t+2)ν² − tν + 1. So
  P_q = (t+2)P_{q−1} + tP_{q−2} − P_{q−3} with P_{−1} = t, P_0 = 3,
  P_1 = t+2: `a=B=n**n;b=3;c=B+2`, then n steps of
  `a,b,c=b,c,(B+2)*c+B*b-a` in `exec`, and `-~b` is the reversed rook
  polynomial at t = B.
- B = nⁿ is a safe base twice: each r_K ≤ C(n,K)·3^K < 4ⁿ ≤ B, so
  `-~b//B**j%B` is r_{n−j}; and the coefficients of H count permutations,
  so each is below n! ≤ B and H(B) = Σ_j r_{n−j}·j!·(B−1)^(n−j) has them
  as base-B digits. `//B%B` is the one for one hit.
- `(f:=f*j or 1)` is the running factorial j!, restarted at 1 by
  `f*0 or 1` for every n; `n=f=4` with `while n:=n+1:` starts at the
  offset n = 5.

**Notes**

- Siblings with the same program: [A000440](../A000440/) (4 hits),
  [A000470](../A000470/) (5 hits), [A000492](../A000492/) (6 hits),
  [A000500](../A000500/) (7 hits). The alternatives measured there (a `for`
  line, `math.perm`, the binomial-sign form, the forward polynomial) are
  about 6 to 46 bytes longer here too.
- Exact integer arithmetic, so the program is right for every n ≥ 5.
- About 144 terms in 60 s here. The b-file has 19 terms (up to a(23));
  the bar is the whole b-file in 60 s.
- a(n) < n!, which reaches 4300 digits only near n = 1750, far beyond what
  the program prints in practice, so the int-to-str limit does not matter.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 232 | first entry |
| 2026-11-06 | Python 3 | 228 | use the three-cells-per-row bound for the packing base |
| 2026-11-06 | Python 3 | 221 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-07 | Python 3 | 147 | reversed rook polynomial by power sums, hit polynomial evaluated at B = nⁿ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000476), CC BY-SA 4.0.
