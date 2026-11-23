# A002201

> Superior highly composite numbers: integers n > 1 for which there is an e > 0 such that d(n)/n^e >= d(k)/k^e for all k > 1, where the function d(n) counts the divisors of n (A000005).
> — [OEIS A002201](https://oeis.org/A002201)

Offset 1: 2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720, 1441440, 4324320, …

### Python 3 — 178 bytes

```python
n=O=1;F=2
while 1:
 if O==n:print(F);n+=1;B=[(0,1),(1,0)]
 u,v=map(sum,zip(*B));F=p=1;O=0
 while(p:=p+1)**u<2**v:
  k=F%p>0
  while(k+1)**v>p**u*k**v>0:k+=1;F*=p;O+=1
 B[O<n]=u,v
```

**How it works**

Every comparison is a comparison of integers at a rational exponent
t = u/v; no logarithm is ever approximated.

- **The maximizer for one e** (Ramanujan, 1915). d(k)/k^e is the product
  over primes of (a + 1)/p^(ae), a the exponent of p in k, so each prime
  can be optimized alone. Going from a − 1 to a multiplies the factor by
  (1 + 1/a)/p^e, which is > 1 exactly while p^e < 1 + 1/a, and 1 + 1/a
  decreases. So the best exponent is the number of a ≥ 1 with
  p^e < 1 + 1/a, unless p^e = 1 + 1/a for some a, a *critical* e,
  where two exponents tie. Call F(e) the product of p to these counts:
  for every non-critical e it is the only maximizer (and for e < 1 it is
  > 1, so "all k > 1" changes nothing).
- **Rational e are not critical**, except e = 1: p^(u/v) = (a+1)/a means
  p^u·a^v = (a+1)^v, and as a and a + 1 are coprime that forces a = 1,
  p^u = 2^v, p = 2, u = v. At t = u/v the test p^t < 1 + 1/a is
  `(a+1)**v>p**u*a**v`, exact.
- **The sequence.** As e decreases, F(e) only changes at critical
  values, by one prime factor at each one, unless two primes share a
  critical value (see below). Every superior highly composite number is
  F(e) on an open interval of e, and every interval contains rationals.
  So a(n) is F(t) for any rational t whose F(t) has Ω = n prime factors
  counted with multiplicity: the program searches such a t for
  n = 2, 3, …, and `n=O=1;F=2` sets up a(1) = 2.
- **The search** is a Stern–Brocot descent: `B` holds the bounds L, R
  (starting at 0/1 and 1/0), t = u/v is their mediant, and `B[O<n]=u,v`
  moves R down to t when Ω(F(t)) < n, L up when it is > n. Ω(F(t))
  only grows as t falls, so the t with Ω = n always stay strictly
  between L and R; the descent passes through every rational of
  (L, R) and the bracket shrinks to a point, so it lands in that open
  interval after finitely many steps. Each search restarts at the root,
  which keeps the fractions as simple as possible (u, v stay small).
- **F(t) and Ω.** The primes with p^t < 2 are the ones that occur
  (`(p:=p+1)**u<2**v`); for each, `k` counts the a with
  (a+1)^v > p^u·a^v while `F*=p` and `O+=1` record them.
- **No primality test.** When p is reached, F already holds every
  smaller prime r, with exponent at least j whenever r^j ≤ p: from
  r^(jt) ≤ p^t < 2 and (1 + 1/j)^j ≥ 2 follows r^t < 1 + 1/j. So a
  composite p divides F, a prime does not, and `k=F%p>0` starts the
  count at 1 for primes and makes `(k+1)**v>p**u*k**v>0` false at once
  for composites (the `>0` rejects k = 0).

**Ties.** If two primes p ≠ q ever had the same critical exponent
(ln(1 + 1/a)/ln p = ln(1 + 1/b)/ln q), Ω would jump by 2 there and both
p·N and q·N would be terms (the definition says ≥). No rational t then
has Ω equal to the count in between: the descent would close in on the
common exponent forever and the program would print nothing more. It
never prints a wrong term. Whether such a tie can happen is open: the
four exponentials conjecture says no, and the six exponentials theorem
rules out three equal exponents (Alaoglu and Erdős); the program
relies on neither. The run reaches a(400), so there is no tie up to
there.

**Notes**

- Exact integers: every printed term is right; past a tie (if one
  exists) nothing would be printed.
- The slow steps are pairs of critical exponents that are very close,
  or close to a simple fraction, such as a(212)/a(211) = 1019 and
  a(213)/a(212) = 1021, both just above 1/10: there the descent needs
  fractions like 142/1419. 300 terms come in about 11 s here and the
  whole b-file (400 terms, a(400) has 76 digits) in 28 s. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 178 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002201), CC BY-SA 4.0.
