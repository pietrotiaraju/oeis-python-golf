# A000039

> Coefficient of q^(2n) in the series expansion of Ramanujan's mock theta function f(q).
> — [OEIS A000039](https://oeis.org/A000039)

Offset 0: 1, −2, −3, −5, −6, −10, −11, −17, −21, −27, −33, −46, −53, −68, …

### Python 3 — 96 bytes

```python
m=0
while 1:x=B=8<<m;k=m+1;exec("x=4*B**m+2*B+B*x//(B**k+1)**2;k-=1;"*k);print(x//4%B-B//2);m+=2
```

**How it works**

- a(n) is the coefficient of q^m, m = 2n, in
  f(q) = Σ_{k≥0} q^(k²) / ((1+q)²(1+q²)²⋯(1+qᵏ)²), so this is
  [A000025](../A000025/) at the even places. Instead of a list of
  coefficients, the program evaluates f at q = 1/B with B = 2^(m+3) and reads
  a(n) off as a digit in base B.
- At q = 1/B the k-th term is B^k / ((B+1)²⋯(B^k+1)²), and term k over
  term k − 1 is B / (B^k+1)². So f(1/B) has the Horner form
  1 + B/(B+1)² · (1 + B/(B²+1)² · (1 + …)), which the `exec` string runs
  from k = m + 1 down to 1 with floor division, every level adding the
  scale S = 4·B^m + 2B. `x=B` only seeds the innermost level; it ends up
  multiplied by about B^(−(m+1)²) and vanishes.
- Then x ≈ S·f(1/B) = 4·P + 2B + 2 + ε, where P = Σ_{j≤m} a_j B^(m−j)
  holds the coefficients up to q^m as signed base-B digits, 2B·f(1/B) =
  2B + 2 − 4/B + … supplies the offset, and |ε| < 2 collects the
  coefficients past q^m (|4·Σ_{j>m} a_j B^(m−j)| < 0.54), the rest of
  2B·f(1/B) (< 0.13), the floor errors (each level's error is divided by
  more than B on the way out, so they total less than B/(B−1)) and the
  terms k > m (below B^(m−(m+1)²)). The window lands in [0, 4), so
  `x//4` is exactly P + B/2.
- P ≡ a_m (mod B) and |a_m| < B/2, so `x//4%B-B//2` is a_m. All the
  bounds rest on |a_j| ≤ p(j) ≤ 2^(j−1): replacing 1/(1+qⁱ)² by
  1/(1−qⁱ)² can only increase the coefficients in absolute value, and
  turns f into Σ q^(k²)/(q;q)_k², the Durfee-square series of the
  partition numbers p(j). The arithmetic is exact for every n.
- For m = 0 the estimate of the tail does not apply (B = 8 is small), but
  the program gives x = 4 + 16 + ⌊64/81⌋ = 20 and prints 20//4 % 8 − 4 = 1.

**Notes**

- The A000025 program with `m+=2` instead of `m+=1` is 119 bytes. It
  divides lists of coefficients and is faster: 200 terms in about 6 s.
- This one handles numbers of about m² bits and is slower: 200 terms in
  about 25 s, 250 in about 62 s. The bar is 200 terms in 60 s, which is
  the same depth (m up to 398) as the 400 terms of A000025. The b-file
  has 5001 terms.
- The offset 2B is what keeps the extraction short: with S = B^(m+1) the
  rounding needs `(x+B*-~B//2)//B%B-B//2`. A scale of 2·B^m would be
  too small, because the floor error alone can reach 1.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000039), CC BY-SA 4.0.
