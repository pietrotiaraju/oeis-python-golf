# A000458

> a(0) = a(1) = 1; thereafter a(n) = sigma(a(n-1)) + sigma(a(n-2)).
> — [OEIS A000458](https://oeis.org/A000458)

Offset 0: 1, 1, 2, 4, 10, 25, 49, 88, 237, 500, …

### Python 3 — 134 bytes

```python
def s(n):
 p=t=1
 while p*p<n:
  p+=1;a=1
  while n%p<1:n//=p;a=a*p+1
  t*=a
 return t*(n+(n>1))
a=b=1
while[print(a)]:a,b=b,s(a)+s(b)
```

**How it works**

- **σ by trial division.** For m = ∏ pᵉ, σ(m) = ∏ (1 + p + … + pᵉ). The
  inner loop strips every factor p from n and builds 1 + p + … + pᵉ in
  `a` by `a=a*p+1` (Horner), and `t` collects the product. Composite
  trial divisors find nothing left to divide.
- **The bound.** The loop tests p + 1 while p² < n, with n the cofactor
  still left. So every p′ with p′² ≤ n is tried (then (p′−1)² < n), and
  when the loop stops every prime factor of n is above p ≥ √n: n is 1 or
  a prime, whose factor is n + 1. `n+(n>1)` gives 1 or n + 1.
- **The recurrence.** `a, b` are a(n), a(n+1); the tuple assignment reads
  both before overwriting them. The `a` inside `s` is local.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: the loop condition `p*p<=n`
  with `p=2` and the increment at the end of the body, the first
  version: 137 bytes. Without the √n bound (`while n>1:`) the function
  is 12 bytes shorter but has to reach the largest prime factor, about
  10¹⁰ already for a(0)…a(41): far too slow.
- Exact integer arithmetic, so the program is right for every n.
- The first 44 terms print in about 1.7 s here; a(44) needs σ(a(43)) and
  σ(a(42)) by trial division and does not come within 30 s. The b-file
  has 101 terms (up to a(100)); the bar is 40 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 146 | first entry |
| 2026-11-06 | Python 3 | 137 | combine the remaining-prime and exhausted-factor cases |
| 2026-11-07 | Python 3 | 134 | `p*p<n` tests p+1 before the increment |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000458), CC BY-SA 4.0.
