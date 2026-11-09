# A001171

> From least significant term in expansion of E( tr (X'*X)^n ), X rectangular and Gaussian. Also number of types of sequential n-swap moves for traveling salesman problem.
> — [OEIS A001171](https://oeis.org/A001171)

Offset 1: 1, 1, 4, 20, 148, 1348, 15104, 198144, 2998656, 51290496, 979732224, …

### Python 3 — 219 bytes

```python
f=lambda n:n<1or-n*f(n-1)
k=0
while 1:k+=1;M=f(7*k);print(k*sum(M*(-8)**d*(4*d+2)*f(A:=B+d)**3*f(2*B)**2*f(m:=k+~A-B)*(m or B<1)//((d*d-k*k)*(k*k-~d*~d or 2*k)*f(A-~A)*f(B)**3)for B in range(k)for d in range(k-2*B))//M)
```

**How it works**

- For a p×q matrix X of independent real normal entries, Hanlon, Stanley and
  Stembridge (Theorem 5.4 and Lemma 5.3 of [their 1992
  paper](https://math.mit.edu/~rstan/pubs/pubfiles/92.pdf)) prove
  E tr((X'X)ᵏ) = Σ c_λ(2) F_λ(p) F_λ(q), summed over the partitions
  λ = (a, b, 1ᵏ⁻ᵃ⁻ᵇ) with a ≥ b ≥ 1, and λ = (k). Every F_λ(x) has the factor x,
  so the coefficient of pq is t_k = Σ c_λ(2) ([x]F_λ)², the formula printed at
  the end of their Section 5 (p. 168). That is a(k).
- Written out with d = a−b, A = a−1, B = b−1 and m = k−a−b+1 (so
  A+B+m = k−1), one λ with b ≥ 1 contributes
  (−1)ᵐ · 2k(2d+1) · 8ᵈ A!³ (2B)!² · m·m! / ((k²−d²)(k²−(d+1)²)(2A+1)! B!³),
  and λ = (k) contributes 8ᵏ⁻¹(k−1)!³/(2k−1)!.
- The OEIS entry points to the same formula on p. 23 of Helsgaun's
  [k-opt report](http://www.akira.ruc.dk/~keld/research/LKH/KoptReport.pdf),
  but that copy has a typo: the factor (k−a+b−1) in the inner sum must be
  (k−a−b+1)! (Herman Jamke's OEIS note). The program follows the paper.
- The λ = (k) term is the b ≥ 1 formula taken at B = 0, d = k−1 once m is
  cancelled against the factor k−d−1 of k²−(d+1)² (for B = 0 they are
  equal). Both are 0 at that point, so `(m or B<1)` puts 1 in the numerator
  and `or 2*k` keeps only k+d+1 = 2k in the denominator. The loops run over
  B ≥ 0 and 0 ≤ d ≤ k−1−2B (so m ≥ 0). The points with m = 0 and B > 0 are
  not partitions. Their factor `m or B<1` is False, so they add 0.
- `f` is a signed factorial, f(n) = (−1)ⁿ n! (and f(n) = `True` = 1 for
  n < 1): one byte more than n!, and it handles the sign. The factorials in
  a term multiply to sign (−1)^(A+B+m+1) = (−1)ᵏ. The term needs (−1)ᵐ, so
  the missing (−1)^(d+1) comes from `(-8)**d` and from d²−k² < 0.
  2k(2d+1) is written k·(4d+2), with the k outside the sum.
- Exact integers: each term's denominator divides (7k)!. The four factors
  k±d, k−d−1, k+d+1 (or 2k), plus (2A+1)! and B!³, divide a product of
  factorials whose arguments add up to less than 6.5k. So
  M·term (with M = (7k)!) is an exact `//`, and k·Σ//M is a(k).

**Notes**

- Correct for every n by the theorem above; checked against the whole
  b-file. Kotesovec's recurrence on the OEIS page is a conjecture and is not
  used.
- About k²/4 terms of a few factorials each: the 100 b-file terms take about
  4 s. The recursive `f(7*k)` hits Python's recursion limit at n = 143, so the
  program stops there with a RecursionError, after 142 correct terms.
- The bar is the whole b-file (100 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 219 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001171), CC BY-SA 4.0.
