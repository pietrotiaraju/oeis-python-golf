# A000329

> Nearest integer to b(n), where b(n) = tan(b(n-1)), b(0) = 1.
> — [OEIS A000329](https://oeis.org/A000329)

Offset 0: 1, 2, 75, -1, -1, -2, 1, 2, 31, -1, …

### Python 3 — 267 bytes

```python
P=5;m=0
def G(u):
 a=(P//5+(u>>P)**2)*V;b=2*a
 for c in range(b-3*V,0,-2*V):a,b=c+u*u//-a//(a*b>0),c-u*u//b
 return u*V//a//(a*b>0),u*V//b
while 1:
 P*=2;l=h=V=1<<P;H=V//2;k=0
 try:
  while 0<=l+H^h+H<V:m+=k==m!=print(l+H>>P);l,*_,h=sorted(G(l)+G(h+1));k+=1
 except:0
```

**How it works**

- This is the [A000319](../A000319/) program with the rounding moved
  half a unit: the nearest integer to b is ⌊b + ½⌋, and with V = 2^P and
  H = V/2 the interval [l, h+1) that holds V·b(k) gives
  V·(b(k) + ½) ∈ [l+H, h+H+1). When `l+H` and `h+H` have the same integer
  part (`0<=l+H^h+H<V`; `+` binds tighter than `^`), `l+H>>P` is a(k).
- `G(u)` encloses V·tan(u/V) by Lambert's continued fraction
  tan x = x/(1 − x²/(3 − x²/(5 − …))), evaluated from the bottom up in
  integers: with R_j = V·r_j, R_j = (2j−1)V − u²/R_{j+1} and
  V·tan x = uV/R_1. The start [NV, 2NV] with N = P//5 + ⌊x⌋² is a valid
  enclosure of the tail, because N² ≥ x² + 1 forces every r_j, j ≥ N,
  into [j, 2j−1] (r_{j+1} ≥ j+1 gives x²/r_{j+1} ≤ j−1).
- Each level rounds its lower end down (`c+u*u//-a`) and its upper end up
  (`c-u*u//b`), which is right because R ↦ c − u²/R increases on each
  side of 0; `//(a*b>0)` raises ZeroDivisionError if an interval touches
  or straddles 0.
- The four values from both ends are sorted and their extremes become the
  new l, h. tan is increasing on [l/V, (h+1)/V] unless a pole lies
  inside; that interval is shorter than 1 (the rounding test passed), so a
  pole would make the two end values differ by cot s + cot t ≥ 2 cot ½ > 3
  and the next test fails before anything is printed.
- On a failed test or a ZeroDivisionError the outer loop doubles P and
  recomputes from b(0); m counts the terms already printed, so
  `m+=k==m!=print(…)` prints each term once.

**Notes**

- What is assumed: higher precision shrinks every enclosure to a point, so
  each term is eventually decided unless b(k) is exactly a half-integer,
  or a zero of one of the tails r_j (then the sign check fails forever).
  This is countably many points; it cannot be proved that the orbit
  misses them, but if it hit one the program would only stall, never
  print a wrong value.
- Precision runs 10, 20, …, 640 bits; about 505 bits suffice for
  n ≤ 10000. The whole b-file (10001 terms) prints in about 21 s here;
  the bar is the whole b-file.
- Floats fail early: iterating `math.tan` loses the orbit by n = 14.
- Writing `V//2` in place of `H` three times is 2 bytes longer than
  `;H=V//2`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 267 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000329), CC BY-SA 4.0.
