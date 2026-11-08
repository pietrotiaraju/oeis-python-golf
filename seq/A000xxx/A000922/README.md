# A000922

> Primes p of the form 3k+1 such that -sqrt(p) < Sum_{x=1..p} cos(2*Pi*x^3/p) < sqrt(p).
> — [OEIS A000922](https://oeis.org/A000922)

Offset 1: 13, 19, 37, 61, 109, 157, 193, 241, 283, 367, 373, 379, 397, 487, 571, 613, 619, 733, 739, 859, …

### Python 3 — 229 bytes

```python
P=p=1
while 1:
 P*=p*p;p+=1
 if P%p*p%3==1:
  s=p**6;x=Y=4*s//p;k=1
  while x:x=x*k//(k-~k);Y+=x;k+=1
  c=s-Y*Y//2//s+Y**4//24//s**3;C=[s,c];exec('C+=2*c*C[-1]//s-C[-2],;'*p)
  if sum(C[x**3%p]for x in range(p))**2<p*s*s:print(p)
```

**How it works**

- Let p ≡ 1 (mod 3) be prime and S = Σ_{x=1}^{p} cos(2πx³/p) (the term
  x = p is the same as x = 0). Gauss showed that S is a root of
  f(x) = x³ − 3px − pL, where 4p = L² + 27M² and L ≡ 1 (mod 3) (OEIS
  comment; it comes from the cubic Gauss periods). Since M ≠ 0,
  |L| < 2√p, so f(−2√p) < 0 < f(−√p) and f(√p) < 0 < f(2√p): f has one
  root below −√p, one between −√p and √p and one above √p.
  [A000921](../A000921/), [A000922](../A000922/) and [A000923](../A000923/)
  split the primes by which root S is. No formula is known for that
  (Kummer's problem), so S has to be computed.
- How close can S get to ±√p? |f(±√p)| = p(2√p ± L) ≥ p(2√p − |L|) =
  27pM²/(2√p + |L|) ≥ 27√p/4, and |f′| ≤ 9p on [−2√p, 2√p], so S is at
  least 3/(4√p) away from ±√p. An approximation T/s with
  |T − sS| < (3/4)s/√p therefore lies on the same side of √p and of −√p
  as S, and the program compares T with ±√p·s exactly, as integers:
  |S| < √p is `T**2<p*s*s`.
- T is computed in fixed point with scale s = p⁶, in integers only:
  1. `Y` ≈ s·2π/p from π/2 = Σ_k k!/(2k+1)!!: the terms
     x_k = ⌊x_{k−1}·k/(2k+1)⌋ start at 4s/p (`k-~k` is 2k+1) and the loop
     stops when they reach 0.
  2. `c=s-Y*Y//2//s+Y**4//24//s**3` ≈ s·cos(Y/s): three Taylor terms are
     enough, since the next one, s·u⁶/720 with u = Y/s ≤ 2π/p, is at most
     (2π)⁶/720 < 86 when s = p⁶.
  3. The Chebyshev recurrence C_{k+1} = ⌊2cC_k/s⌋ − C_{k−1} from C₀ = s,
     C₁ = c gives C_k ≈ s·cos(2πk/p); `exec` runs p copies of the step,
     which is shorter than a loop.
  4. T = Σ_{x<p} C[x³ mod p].
- Error bound. Each floor loses less than 1 and each term of the π
  series is less than half the one before, so 0 ≤ 2πs/p − Y <
  10·log₂p + 10; with the Taylor remainder and the floors in `c`,
  |Δ| = |c − s·cos(2π/p)| < 10·log₂p + 98. With cos φ = c/s, the rounded
  recurrence stays within (k−1)/sin φ of s·cos kφ, and
  s·|cos kφ − cos kθ| ≤ k·|Δ|/sin ξ for some ξ near θ = 2π/p; both sines
  are at least sin(π/p) ≥ 2/p. So |C_k − s·cos kθ| ≤ kp(1+|Δ|)/2 and
  |T − sS| ≤ p³(1+|Δ|)/2, which is below (3/4)p^5.5 = (3/4)s/√p for every
  p ≥ 7, because 1+|Δ| < 1.5·p^2.5 there.
- `P` is ((p−1)!)², so `P%p*p%3==1` holds exactly for the primes
  p ≡ 1 (mod 3) (Wilson's theorem).

**Notes**

- Integer arithmetic throughout, with a proven error bound valid for every
  p; the only outside fact is Gauss's cubic for S.
- Compiling the p statements of the `exec` string is the slow part:
  about 170 terms in 60 s. Writing the recurrence as a
  `for k in C*p:` loop costs 4 bytes more and is about three times faster.
- The b-file has 1000 terms; the bar is 130 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 229 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000922), CC BY-SA 4.0.
