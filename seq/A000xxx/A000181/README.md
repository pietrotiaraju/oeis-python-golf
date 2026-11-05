# A000181

> a(n) = A058087(n,n-4).
> — [OEIS A000181](https://oeis.org/A000181)

Offset 4: 2, 15, 60, 469, 3660, 32958, 328920, 3614490, 43341822, 563144725, …

### Python 3 — 89 bytes

```python
a=1;b=c=0;n=2
while[print((n+2)*abs(3*(b-c)-n*(~b+4*c)-5*a)//6)]:a,b,c=b,c,n*(b-c)-a;n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t⁴: the
  number of permutations π of 1..n with exactly four i such that
  π(i) ≡ i or i+1 (mod n).
- Two identities fold the factor 2n/(2n−k) and C(k,4) away (C(m,k)/m =
  C(m−1,k−1)/k with m = 2n−k, then C(k,4)/k = C(k−1,3)/4):
  a(n) = (2n/4)·e_3(n−1), where
  e_j(m) = Σ_k (−1)^(k−j)·C(k,j)·C(2m−k,k)·(m−k)! is the number of
  permutations of 1..m with exactly j i such that π(i) = i or i+1 (the
  straight-table hit numbers, [A058057](https://oeis.org/A058057)).
- With W_m = [A000271](https://oeis.org/A000271)(m) = e_0(m),
  3e_3(m) = 5W_m − (m−4)W_{m−1} − (4m−7)W_{m−2} + (−1)^m(m−1) for m ≥ 2.
  Proof by generating functions, as on the [A000222](../A000222/) page:
  with t = z/(1+z)², u = 1/t and f = Σ m!·t^m,
  Σ_m e_3(m)z^m = z³/(1+z)⁴·Σ_m C(2m+3,3)·m!·t^m, and θf = (u−1)f − u
  (θ = t d/dt) turns the sum into α(u)f + β(u) with explicit polynomials.
  On the right, each m·W_{m−i} has generating function θ_z(z^i W) and
  W's equation z²(1+z)W′ = (1−z²−z³)W − (1−z²) (proved on the
  [A000179](../A000179/) page) removes W′. Both sides become
  ρ(z)·W(z) + σ(z) with the same ρ = (4+4z+3z²+4z³+4z⁴)/(3(1+z)) and σ's
  that differ by 4+3z, so the two sequences agree from m = 2 on. ρ has the
  factor 1/(1+z), so unlike e_2 there is no form with constant
  coefficients.
- The program runs X_k = (−1)^k·W_k, whose recurrence
  X_{k+1} = k(X_{k−1} − X_k) − X_{k−2} (from A000271's, k ≥ 2) has plain
  copies. The counter is k = n−2 and the state (a,b,c) = (X_{k−2}, X_{k−1}, X_k),
  seeded at k = 2 with X_0, X_1, X_2 = 1, 0, 0.
- a(n) = (k+2)·e_3(k+1)/2. Writing W_{k+1} = k(W_k + W_{k−1}) + W_{k−2}
  gives 3e_3(k+1) = (4k+3)W_k + (k+3)W_{k−1} + 5W_{k−2} − (−1)^k·k
  = −(−1)^k·L with L = (k+3)b + k − (4k+3)c − 5a, written
  `3*(b-c)-n*(~b+4*c)-5*a` (−n·~b = n(b+1)). So a(n) = (k+2)·|L|/6, and
  `abs` is safe because a(n) ≥ 0.

**Notes**

- Each term is a few big-integer operations. The whole b-file
  (247 terms) prints at once; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits). All printed terms agree with the hit-polynomial
  sum.
- The previous record (113 bytes) summed the folded formula term by term:
  `n*sum((-1)**j*comb(j,3)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//-2`.
- The relation was found by fitting e_3 against three consecutive W's with
  coefficients of degree ≤ 1 and a (−1)^m·(linear) term, over every index
  shift and sign pattern of the state; this layout was the shortest.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 113 | first entry |
| 2026-11-05 | Python 3 | 89 | 113 → 89: W-recurrence instead of the sum |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000181), CC BY-SA 4.0.
