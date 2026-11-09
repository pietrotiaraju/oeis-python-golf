# A001208

> a(n) = solution to the postage stamp problem with 3 denominations and n stamps.
> — [OEIS A001208](https://oeis.org/A001208)

Offset 1: 3, 8, 15, 26, 35, 52, 69, 89, 112, 146, 172, 212, 259, 302, 354, 418, …

a(n) is the h-range n(h,3) for h = n: the largest N such that some set of
stamps 1 = a₁ < a₂ < a₃ pays every amount 1, 2, …, N with at most h stamps.
(Lunnon's "solution" is the first amount that cannot be paid, one more; the
OEIS data are the h-range, as its comment says.)

### Python 3 — 208 bytes

```python
f=lambda L,k,y:k and max(f([q:=s|q<<a for s in L],k-1,len(bin(q^q+1)))for a in range(y)if[q:=0])or y-4
n=0
while 1:n+=1;v=2*n//9;q=4*-~n//9;a=2*q-v+3;print(n<23and f([1]*-~n,3,4)or(n-v-q)*((v+2)*a-q-2)+v*a+q)
```

**How it works**

- **n ≥ 23: the closed form.** Hofmeister determined n(h,3) for all h ≥ 20
  (J. Reine Angew. Math. 232 (1968) 77–101 and 339 (1983) 207–214; see
  Guy, *Unsolved Problems in Number Theory*, C12): a cubic in h whose lower
  coefficients depend on h mod 9. Challis gave an independent proof for
  h ≥ 81 ([arXiv:1311.1024](https://arxiv.org/abs/1311.1024), Theorem 101
  with Tables 103–105) and, by exhaustive computation up to h = 284,
  confirmed the same formula for every h ≥ 23 (his Section 7.1). The
  program uses it from n = 23 on, where both sources cover it.
- Challis's Table 105 writes the maximal set and its range, with
  h = 9t + r, as a payment with exactly h stamps:
  n(h,3) = q₃·a₃ + q₂·a₂ + q₁·1. Read off the nine rows, the counts are
  v = q₂ = ⌊2h/9⌋ and q = q₁ = ⌊4(h+1)/9⌋ (`4*-~n//9`), q₃ = h − v − q, and
  the stamps are a₂ = 2q − v + 3 and a₃ = (v+2)·a₂ − q − 2. For h = 27:
  v = 6, q = 12, the set {1, 21, 154} and 9·154 + 6·21 + 12 = 1524. Both
  sides are quasi-polynomials of degree 3 with period 9, so checking four
  periods proves the rewriting; it matches the b-file from h = 20 to 1000.
- **n ≤ 22: exhaustive search.** `f(L,k,y)` adds k more stamps to a set.
  `L[j]` is the bitmask of the amounts payable with at most j stamps
  (bit m set when m is payable), j = 0…h, and y is the set's range + 4.
  A new stamp a gives L′[j] = L[j] | L′[j−1] << a (use no a, or one a
  plus at most j−1 stamps), built in one pass by the walrus `q`
  (`if[q:=0]` resets it for each a, so L′[0] = L[0] = 1).
- The range is the lowest 0 bit of L[h] minus 1. After the pass `q` is
  L′[h], and `q^q+1` is 2^(range+2) − 1, so `len(bin(q^q+1))` is the new
  y, passed down with the list; a leaf (k = 0) returns y − 4.
- A stamp above range + 1 cannot help (the amount range + 1 would need a
  stamp no larger than it), so some optimal set has each stamp at most
  one more than the range of the smaller ones. The search tries
  0…range + 3 in any order, starting from the empty set (L = [1]·(h+1),
  y = 4, so the first stamp can be 1). A 0, a repeat or a useless large
  stamp only gives another set of at most three stamps, whose range is at
  most n(h,3), so the maximum is exactly n(h,3).

**Notes**

- The whole b-file (1000 terms) prints in about 0.2 s.
- The search alone (141 bytes with a plain loop) is correct for every n,
  but reaches only about 60 terms in a minute here; the formula is what
  carries the b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 208 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001208), CC BY-SA 4.0.
