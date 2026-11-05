# A000061

> Generalized tangent numbers d(n,1).
> — [OEIS A000061](https://oeis.org/A000061)

Offset 1: 1, 1, 2, 4, 4, 6, 8, 8, 12, 14, 14, 16, 20, 20, 24, 32, 24, 30, 38, 32, …

### Python 3 — 158 bytes

```python
h=lambda x:sum(sum(d for d in range(4,x-s*s+1,4)if x%d==s*s%d)+x*(s*s==x)-(s>1>x%s**2and h(x//s//s))for s in range(-x,x))
x=4
while[print((h(x)+10)//20)]:x+=4
```

**The formula**

Shanks defines d(a,1) through a value of an L-function: with χ(j) the Jacobi
symbol (a|j) for odd j and 0 for even j,
d(a,1) = (4a√a/π²)·L(2, χ) for a > 1, and half of that for a = 1. The program
never computes a Jacobi symbol. It uses a divisor-sum formula instead:

1. Write 4a = D·f² with D a fundamental discriminant. χ is the character of
   D with the primes of f removed, and the functional equation of L gives
   d(a,1) = g(4a) = ½·B₂,χ_D·f³·∏_{p|f}(1 − χ_D(p)/p²), where B₂,χ_D is a
   generalized Bernoulli number. The same expression defines g(N) for every
   discriminant N = D·f² > 0. For a = 1 it gives ½, which is why a(1) = 1 is
   special.
2. The Siegel–Zagier formula ζ_K(−1) = (1/60)·Σ σ((D − s²)/4) for real
   quadratic fields, extended to every discriminant N by Cohen's
   generalized class numbers H(2, N) (Cohen 1975), says that
   T(N) = Σ_{s² < N} σ((N − s²)/4) = 5·Σ_{e|f} g(D·e²) when N is not a
   square. When N = f² is a square there is an extra term:
   T(N) + N/2 − 1/12 = 5·Σ_{e|f} g(e²). That case was checked numerically
   here, for every square the b-file reaches. Terms with (N − s²)/4 not an
   integer count 0, so only s of the parity of N count.
3. That is T(N) = 5·Σ g(N/k²) over the k with k² | N, so Möbius inversion
   over square divisors recovers g, and a(n) = g(4n).

**How it works**

- `h(x)` is 20·g(x), worked out as 4·T(x) plus the square term, minus
  `h(x/k²)` for every k ≥ 2 with k² | x. Non-discriminants come out as 0 by
  themselves.
- The inner sum adds every multiple of 4 dividing x − s², which is
  4·σ((x − s²)/4). `x%d==s*s%d` is "d divides x − s²", and the empty range
  for s² ≥ x takes care of s outside −√x … √x.
- `x*(s*s==x)` is the square term: x for each of s = ±√x, so 2x in all.
  The true term is 4·(x/2 − 1/12) = 2x − 1/3; a constant added at every
  square only changes h(1), and Möbius inversion cancels it everywhere else.
- The same loop variable s, for s ≥ 2, also serves as the k of the
  recursion. `s>1>x%s**2and h(x//s//s)` checks s > 1 before it divides by
  s², so s = 0 never divides by zero.
- `range(-x,x)` misses s = +1 for x = 1, so h(1) is 1, not 2, and h(c²) ends
  up off by −μ(c), where μ is the Möbius function. For a(n) with n > 1, h(4n)
  is then 20·a(n), or 20·a(n) ± 1 when n is a square, and
  `(h(x)+10)//20` rounds that away. h(4) is 11, and 21//20 = 1 gives a(1) = 1
  even though g(4) = ½.
- x runs over 4, 8, 12, …, so h(x) gives the terms in order.
  `while[print(...)]:` prints in the loop condition: a list holding `None` is
  true.

**Notes**

- Exact integer arithmetic, so the program is right for every n, given the
  theorems above. A fast version of the same formula (σ from a sieve, memoized
  recursion) matches all 10000 terms of the b-file.
- Each term costs about x^1.5/3 steps with x = 4n, plus a few recursive calls
  for the square divisors of x. That is about 3300 terms a minute here; the
  bar for this sequence is 1000 terms in 60 s.
- `x%s**2and` makes CPython print a `SyntaxWarning` (invalid decimal
  literal) to stderr; it is still valid code.
- Shanks's own recipe (squarefree part b, a sum of Jacobi symbols for d(b,1),
  then a product over the primes of √(a/b)) needs the squarefree part, a
  Jacobi symbol and a factorization, and comes out longer.
- `x-s*s+1` and `-~x-s*s` are the same length.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 158 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000061), CC BY-SA 4.0.
