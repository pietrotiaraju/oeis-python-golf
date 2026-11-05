# A000130

> One-half the number of permutations of length n with exactly 1 rising or
> falling succession.
> — [OEIS A000130](https://oeis.org/A000130)

Offset 0: 0, 0, 1, 2, 5, 20, 115, 790, 6217, 55160, 545135, 5938490,
70686805, 912660508, …

### Python 3 — 88 bytes

```python
a=b=m=0;c,d=1,2
while[print(a)]:m+=1;a,b,c,d=b,c,d,m*(d-c-b+a)+4*d+3*a+2*(a+2*b+~m*c)//m
```

**How it works**

- A succession is a pair i, i+1 standing next to each other, in either
  order. Reversing a permutation keeps its successions and never gives the
  same permutation back (n ≥ 2), so the permutations with exactly one come
  in pairs and a(n) counts the pairs.
- The program runs R. J. Mathar's recurrence from
  [A086852](https://oeis.org/A086852) (= 2·a(n)), true for n ≥ 3:

  **(n − 3)a(n) = (n+1)(n−3)a(n−1) − (n² − 4n + 5)a(n−2)
  − (n−1)(n−5)a(n−3) + (n−1)(n−2)a(n−4).**

  At n = 3 both sides vanish, so it gives a(n) for n ≥ 4 from
  a(0..3) = 0, 0, 1, 2.
- Divide by m = n − 3. Each coefficient splits into a polynomial in m and a
  remainder over m:

  a(n) = m(a(n−1) − a(n−2) − a(n−3) + a(n−4)) + 4a(n−1) + 3a(n−4)
  + 2(a(n−4) + 2a(n−3) − (m+1)a(n−2))/m.

  The left side and the rest of the right side are integers, so the last
  quotient is exact and `//` computes it exactly; `~m` is −m−1.
- `a,b,c,d` hold a(n−4) … a(n−1) and `m` counts 1, 2, 3, … from n = 4.
  The loop prints `a` and shifts the window; `[print(a)]` is a list holding
  `None`, never empty, so always true.

**Why the recurrence holds**

The OEIS states the recurrence without proof; here is one.

- Inclusion–exclusion, as in Robbins's formula on the A086852 page: glue
  a chosen set of successions into runs. That splits 1..n into consecutive
  blocks; a block of size s ≥ 2 is laid out increasing or decreasing and
  the k blocks in any of k! orders. With w = t − 1 marking each glued pair,
  Σₙ Σ_π t^succ(π) xⁿ = Σₖ k!·Pᵏ, where P = x + 2wx²/(1 − wx) and π runs
  over the permutations of 1..n.
- At w = −1 (t = 0), P = z = x(1−x)/(1+x), which gives Flajolet's
  generating function E(z) = Σ k!·zᵏ of [A002464](https://oeis.org/A002464).
  The coefficient of t¹ is d/dw at w = −1, and ∂P/∂w = 2x²/(1+x)² there,
  so
  G(x) = Σ a(n)xⁿ = x²/(1+x)² · E′(z).
- As formal power series, z²E′(z) = (1 − z)E(z) − 1. So G and all its
  derivatives are E(z) times a rational function of x plus another rational
  function of x. Applying the recurrence's operator to G (n ↦ x·d/dx,
  a(n−k) ↦ xᵏ) leaves exactly x², the left side minus the right side at
  n = 2. This is checked with sympy:

  ```python
  from sympy import *
  x,E=symbols('x E')
  z=x*(1-x)/(1+x)
  dE=((1-z)*E-1)/z**2              # E'(z), from z²E' = (1-z)E - 1
  T=lambda f:x*(diff(f,x)+diff(f,E)*dE*diff(z,x))   # x d/dx
  G=x**2/(1+x)**2*dE               # g.f. of A000130
  G1=T(G);G2=T(G1)                 # sum n a(n) xⁿ, sum n² a(n) xⁿ
  print(cancel(3*G-G1+x*(G2-4*G)-x**2*(G2+G)-x**3*(G2-4*G)+x**4*(G2+5*G1+6*G)))
  ```

  prints `x**2`. The recurrence therefore holds for every n ≥ 3, and the
  program is right for every n.

**Notes**

- Mathar's recurrence with the division left whole,
  `((m+4)*m*d-(m*m+2*m+2)*c-(m*m-4)*b+(m+2)*(m+1)*a)//m`, is 103 bytes.
  Splitting off the remainder as `4*d-2*c+3*a+2*(a+2*b-c)//m` is 89;
  moving the −2c back into the quotient as `~m*c` gives the 88.
- An order-6 recurrence needs no division:
  a(n) = (n+1)a(n−1) − n·a(n−2) + 5a(n−4) + (7−n)a(n−5) + (n−4)a(n−6) for
  n ≥ 5 (the same sympy check leaves −x² + 2x³ + x⁴). As
  `a=b=c=0;d,e,f=1,2,5;n=4` +
  `while[print(b)]:n+=1;a,b,c,d,e,f=b,c,d,e,f,n*(f-e-b+a)+f+5*c+7*b-4*a`
  it is 92 bytes: two more state variables cost more than the division.
- The same generating function gives (1−x)²(1+x)·G = (1+x²)·E(z) − 1 − x,
  that is a(n) − a(n−1) − a(n−2) + a(n−3) = A002464(n) + A002464(n−2) for
  n ≥ 2. Running A002464 alongside takes seven state variables.
- a(1559) has 4302 digits, past Python's 4300-digit limit for converting
  an int to a string, so `print` stops with a `ValueError` after the 1559
  terms a(0)..a(1558). The arithmetic itself has no limit.
- The b-file has the 201 terms a(0)..a(200), all printed in about 0.1 s
  here; the bar is the whole b-file in 60 s. 600 terms also agree with the
  inclusion–exclusion double sum.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000130), CC BY-SA 4.0.
