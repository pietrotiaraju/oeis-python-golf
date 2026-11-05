# A000121

> Number of representations of n as a sum of Fibonacci numbers (1 is allowed
> twice as a part).
> — [OEIS A000121](https://oeis.org/A000121)

Offset 0: 1, 2, 2, 3, 3, 3, 4, 3, 4, 5, 4, 5, 4, 4, 6, 5, 6, 6, 5, 6, 4, …

### Python 3 — 74 bytes

```python
*l,c=1,0
while[*map(print,l[c:])]:c=-len(l)-c;l+=map(sum,zip(l,l[~c::-1]))
```

**How it works**

- a(n) is the coefficient of xⁿ in Pₖ = (1 + x^F₁)(1 + x^F₂)⋯(1 + x^Fₖ)
  with F₁ = F₂ = 1, for any k with n < Fₖ₊₁ (the later factors only touch
  higher powers). Pₖ has degree F₁ + ⋯ + Fₖ = Fₖ₊₂ − 1 and is a
  palindrome, being a product of palindromes 1 + xᵐ.
- For Fₖ₊₁ ≤ n < Fₖ₊₂ write n = Fₖ₊₁ + j with 0 ≤ j < Fₖ. Then
  a(n) = [xⁿ]Pₖ₊₁ = [xⁿ]Pₖ + [x^j]Pₖ, and the palindrome turns [xⁿ]Pₖ
  into [x^(Fₖ−1−j)]Pₖ. Both exponents are below Fₖ₊₁, so both are terms
  already known:

  **a(Fₖ₊₁ + j) = a(j) + a(Fₖ − 1 − j)** for 0 ≤ j < Fₖ.

  So each new block of Fₖ terms is the first Fₖ terms plus the same terms
  reversed: 1 | 2 | 2 | 3 3 | 3 4 3 | 4 5 4 5 4 | ….
- `l` holds a(0) … a(Fₖ₊₂ − 1) and `c` is minus the length of the last
  block, so `l[c:]` is the block just made and gets printed in the loop
  condition (a list of `None`s, never empty, so always true).
  `c=-len(l)-c` makes it minus the next block's length Fₖ₊₁ = Fₖ₊₂ − Fₖ,
  and `l[~c::-1]` is a(Fₖ₊₁ − 1) down to a(0).
- `zip` stops at the shorter list, the reversed slice, so it pairs exactly
  a(j) with a(Fₖ₊₁ − 1 − j). `l+=map(…)` extends `l` while `zip` is still
  reading it; that is safe because only the first Fₖ₊₁ entries are read.
- The start `*l,c=1,0` (l = [1], c = 0) prints all of `l`, the lone a(0),
  and then acts as F₀ = 0: the next block has length 1 − 0 = F₁.

**Notes**

- Exact integer arithmetic and a proved identity, so the program is right
  for every n. The list grows by a factor of about φ per block, so memory is
  the only limit.
- Keeping the whole polynomial and multiplying by 1 + x^b each step,
  `c=[*map(sum,zip(c+[0]*b,[0]*b+c))]`, then printing the settled
  coefficients `c[a:b]` with a, b stepping through the Fibonacci numbers,
  is 86 bytes.
- Tracking the block lengths with a Fibonacci pair instead of `len(l)`,
  `*l,a,b=1,0,-1` + `a,b=b,a+b`, is 77 bytes.
- The same identity as a recursive function,
  `f=lambda n,a=1,b=1:0**n or n<a+b and f(n-b)+f(a+b+~n)or f(n,b,a+b)`,
  is 94 bytes with the counting loop.
- The b-file has the 6766 terms a(0)..a(6765), all printed in about 0.1 s
  here; the bar is the whole b-file in 60 s. 50 001 terms also agree with
  a direct product expansion.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000121), CC BY-SA 4.0.
