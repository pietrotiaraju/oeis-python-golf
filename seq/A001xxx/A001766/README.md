# A001766

> Index of (the image of) the modular group Gamma(n) in PSL_2(Z).
> — [OEIS A001766](https://oeis.org/A001766)

Offset 1: 1, 6, 12, 24, 60, 72, 168, 192, 324, 360, 660, 576, 1092, 1008, …

### Python 3 — 86 bytes

```python
J=[n:=0]
while 1:n+=1;J+=n*n-sum(J[d>>n%d*n]for d in range(1,n)),;print(n*J[n]>>(n>2))
```

**How it works**

- Γ(n) is the kernel of reduction mod n, SL₂(ℤ) → SL₂(ℤ/n), which is
  onto, so its index in SL₂(ℤ) is |SL₂(ℤ/n)| = n³∏(1 − 1/p²) = n·J₂(n),
  with J₂ Jordan's totient (that order is [A000056](../../A000xxx/A000056/)).
  Passing to PSL₂(ℤ) divides by 2 when −I is not in Γ(n), that is for
  n ≥ 3; for n ≤ 2, −I ≡ I mod n and the index stays n·J₂(n) (6 for
  n = 2, 1 for n = 1). `>>(n>2)` halves only from n = 3 on.
- J₂ comes from Σ_{d|n} J₂(d) = n², as in [A000114](../../A000xxx/A000114/)
  (the cusps of Γ(n), J₂(n)/2): every pair (x, y) mod n has a gcd g with n,
  and dividing by g leaves a primitive pair mod n/g. So
  J₂(n) = n² − Σ J₂(d) over the divisors d < n, and the list `J` keeps
  every value found so far.
- `J[d>>n%d*n]` reads J[d] when d divides n (the shift is 0); otherwise the
  shift is at least n, more than the bits of d, and it reads `J[0]`, which
  is 0. `J=[n:=0]` makes that zero slot and starts n at 0 in 8 bytes.

**Notes**

- A recursive lambda, `f=lambda n:n*n-sum(f(d>>n%d*n)for d in
  range(1,n))` with `while[print(n*f(n)>>(n>2))]:n+=1`, is 87 bytes.
  Counting the pairs directly, `sum(gcd(k%n,k//n,n)<2for k in range(n*n))`
  with `from math import*`, is 92 bytes and takes n² steps a term.
- Exact integer arithmetic, so the program is right for every n. Each term
  costs n steps; the b-file (1000 terms) prints in 0.2 s, and the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001766), CC BY-SA 4.0.
