# A000373

> Conjectured dimension of a module associated with the free commutative Moufang loop with n generators.
> — [OEIS A000373](https://oeis.org/A000373)

Offset 1: 0, 0, 1, 8, 44, 214, 1000, 4592, 20888, 94846, 434973, 2042836, 9979086, 51460622, …

### Python 3 — 182 bytes

```python
from math import comb as C
d=[n:=1]
while[print(sum(C(n,p)*C(n-p,k-~k)*(abs(d[k])+C(p+k-1,p))for k in range(1,n)for p in range(n)))]:d+=n*n-sum(C(n,i)**2*d[i]for i in range(n)),;n+=1
```

**The formula**

The terms are Smith's explicit formula (Invent. Math. 67 (1982), Eq. (8.4)),
in the form of Michael Somos's PARI program on the OEIS page:

a(n) = Σ_{k≥1} Σ_{p≥0} n! / (p!·(2k+1)!·(n−p−2k−1)!) · (A_k + C(p+k−1, k−1)),

where A_1 = 0 and A_k = b_k for k ≥ 2, with b_k = 1, 1, 3, 19, 211, …
([A000275](https://oeis.org/A000275)) the coefficients of
1/J₀(2√x) = Σ b_k x^k/k!². (The conjecture that these numbers are Manin's
dimensions was disproved by Grishkov and Shestakov; the sequence is the
formula.)

**How it works**

- `C(n,p)*C(n-p,k-~k)` is the multinomial n!/(p!·(2k+1)!·(n−p−2k−1)!), and
  `k-~k` is 2k+1. Both loops run to n: the terms with p + 2k + 1 > n vanish
  because `math.comb` returns 0 when the lower index is larger.
- **A_k without a special case.** With J(x) = Σ (−1)^j x^j/j!², the series
  Σ A_k x^k/k!² is 1/J − x, so J·(Σ A_k x^k/k!²) = 1 − x·J. Comparing the
  coefficients of x^k/k!² for k ≥ 1 gives Σ_i C(k,i)²·(−1)^(k−i)·A_i =
  (−1)^k·k². For d_i = (−1)^i·A_i that is
  d_k = k² − Σ_{i<k} C(k,i)²·d_i, with d_0 = 1, which is the update
  `d+=n*n-sum(C(n,i)**2*d[i]for i in range(n)),`. It gives d_1 = 0 by
  itself, so no `(k>1)*` is needed.
- `abs(d[k])` = A_k because every b_k is positive: J₀(2√x) =
  Π_m (1 − 4x/j_m²) over the real zeros j_m of J₀, so
  1/J₀(2√x) = Π_m Σ_r (4x/j_m²)^r has positive coefficients.
- d has n entries when a(n) is printed, enough for every k < n.

**Notes**

- Exact integers throughout. The double loop does n² products of
  binomials of up to 1000 digits, so a(n) costs O(n²) big multiplications:
  the program prints 263 terms in 60 s here. The bar is 200; the b-file has
  523 (n = 1 to 523, up to 999 digits, below the 4300-digit str limit).
- Stopping the loops at k ≤ (n−1)/2 and p ≤ n−2k−1 is 4 times faster
  (458 terms in 60 s with the b_k recurrence and `(k>1)*`) but 66 bytes
  longer in that form. Summing p out of the A_k term
  (A_k·C(n,2k+1)·2^(n−2k−1)) is also longer.
- The b_k recurrence b_k = Σ_{j≥1} (−1)^(j+1)·C(k,j)²·b_(k−j) with
  `(k>1)*b[k]` is 4 bytes longer than the d_k form.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 182 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000373), CC BY-SA 4.0.
