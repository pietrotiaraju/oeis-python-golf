# A001782

> Discriminants of Shapiro polynomials.
> — [OEIS A001782](https://oeis.org/A001782)

Offset 1: 1, -44, -4940800, -564083990621761115783168, …

### Python 3 — 328 bytes

```python
p=q=[1]
while 1:
 p,q=p+q,p+[-x for x in q];A=p;B=[i*x for i,x in enumerate(p)][1:];g=h=1;s=p[-2]
 while B[1:]:a=len(A);d=a-len(B);s*=(a|d)%2or-1;exec("A=[B[0]*x-A[0]*y for x,y in zip(A,B+[0]*d)][1:];"*-~d+"\nwhile[0]==A[:1]<A:A=A[1:]");A,B=B,[x//g//h**d for x in A];g=A[0];h=g**d//h**~-d
 print(s*B[0]**~-len(A)//h**(len(A)-2))
```

**How it works**

- **The polynomials.** P₀ = Q₀ = 1, Pₙ₊₁ = Pₙ + x^(2ⁿ)Qₙ and
  Qₙ₊₁ = Pₙ − x^(2ⁿ)Qₙ, so Pₙ has degree d = 2ⁿ − 1 and coefficients
  p₀, …, p_d = ±1 (the Rudin–Shapiro sequence). `p,q=p+q,p+[-x for x in q]`
  builds the coefficient lists from x⁰ up, and a(n) = disc(Pₙ).
- **Read backwards.** The program reads the list `p` from the top power
  down, i.e. it works with A(x) = x^d·Pₙ(1/x). Since Pₙ(0) = 1, A has the
  roots 1/αᵢ and leading coefficient 1, and disc A = disc Pₙ (the
  differences 1/αᵢ − 1/αⱼ bring a factor ∏αᵢ^(−2(d−1)), which the leading
  coefficient Pₙ(0) = lc(Pₙ)·(−1)^d∏αᵢ cancels).
- **A cheaper derivative.** Instead of A′ the program uses C = dA − xA′,
  whose coefficient list (top down) is i·pᵢ for i = 1…d:
  `[i*x for i,x in enumerate(p)][1:]`, leading coefficient p₁ = 1. At each
  root C(α) = −αA′(α), so Res(A, C) = ∏(−αᵢ)·Res(A, A′) = p_d·Res(A, A′),
  and disc A = (−1)^(d(d−1)/2)·Res(A, A′). Hence
  a(n) = σ·Res(A, C) with σ = (−1)^(d(d−1)/2)·p_d. The recursion gives
  p_d = lc(Pₙ) = (−1)^(n−1), and d(d − 1)/2 is odd for n ≥ 2, so σ = (−1)ⁿ
  for n ≥ 2 and σ = 1 for n = 1. That is exactly the next-to-top
  coefficient p_(d−1) (the top half of Pₙ is Qₙ₋₁, whose next-to-top
  coefficient is (−1)ⁿ, and P₁ = 1 + x): `s=p[-2]`.
- **Subresultants.** Res(A, C) comes from the subresultant algorithm
  (G. E. Collins, 1967; H. Cohen, *A Course in Computational Algebraic
  Number Theory*, Algorithm 3.3.7), all in integers. Each round takes
  δ = deg A − deg B, flips the sign when both degrees are odd (lengths `a`
  and `d` both even), forms the pseudo-remainder of B[0]^(δ+1)·A by B
  (δ + 1 passes of `A=[B[0]*x-A[0]*y …][1:]`, repeated by `exec`), strips
  its leading zeros, and divides it by g·hᵟ, which is exact; then
  g = lc(A) and h = gᵟ/h^(δ−1). When B is a constant,
  Res = s·B[0]^(deg A)/h^(deg A − 1). If the remainder ever vanished (a
  repeated root), the strip keeps a single 0 and the program prints 0, the
  right discriminant. Nothing assumes a normal remainder sequence.
- **Speed.** The subresultant coefficients are minors of the Sylvester
  matrix, no larger than the answer, so a(8) (degree 255, 973 digits) takes
  about a second.

**Notes**

- Euclid over `fractions.Fraction` is shorter but takes over 5 minutes for
  a(8). Here a(9) (2251 digits) arrives after about 17 s on a slow PC; a(10)
  is out of reach of a 60 s run.
- Gluing the strip loop onto the `exec` string (`+"\nwhile…"`) puts the whole
  inner loop on one line.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 8 terms (n = 1 to 8); the bar is all of them in 60 s, which
  takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 328 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001782), CC BY-SA 4.0.
