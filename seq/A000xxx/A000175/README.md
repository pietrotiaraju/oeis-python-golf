# A000175

> Related to zeros of Bessel function.
> — [OEIS A000175](https://oeis.org/A000175)

Offset 1: 1, 1, 2, 11, 38, 946, 4580, 202738, 3786092, 261868876, …

### Python 3 — 119 bytes

```python
a=[0,n:=1]
while[print(a[n])]:n+=1;a+=sum(max(w:=a[k]*a[-k],*[w:=w*r**(k%r>n%r)for r in range(1,n)])for k in range(n)),
```

**How it works**

- The terms are the constant terms of the Rayleigh polynomials:
  a(n) = 4^n·Π(n)·σ_n, where σ_n = Σ j_k^(−2n) runs over the positive zeros
  j_k of J₀ and Π(n) = ∏_{r≤n} r^⌊n/r⌋ (the Mathematica and PARI programs on
  the OEIS page compute exactly this, as coefficients of J₁(x)/(2J₀(x))).
- y = J₁/J₀ = 2Σσ_n x^(2n−1) satisfies the Riccati equation
  y′ = 1 − y/x + y², which gives σ₁ = 1/4 and n·σ_n = Σ_{k=1}^{n−1} σ_k σ_{n−k}.
  So b_n = 4^n σ_n has b₁ = 1 and n·b_n = Σ b_k b_{n−k}.
- Putting a(n) = Π(n)·b_n into that recurrence:
  a(n) = Σ_{k=1}^{n−1} a(k)·a(n−k)·Π(n)/(n·Π(k)·Π(n−k)). The exponent of r
  in Π(n)/(Π(k)Π(n−k)) is ⌊n/r⌋ − ⌊k/r⌋ − ⌊(n−k)/r⌋, which is 1 when adding
  k and n−k carries in the last base-r digit, that is when k mod r > n mod r,
  and 0 otherwise. For r = n it is always 1 and cancels the 1/n; for r > n
  it is 0. Hence
  a(n) = Σ_{k=1}^{n−1} a(k)·a(n−k)·∏_{r<n, k mod r > n mod r} r,
  all in integers (Herman Jamke's `phi2` on the OEIS page at v = 0).
- The product needs no `math.prod`: `max(w:=a[k]*a[-k],*[w:=w*r**(…)for r in …])`
  keeps a running product in `w`, and since every factor is at least 1 the
  running products never decrease, so their maximum is the last one. The
  factor `r**(k%r>n%r)` (instead of an `if` filter) keeps the list non-empty,
  so `max` never gets a lone int. 3 bytes under `import math` and
  `math.prod(…)`.
- `a[0] = 0` lets k run over `range(n)`, and `a[-k]` is a(n−k) because `a`
  holds a(0)…a(n−1) when a(n) is being built.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (100 terms) prints in under a second; about 540 terms come out in 60 s,
  and the program stops after a(566), when the next term passes the
  4300-digit int-to-str limit of Python 3.11+. The bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000175), CC BY-SA 4.0.
