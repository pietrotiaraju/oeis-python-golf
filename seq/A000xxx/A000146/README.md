# A000146

> From von Staudt-Clausen representation of Bernoulli numbers: a(n) = Bernoulli(2n) + Sum_{(p-1)|2n} 1/p.
> — [OEIS A000146](https://oeis.org/A000146)

Offset 1: 1, 1, 1, 1, 1, 1, 2, -6, 56, -528, 6193, -86579, 1425518, -27298230, …

### Python 3 — 101 bytes

```python
r=[1]
for m in r:r+=m+1,;m%2or print(-sum(-(c:=1)*sum(j**m*(c:=c*(j-k)//j)for j in r)//k for k in r))
```

**How it works**

- With m = 2n, the classical identity behind most proofs of von
  Staudt–Clausen writes the Bernoulli number as a sum of fractions with
  denominators 1, 2, …, m + 1:
  B_m = Σ_{k=1}^{m+1} X_k / k, where X_k = (−1)^(k−1)·(k−1)!·S(m, k−1)
  = Σ_j (−1)^j·C(k−1, j)·j^m and S is a Stirling number of the second kind.
- The program never adds the 1/p terms or tests for primes. It rounds every
  fraction up instead: a(n) = Σ_k ⌈X_k / k⌉ (proof below).
- `c` runs through (−1)^j·C(k−1, j) by the recurrence c·(j − k)/j. The
  division is always exact, and c drops to 0 once j ≥ k, so the inner
  `sum` over j = 1, …, m + 1 is exactly X_k (the j = 0 term is 0^m = 0).
  `-(c:=1)*` resets c for each k and negates the sum, so `//k` gives
  ⌊−X_k/k⌋ = −⌈X_k/k⌉, and the outer minus turns that back.
- The list `r` is both the main loop and the range: when the loop reaches
  m it has just appended m + 1, so r = [1, …, m + 1]. `m%2or` prints only
  for even m, starting with a(1) at m = 2.

**Why rounding up gives a(n)**

Write t_k = X_k/k, so t_k = (−1)^i·i!·S(m, i)/(i + 1) with i = k − 1, and
m ≥ 2 is even.

- k = 1: t_1 = 0.
- k = 2: t_2 = −S(m, 1)/2 = −1/2, and ⌈t_2⌉ = 0 = t_2 + 1/2.
- k = 4: t_4 = −3·S(m, 3)/2. Here 6·S(m, 3) = 3^m − 3·2^m + 3 ≡ 1 + 3 ≡ 0
  (mod 4) because m is even, so S(m, 3) is even and t_4 is an integer.
- k composite, k ≥ 6: k divides (k − 1)!, so t_k is an integer.
- k = p, an odd prime: C(p − 1, j) ≡ (−1)^j (mod p), so
  (p − 1)!·S(m, p − 1) ≡ Σ_{j=0}^{p−1} j^m (mod p), which is −1 if
  (p − 1) | m and 0 otherwise. So t_p ≡ −1/p (mod 1) exactly when
  (p − 1) | m, and t_p is an integer otherwise.

So ⌈t_k⌉ = t_k + 1/k when k is a prime with (k − 1) | m, and ⌈t_k⌉ = t_k for
every other k. Adding up, Σ_k ⌈t_k⌉ = B_m + Σ_{(p−1)|m} 1/p = a(n). Every
prime with (p − 1) | m is at most m + 1, so none is missed.

**Notes**

- Term n costs about 4n² big-integer products, so the program prints about
  200 terms in 60 s. The bar is 150 terms in 60 s; the b-file has 317.
- From about n = 1032 on, a(n) has more than 4300 digits and `print` hits
  Python's int-to-str limit.
- Earlier versions: with `math.comb` and the sign `(-1)**j` it was 113
  bytes; keeping k − 1 as the loop variable, `//~k` and `j+~k` cost one
  byte more than the shifted `k`, `j-k` and `-(c:=1)*`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000146), CC BY-SA 4.0.
