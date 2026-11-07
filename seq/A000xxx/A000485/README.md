# A000485

> Number of partially labeled trees with n nodes (4 of which are labeled).
> — [OEIS A000485](https://oeis.org/A000485)

Offset 4: 16, 125, 680, 3135, 13155, 51873, 195821, 715614, 2550577, 8911942, …

### Python 3 — 163 bytes

```python
r=[n:=1]
while 1:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;n+=1;X=8**n;T=0;[T:=T*X+c for c in r];U=X**n-T;n>3==print(T**4*(3*T*T+13*T*U+16*U*U)//U**5%X)
```

**How it works**

- The g.f. on the OEIS page is f(B) with f(b) = b⁴(16 − 19b + 6b²)/(1−b)⁵,
  where B(x) = Σ t(k)xᵏ counts unlabeled rooted trees,
  [A000081](../A000081/).
- `r` holds t(1), …, t(n). The first statement appends t(n+1) by the
  usual Euler-transform recurrence,
  n·t(n+1) = Σ_d d·t(d)·Σ_{m≥1} t(n+1−md), in the form of the A000081
  page: `r[~j::~j]` walks back from t(n−j) in steps of d = j + 1.
- Then x = 1/X with X = 8ⁿ: the Horner walrus gives
  T = Xⁿ·B_n(1/X), where B_n is B cut after xⁿ, and U = Xⁿ − T. With
  b = T/Xⁿ and 1 − b = U/Xⁿ, Xⁿ·f(b) = T⁴(16X²ⁿ − 19TXⁿ + 6T²)/U⁵, and
  substituting Xⁿ = T + U turns the bracket into 3T² + 13TU + 16U². So
  `T**4*(3*T*T+13*T*U+16*U*U)//U**5` is ⌊Σ_k c_k·Xⁿ⁻ᵏ⌋, where c_k are the
  coefficients of f(B_n(x)); c_k = a(k) for k ≤ n.
- `n>3==print(…)` prints only from n = 4 on: the chained comparison calls
  `print` only when n > 3.

**Why the floor and the last digit are right**

- f has nonnegative coefficients: the coefficient of b^(4+j) is
  16C(j+4,4) − 19C(j+3,4) + 6C(j+2,4) = (j+1)(j+2)(3j² + 49j + 192)/24.
  So 0 ≤ c_k ≤ a(k).
- A rooted tree with k nodes has a plane embedding, so t(k) is at most
  the Catalan number C(k−1), and B ≤ g = (1 − √(1−4x))/2 coefficientwise.
  Then Σ a(k)4⁻ᵏ ≤ f(g(¼)) = f(½) = 16, so a(k) ≤ 16·4ᵏ.
- The part of the sum below the units, Σ_{j≥1} c_{n+j}·8^(−nj), is then
  below 1: for n ≥ 7 the j = 1 term is at most 64/2ⁿ ≤ ½ and the rest is
  tiny; for n = 4, 5, 6 the j = 1 term is a(n+1)/8ⁿ ≤ 0.031 (125/4096,
  680/8⁵, 3135/8⁶) and the bound 16·4ᵏ handles j ≥ 2. So the floor is
  Σ_{k≤n} a(k)·Xⁿ⁻ᵏ, and `%X` returns a(n), because a(n) < 8ⁿ (from
  16·4ⁿ for n ≥ 5; a(4) = 16).

**Notes**

- `X=16**n` makes the tail bound work without the small cases and costs
  1 byte. The previous record, 205 bytes, inverted 1 − S modulo B^(m+1)
  with `pow(1-S,-5,…)`.
- Exact integer arithmetic, so the program is right for every n.
- T has about 3n² bits, so the terms slow down: about 190 terms in 10 s
  and 280 in 60 s here. The b-file has 997 terms (up to a(1000)); the bar
  is 100 terms in 10 s.
- a(n) first has more than 4300 digits around n = 9100 (growth rate
  2.9557ⁿ), far beyond what the program reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 205 | first entry |
| 2026-11-07 | Python 3 | 163 | evaluate at x = 1/8ⁿ by Horner, f(B) as T⁴(3T²+13TU+16U²)/U⁵ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000485), CC BY-SA 4.0.
