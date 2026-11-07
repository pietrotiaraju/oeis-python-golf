# A000456

> Number of permutations of [n] in which the longest increasing run has length 5.
> — [OEIS A000456](https://oeis.org/A000456)

Offset 1: 0, 0, 0, 0, 1, 10, 99, 1024, 11304, 133669, …

A run is a maximal block of consecutive positions whose entries increase.

### Python 3 — 149 bytes

```python
A=[1];B=[1];n=0
while n:=n+1:
 for a,q in(A,5),(B,6):c=1;a+=[sum((c:=c*(n-k+1)//k)*(k%q<2)*(k%q*2-1)*a[-k]for k in range(1,n+1))]
 print(B[-1]-A[-1])
```

**How it works**

- **The formula.** Let R_q(n) count the permutations of [n] whose
  increasing runs all have length below q. Their e.g.f. is
  1/G_q(x) with G_q(x) = Σ_{j≥0} (x^(qj)/(qj)! − x^(qj+1)/(qj+1)!)
  (David and Barton, Combinatorial Chance, 1962; Heinz's formula on
  A008304). The longest run has length exactly 5 when all runs are
  below 6 but not all below 5, so a(n) = R_6(n) − R_5(n).
- **The recurrence.** Comparing e.g.f. coefficients in G_q·(1/G_q) = 1
  gives, for n ≥ 1,
  R_q(n) = Σ_{k=1}^{n} C(n, k)·w_k·R_q(n−k), where w_k = 1 for k ≡ 1,
  −1 for k ≡ 0 (mod q) and 0 otherwise.
- **The code.** `A` and `B` hold R_5(0…n−1) and R_6(0…n−1), both
  starting with R(0) = 1 (two lists: `A=B=[1]` would alias them).
  `a[-k]` is R(n−k). `(c:=c*(n-k+1)//k)` turns C(n, k−1) into C(n, k),
  exact because C(n, k) = C(n, k−1)·(n−k+1)/k is an integer; `c=1`
  resets it for each list. `(k%q<2)*(k%q*2-1)` is w_k: −1 at residue 0,
  1 at residue 1, 0 otherwise. For n < 5 it prints 0, and for n = 5
  only the increasing permutation qualifies, so the first nonzero term
  is 1.
- `while n:=n+1:` steps n and is never false.

**Notes**

- Other versions that print the same terms: `math.comb(n,k)` with
  `import math` instead of the running binomial: 5 bytes longer;
  `((k%q==1)-(k%q<1))` for w_k: 1 byte longer; looping
  `for q,a in enumerate(L,5):` over `L=[[1],[1]]` and printing
  `L[1][-1]-L[0][-1]`, the first version: 166 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 450 terms print in about 0.6 s here; each term costs
  2n big products. The b-file has 450 terms (up to a(450)); the bar is
  the whole b-file in 60 s.
- a(n) is within a small factor of n!, and a(1559) is the first term with
  more than 4300 digits and printing stops there (after about 17 s).
- Related: [A000434](../A000434/) (length 4) and
  [A000467](../A000467/) (length 6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 167 | first entry |
| 2026-11-06 | Python 3 | 166 | import math for a single comb call |
| 2026-11-07 | Python 3 | 149 | running binomial, two named lists |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000456), CC BY-SA 4.0.
