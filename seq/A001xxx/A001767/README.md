# A001767

> Genus of modular group Gamma(n) = genus of modular curve Chi(n).
> — [OEIS A001767](https://oeis.org/A001767)

Offset 2: 0, 0, 0, 0, 1, 3, 5, 10, 13, 26, 25, 50, 49, 73, 81, 133, 109, 196, …

### Python 3 — 91 bytes

```python
J=[0,n:=1]
while 1:n+=1;J+=n*n-sum(J[d>>n%d*n]for d in range(1,n)),;print(1+J[n]*(n-6)//24)
```

**How it works**

- For n ≥ 2 the image of Γ(n) in PSL₂(ℤ) has no elliptic points, index μ
  ([A001766](../A001766/)) and μ/n cusps, so the Riemann–Hurwitz formula
  for X(n) → X(1) gives g = 1 + μ/12 − μ/(2n) = 1 + μ(n − 6)/(12n).
  With μ = n·J₂(n)/2 for n ≥ 3 (J₂ is Jordan's totient) this is
  g = 1 + J₂(n)(n − 6)/24, the OEIS formula 1 + (n − 6)φ(n)ψ(n)/24.
- For n ≥ 3 the genus is an integer, so `J[n]*(n-6)//24` divides exactly
  (also for n = 3, 4, 5, where n − 6 < 0 and g = 0). At n = 2, μ = 6
  rather than n·J₂/2 = 3, so the exact quotient would be −1/2; the floor
  makes it −1 and the program prints 1 − 1 = 0, the right genus.
- J₂ comes from Σ_{d|n} J₂(d) = n² as in [A000114](../../A000xxx/A000114/):
  J₂(n) = n² − Σ J₂(d) over the divisors d < n. `J[d>>n%d*n]` reads J[d]
  when d divides n and the zero slot `J[0]` otherwise (the shift is then at
  least n). `J=[0,n:=1]` holds that slot and J₂(1) = 1 and starts at n = 2.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each term
  costs n steps; the b-file (999 terms, n = 2 to 1000) prints in 0.2 s,
  and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001767), CC BY-SA 4.0.
