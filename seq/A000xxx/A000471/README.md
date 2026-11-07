# A000471

> a(n) = floor(sinh(n)).
> — [OEIS A000471](https://oeis.org/A000471)

Offset 0: 0, 1, 3, 10, 27, 74, 201, 548, 1490, 4051, …

### Python 3 — 86 bytes

```python
n=0
while 1:
 N=n;F=d=1
 while-N%F<n**d:d+=2;N=N*d*~-d+n**d;F*=d*~-d
 print(N//F);n+=1
```

**How it works**

- sinh n = Σ_{d odd} nᵈ/d!. The inner loop keeps the partial sum up to
  degree d as N/F with F = d!: start at N = n, F = d = 1, and each step
  raises d by 2, multiplies N and F by d(d−1) (`d*~-d`) and adds nᵈ to N.
- `-N%F` is F times the distance from N/F up to the next integer (0 when
  N/F is an integer). The loop stops once that distance is at least the
  last term t = nᵈ/d!, and then ⌊sinh n⌋ = ⌊N/F⌋, because the rest of the
  series is positive and smaller than t.
- Why the rest is smaller than t when the loop stops: the distance is
  below 1, so the stop needs t < 1. For odd d ≤ 2n − 1, AM–GM gives
  d! ≤ ((d+1)/2)ᵈ ≤ nᵈ, so t ≥ 1 there; hence d ≥ 2n + 1 at the stop.
  From there each further term is at most n²/((d+1)(d+2)) < 1/4 times the
  one before, so the tail is below t·(1/4 + 1/16 + …) = t/3.
- At n = 0 the bound `n**d` is 0 and the loop stops at once with N = 0.
- The loop ends for every n ≥ 1: sinh n is not an integer, since then
  eⁿ would be a root of z² − 2sz − 1 and so algebraic, against
  Hermite–Lindemann. The distance up therefore tends to a positive limit
  while t tends to 0.

**Notes**

- Same template as ⌊eⁿ⌋ in [A000149](../A000149/). Keeping nᵈ in a
  variable (`N=p=n;F=d=1`, `p*=n*n`) is 89 bytes; the form with
  `while -N%F` and `(d-1)` written out was 91.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints in under a second here; about 880 terms in
  60 s.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s.
- a(n) first has more than 4300 digits at n = 9902, far beyond what the
  program reaches in practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |
| 2026-11-07 | Python 3 | 86 | `d*~-d`, no space after `while` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000471), CC BY-SA 4.0.
