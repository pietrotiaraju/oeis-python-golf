# A000185

> a(n) = A058087(n,n-5).
> — [OEIS A000185](https://oeis.org/A000185)

Offset 5: 2, 24, 140, 1232, 11268, 115056, 1284360, 15596208, 204710454, 2888897032, …

### Python 3 — 90 bytes

```python
a=b=0;c=1;n=3
while[print((n+2)*abs(~-n*(8*a+n)-8*n*c-6*~b)//30)]:a,b,c=b,c,n*(b-c)-a;n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t⁵: the
  number of permutations π of 1..n with exactly five i such that
  π(i) ≡ i or i+1 (mod n).
- Two identities fold the factor 2n/(2n−k) and C(k,5) away (C(m,k)/m =
  C(m−1,k−1)/k with m = 2n−k, then C(k,5)/k = C(k−1,4)/5):
  a(n) = (2n/5)·e_4(n−1), where
  e_j(m) = Σ_k (−1)^(k−j)·C(k,j)·C(2m−k,k)·(m−k)! is the number of
  permutations of 1..m with exactly j i such that π(i) = i or i+1 (the
  straight-table hit numbers, [A058057](https://oeis.org/A058057)).
- With W_m = [A000271](https://oeis.org/A000271)(m) = e_0(m),
  12e_4(m) = 8(m−1)W_{m−1} + 6W_{m−2} − 8(m−2)W_{m−3} − (−1)^m(m²−3m+8)
  for m ≥ 2. Proof as for e_3 on the [A000181](../A000181/) page: both
  generating functions reduce, with θf = (u−1)f − u and W's differential
  equation, to ρ(z)·W(z) + σ(z) with the same ρ = (4−4z−z²−4z³+4z⁴)/6, and
  the σ's differ by 6z − 8, so the sequences agree from m = 2 on.
  (ρ is a polynomial here, but the constant-coefficient form would need
  five consecutive W's and a (−1)^m·(quadratic) term.)
- The program runs −X_k = −(−1)^k·W_k, whose recurrence
  X_{k+1} = k(X_{k−1} − X_k) − X_{k−2} (from A000271's, k ≥ 2) has plain
  copies. The counter is k = n−2 and the state (a,b,c) = (−X_{k−2}, −X_{k−1}, −X_k),
  seeded at k = 3 with 0, 0, 1 (X_1, X_2, X_3 = 0, 0, −1).
- a(n) = 2(k+2)·e_4(k+1)/5, and 12e_4(k+1) = (−1)^k·L with
  L = 8(k−1)a + k(k−1) − 8kc + 6(b+1), written `~-n*(8*a+n)-8*n*c-6*~b`.
  So a(n) = (k+2)·|L|/30, and `abs` is safe because a(n) ≥ 0.

**Notes**

- Each term is a few big-integer operations. The whole b-file
  (246 terms) prints at once; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4298 digits). All printed terms agree with the hit-polynomial
  sum.
- The previous record (113 bytes) summed the folded formula term by term:
  `n*sum((-1)**j*perm(j,4)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//60`.
- The relation was found by fitting e_4 against three consecutive W's with
  coefficients of degree ≤ 1 and a (−1)^m·(quadratic) term, over every
  index shift and sign pattern of the state; this layout was the shortest.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 113 | first entry |
| 2026-11-05 | Python 3 | 90 | 113 → 90: W-recurrence instead of the sum |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000185), CC BY-SA 4.0.
