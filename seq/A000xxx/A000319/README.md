# A000319

> a(n) = floor(b(n)), where b(n) = tan(b(n-1)), b(0)=1.
> — [OEIS A000319](https://oeis.org/A000319)

Offset 0: 1, 1, 74, -1, -2, -3, 0, 1, 30, -2, …

### Python 3 — 254 bytes

```python
P=5;m=0
def G(u):
 a=(P//5+(u>>P)**2)*V;b=2*a
 for c in range(b-3*V,0,-2*V):a,b=c+u*u//-a//(a*b>0),c-u*u//b
 return u*V//a//(a*b>0),u*V//b
while 1:
 P*=2;l=h=V=1<<P;k=0
 try:
  while 0<=l^h<V:m+=k==m!=print(l>>P);l,*_,h=sorted(G(l)+G(h+1));k+=1
 except:0
```

**How it works**

- Everything is integer interval arithmetic with V = 2^P. The pair l ≤ h
  says V·b(k) ∈ [l, h+1); it starts as l = h = V for b(0) = 1.
- `0<=l^h<V` holds when l and h have the same integer part (no XOR bit at
  position P or above, same sign), and then every point of the interval
  has floor `l>>P`, so that is a(k). `m+=k==m!=print(l>>P)` prints only
  when k equals the count m of terms already printed, and counts it.
- `G(u)` encloses V·tan(u/V) between its two outputs, using Lambert's
  continued fraction tan x = x/(1 − x²/(3 − x²/(5 − …))). With
  r_j = (2j−1) − x²/r_{j+1} and R_j = V·r_j this reads
  R_j = (2j−1)V − u²/R_{j+1}, and V·tan x = uV/R_1.
- The tail: N = P//5 + ⌊x⌋² satisfies N² ≥ x² + 1 (P ≥ 10, so P//5 ≥ 2),
  and then every r_j with j ≥ N lies in [j, 2j−1]: if r_{j+1} ≥ j+1 then
  x²/r_{j+1} ≤ (j²−1)/(j+1) = j−1. So [NV, 2NV] encloses R_N.
- Going down, R ↦ c − u²/R is increasing on each side of 0, so the lower
  end becomes `c+u*u//-a` (rounded down) and the upper end `c-u*u//b`
  (rounded up), valid when a and b have the same sign; `//(a*b>0)`
  divides by zero otherwise, at every level and once more for R_1. The
  last line gives ⌊uV/R⌋ at both ends, and V·tan x lies below the larger
  one plus 1.
- `sorted(G(l)+G(h+1))` takes the extremes of the four values. b(k) lies
  in [l/V, (h+1)/V], of length at most 1, and tan is increasing there
  unless it holds a pole, so the new l, h enclose V·b(k+1).
- A pole inside, at distances s and t with s + t ≤ 1, makes
  tan(l/V) − tan((h+1)/V) = cot s + cot t ≥ 2 cot ½ > 3, so the new l and h
  are more than V apart, the floor test fails at once, and nothing is
  printed from that wrong interval.
- When the floor test fails, or anything divides by zero (`except:0`),
  the outer loop doubles P and starts again from b(0); m remembers what was
  printed, so no term repeats and every printed term was decided by a
  rigorous enclosure.

**Notes**

- What is assumed: as P grows the enclosure of each b(k) shrinks to a
  point, so a(k) is eventually decided unless b(k) is an exact integer,
  or a zero of one of the tails r_j (then the sign check fails at every
  precision). These are countably many points and no one can prove the
  orbit avoids them (b(1) = tan 1 is transcendental by Lindemann, little
  is known beyond), but hitting one would only make the program stall: it
  never prints a wrong value.
- Precision runs 10, 20, …, 640 bits; about 505 bits carry the orbit to
  n = 10000 (the derivatives sec² b(k) multiply up). The chain has
  P//5 + ⌊b⌋² levels: P//5 brings the truncation error below 2^−P, ⌊b⌋²
  covers large arguments such as b(2) ≈ 74.7.
- The whole b-file (10001 terms, n = 0…10000) prints in about 20 s here;
  the bar is the whole b-file.
- Floats are useless: iterating `math.tan` gives a wrong floor already at
  n = 14. The standard library has no arbitrary-precision tan
  (`decimal` has only exp, ln, log10, sqrt).
- Checking the sign only once, for R_1, is 3 bytes shorter and also
  passes the b-file, but then a rounding step could in principle wrap an
  interval around 0 unnoticed, so the per-level check stays. A first
  version with a separate error estimate for the tail was 430 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 254 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000319), CC BY-SA 4.0.
