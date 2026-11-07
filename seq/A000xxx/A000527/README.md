# A000527

> Series-parallel numbers.
> — [OEIS A000527](https://oeis.org/A000527)

Offset 4: 52, 472, 3224, 18888, 101340, 511120, 2465904, 11496144, 52165892, 231557064, …

a(n) counts series-parallel networks with n edges of which four carry the
labels 1, 2, 3, 4 and the other n − 4 are unlabeled (Riordan 1958, p. 142).
a(4) = 52 and a(5) = 472 are the fully labeled counts A006351; a brute-force
enumeration also gives a(6) = 3224.

### Python 3 — 169 bytes

```python
L=[n:=1,1]
while 1:X=99**n;Q=0;[Q:=Q*X+c for c in L];print(4*Q*(3*Q*Q+8*Q+2)*pow(2-Q,-7,X**n)//X**~-n%X);n+=1;L=[sum(sum(L[d-1::d])*d*L[~d]for d in(1,*range(1,n)))//n]+L
```

**How it works**

- S(x) = x + 2x² + 4x³ + 10x⁴ + … counts series-parallel networks
  ([A000084](../A000084/)), and the OEIS generating function (S. A. Irvine
  2010) is Σ_{j≥0} a(j+4)·x^j = 4(13 + 14S + 3S²)(1 + S)/(1 − S)⁷. In
  Q = 1 + S it reads G = 4Q(3Q² + 8Q + 2)/(2 − Q)⁷.
- The recurrence for S. A network with at least two edges is a series or a
  parallel composition, and duality swaps the two kinds, so S = x + 2T with
  T the series ones. A series network is a multiset of at least two
  networks that are not series (g.f. x + T), so the Euler transform
  ℰ(x + T) = Π(1 − x^k)^(−[x^k](x+T)) equals 1 + (x + T) + T = 1 + S.
  Since ℰ is multiplicative and ℰ(x) = 1/(1 − x),
  ℰ(S) = ℰ(x + T)·ℰ(T) = (1 + S)²(1 − x). Taking x·d/dx of the logarithm,
  2n·s_n = Σ_{k=1}^{n} (c_k + 1)·A_{n−k} with c_k = Σ_{d|k} d·s_d and A the
  coefficients of 1 + S (A₀ = 1). The c_n term holds n·s_n·A₀, so
  n·s_n = Σ over d = 1, 1, 2, …, n−1 of d·s_d·Σ_{j≥1} A_{n−jd}: the second
  d = 1 entry is the +1, because s₁ = 1.
- `L` holds A newest first, L = [A_{n−1}, …, A₁, A₀], so `L[~d]` is s_d
  and `L[d-1::d]` is A_{n−d}, A_{n−2d}, …. The new coefficient goes in
  front with `L=[…]+L`, which costs 2 bytes more than appending, but the
  Horner sum `[Q:=Q*X+c for c in L]` then needs no `[::-1]` and gives
  Q = Σ_i A_i·X^i, that is 1 + Ŝ evaluated at x = X.
- x ↦ X maps Z[x]/(x^n) onto Z/X^n, and 2 − Q ≡ 1 (mod X) is invertible,
  so 4Q(3Q² + 8Q + 2)·`pow(2-Q,-7,X**n)` is congruent mod X^n to
  Σ_{j<n} g_j X^j, where g_j = a(j+4) are the true coefficients (Ŝ agrees
  with S up to degree n). If every g_j < X these are the base-X digits,
  and `//X**~-n%X` reads g_{n−1} = a(n+3). Pass n = 1 prints a(4), so the
  stored A₁ = 1 is all the seed needed.
- The digit bound. Every network is the value of a binary expression tree
  with S/P labels at its k − 1 inner nodes, so s_k ≤ Catalan(k−1)·2^(k−1)
  ≤ 8^(k−1) and S ≼ x/(1 − 8x) coefficientwise. G is a power series in S
  with nonnegative coefficients, and 1/(1 − S), 1 + S ≼ 1/(1 − 9x),
  13 + 14S + 3S² ≼ 30/(1 − 9x)², so G ≼ 120/(1 − 9x)¹⁰ and
  g_j ≤ 120·C(j+9, 9)·9^j. With X = 99^n this is below X for every
  j ≤ n − 1 once n ≥ 3 (n = 3: 534600 < 99³), and for n = 1, 2 the digits
  52 and 472 are below 99 and 99².

**Notes**

- The same program appending to the list in the natural order and
  reversing it for the Horner sum: 172 bytes. The first entry evaluated S
  at 2^((n+2)²) with an `if n>3:` block: 218 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 135 terms in 60 s here.
- a(n) grows by a factor of about 3.8 per term (a(38)/a(37)), so the
  4300-digit int-to-str limit is out of reach.
- The b-file has 35 terms (up to a(38)); the bar is 15 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |
| 2026-11-07 | Python 3 | 169 | Q = 1 + S form, list kept newest first for the Horner sum |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000527), CC BY-SA 4.0.
