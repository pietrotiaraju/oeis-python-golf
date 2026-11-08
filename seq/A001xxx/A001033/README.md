# A001033

> Numbers n such that the sum of the squares of n consecutive positive odd numbers x^2 + (x+2)^2 + ... + (x+2n-2)^2 = k^2 for some integer k. The least values of x and k for each n are in A056131 and A056132, respectively.
> — [OEIS A001033](https://oeis.org/A001033)

Offset 1: 1, 16, 25, 33, 49, 52, 64, 73, 97, 100, 121, 148, 169, 177, 193, 196, 241, 244, 249, 256, 276, 289, …

### Python 3 — 493 bytes

```python
from math import*
k=0
while k:=k+1:
 D=range(1,2*k);b=min(k//s**2for s in D if k%s**2<1);N=3*k*k-3;S={k<2or b<2and any(N%d+(T:=N//d-d-6*k)%12<1>-T for d in D)}
 for f in[f for f in D if N%f**2<1<b]:
  M=N//f//f;R=[0];m=p=1
  while m<M:
   p+=1
   while M%(q:=m*p)<1:R=[y for x in R for y in range(x,q,m)if(y*y-b)%q<1];m=q
  for P in R:
   Q,g,u,w=M,1,f*M,-f*P
   while{t:=(P,Q,g,u,w)}-S:S|={t,Q+g==0==u-k%2*3};a=(P+isqrt(b)+(Q<0))//Q;P=a*Q-P;Q=(b-P*P)//Q;g=-g;u,w=(a*u+w)%6,u
 if{1}&S:print(k)
```

**How it works**

- With c = x + k − 1 the mean of the k odd numbers x, x+2, …, x+2k−2,
  their squares add up to k(3c² + k² − 1)/3. Write k = b·s² with b
  squarefree and N = 3(k² − 1). Multiplying by 9/k, the sum is a square y²
  exactly when X'² − b·Z² = −N with X' = 3c and Z = 3y/(bs), an integer
  because b is squarefree. x is a positive odd number exactly when
  X' ≡ 3k (mod 6) and X' ≥ 3k; the class condition is sign-free.
- This is the equation of [A001032](../A001032/) with another class, so the
  program is the same with two constants changed: the square case tests
  T = E − d − 6k (`N//d-d-6*k`) and a hit needs X' ≡ 3k (mod 6)
  (`u-k%2*3`). In short:
- k = 1 is always a term. Square k (b = 1): (Z − X')(Z + X') = N, so each
  divisor d < √N < 2k of N gives X' = (E − d)/2 with E = N/d, and the
  conditions are T ≥ 0 and T ≡ 0 (mod 12): `N%d+(T:=N//d-d-6*k)%12<1>-T`.
- Non-square k: multiplying a solution by ε² (ε the Pell unit of
  t² − bu² = 1) keeps X' mod 6 and makes it as large as we like, so k is a
  term iff some solution has X' ≡ 3k (mod 6).
- That is decided with the Lagrange–Matthews–Mollin method: for each f with
  f² | N, M = N/f², each root z of z² ≡ b (mod M) (found by lifting one
  factor p of M at a time in `R`), the primitive solutions of
  x² − by² = −M with y > 0 in the class of z are x = M·A − z·B, y = B at
  the steps i of the continued fraction of (z + √b)/M with (−1)ⁱ·Qᵢ = −1.
  `u,w` follow f·x mod 6 through the convergent recurrence, from
  (f·M, −f·z).
- The state (P, Q, g, u, w) takes finitely many values from some point on,
  so `while{t:=(P,Q,g,u,w)}-S:` stops when it repeats; the set `S` is
  shared by all f and z of one k and also collects the hit tests, and
  `{1}&S` is the verdict. `(P+isqrt(b)+(Q<0))//Q` is the exact floor of
  (P + √b)/Q for either sign of Q.

**Notes**

- Exact integer arithmetic; the facts used are the reduction above, Pell
  units, and the LMM theorem (K. R. Matthews, Expositiones Math. 18 (2000)
  323–331). See [A001032](../A001032/) for the details.
- The whole b-file (7103 terms, k ≤ 250 000) agrees with a faster version
  of the same decision; the program itself was compared on its first 320
  terms.
- It prints 320 terms (k ≈ 7330) in 60 s, fewer than A001032 because the
  terms are sparser; the bar is 250 terms with a 120 s timeout (about 30 s
  here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 493 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001033), CC BY-SA 4.0.
