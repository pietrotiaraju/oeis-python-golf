# A001454

> Number of permutations of length n with longest increasing subsequence of length 3.
> — [OEIS A001454](https://oeis.org/A001454)

Offset 3: 1, 9, 61, 381, 2332, 14337, 89497, 569794, 3704504, 24584693, …

### Python 3 — 100 bytes

```python
u,v=2,6;c=r=5
while[print(v-c)]:r+=1;u,v=v,((10*r*r-38*r+33)*v-9*(r-3)**2*u)//r**2;c=c*(4*r-10)//~-r
```

**Why the recurrence**

- Let uₖ(n) count the permutations of n whose longest increasing
  subsequence has length at most k. Then a(n) = u₃(n) − u₂(n), and
  u₂(n) is the Catalan number Cₙ (the 123-avoiding permutations).
- Gessel ("Symmetric functions and P-recursiveness", JCTA 53, 1990) proved

  u₃(n) = 2·Σₖ C(2k,k)·C(n,k)²·(3k² + 2k + 1 − n − 2nk) / ((k+1)²(k+2)(n−k+1)).

- Zeilberger's algorithm on this sum returns a rational certificate for a
  third-order recurrence Z, Jovovic's recurrence in
  [A005802](https://oeis.org/A005802). Over the base
  C(2k,k)·n!²/(k!²(n+4−k)!²) every term of the certificate identity is a
  rational function whose denominator is a power of k + 1 or k + 2 times a
  polynomial in n with no root n ≥ 0, so the identity holds at every
  0 ≤ k ≤ n + 4, all terms vanish outside, and Z holds for every n ≥ 0
  (natural boundaries; checked in exact arithmetic with SymPy).
- Z factors through Mihailovs's second-order recurrence (also in A005802)

  M(n): (n+4)²·u₃(n+2) = (10n² + 42n + 41)·u₃(n+1) − 9(n+1)²·u₃(n).

  Writing e(n) for M's left side minus its right side,
  Z = b(n)·e(n+1) + e(n)/(9(n+1)²) with
  b(n) = −(n+4)²(4n²+22n+31) / (9(n+1)²(n+2)²(4n²+30n+57)), which is
  never 0. Since Z(n) = 0, e(n + 1) is a fixed multiple of e(n), and
  e(0) = 16·2 − 41·1 + 9·1 = 0, so e(n) = 0 for every n: **M holds for
  all n ≥ 0.**

**How it works**

- `u`, `v` hold u₃(n − 1), u₃(n) and `c` is Cₙ, starting at n = 3 with
  u₃(2) = 2, u₃(3) = 6, C₃ = 5; each pass prints v − c = a(n).
- `r` is n + 2 (it starts at 5, the same as C₃, so `c=r=5`). In terms of r
  the recurrence for the next n is r²·u₃(n) =
  (10r² − 38r + 33)·u₃(n−1) − 9(r−3)²·u₃(n−2), and
  Cₙ = Cₙ₋₁·(4r − 10)/(r − 1); `~-r` is r − 1. Both divisions are exact
  because the results are integers.
- This shift gives the smallest constants: written in n itself, or with
  r = n + 1, the program is 102 bytes.

**Notes**

- Exact integer arithmetic; correct for every n by Gessel's theorem and
  the certificate above. a(4522) passes Python's 4300-digit int-to-str
  limit, after about 4500 terms in a few seconds.
- The general method of [A001455](../A001455/)–[A001458](../A001458/)
  (the hook-walk sum Σ f_λ² over shapes, by RSK) does this sequence in
  130 bytes, about 450 terms in 20 s here. Conway and Guttmann's binomial form
  of Gessel's sum, u₃(n) = Σ C(2k,k)C(n+1,k+1)C(n+2,k+1)/((n+1)²(n+2)),
  minus Cₙ with `math.comb`, is 130 bytes too.
- The b-file has 998 terms (n = 3 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001454), CC BY-SA 4.0.
