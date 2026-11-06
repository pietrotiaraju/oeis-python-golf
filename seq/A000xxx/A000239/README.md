# A000239

> One-half of number of permutations of [n] with exactly one run of adjacent
> symbols differing by 1.
> — [OEIS A000239](https://oeis.org/A000239)

Offset 1: 1, 1, 3, 8, 28, 143, 933, 7150, 62310, 607445, 6545935, 77232740,
989893248, 13692587323, …

### Python 3 — 100 bytes

```python
a=b=m=s=0;c,d=1,2
while[print(s or 1)]:m+=1;s+=c;a,b,c,d=b,c,d,m*(d-c-b+a)+4*d+3*a+2*(a+2*b+~m*c)//m
```

**How it works**

- A run is a maximal stretch of neighbours that differ by 1, like 3-2-1,
  4-5 and 7-6 in 3214576. Inside a permutation a run always goes straight up
  or straight down. Reversing a permutation keeps its runs and never gives
  the same permutation back (n ≥ 2), so the count is even and a(n) counts
  the pairs.
- For n ≥ 2, a(n) = A000130(2) + A000130(3) + … + A000130(n), where
  [A000130](../A000130/) counts (in pairs) the permutations with exactly one
  succession, that is, one pair of neighbours differing by 1. The proof is
  below.
- So the program is the [A000130](../A000130/) program plus a running sum.
  There `a,b,c,d` hold A000130(n−4) … A000130(n−1), `m` = n − 3, and each
  pass computes the next term with R. J. Mathar's recurrence; see that page
  for the recurrence and its proof.
- On pass k (k = 1, 2, …) the window holds A000130(k−1) … A000130(k+2) and
  `s` = A000130(0) + … + A000130(k), which is a(k) for k ≥ 2 (A000130(0) =
  A000130(1) = 0). `s+=c` adds A000130(k+1) for the next pass.
- On the first pass `s` is 0: the one-element permutation has no neighbours,
  so the sum gives 0. The OEIS lists a(1) = 1, and `s or 1` prints that.
  After that `s` ≥ 1, so `or 1` never changes it again.

**Why the first differences are A000130**

Ralf Stephan noticed in 2003 that the first differences "seem to be" in
A000130. They are, and it follows from collapsing the run:

- Take a permutation π of [n] with exactly one run, of length k ≥ 2, on the
  values v, …, v+k−1. Replace the run by v, v+1 in the same direction and
  lower every value above v+k−1 by k−2. The result π′ is a permutation of
  [n−k+2] in which v and v+1 are neighbours.
- π′ has no other succession. Two neighbours away from the run keep their
  difference if both are below v or both above the run, and otherwise
  differ by at least 3 in π and in π′. For an increasing run, the entry x just
  before it forms a succession with it exactly when x = v−1, in π and in π′
  alike. The entry y just after it does so when y = v+k in π, which is the
  same entry as y = v+2 in π′. A decreasing run is the mirror image.
- Going back, stretching the only succession of a permutation of
  [n−k+2] into a run of length k gives π. So the permutations of [n] whose
  only run has length k are exactly as many as the permutations of [n−k+2]
  with exactly one succession, 2·A000130(n−k+2). Summing over k = 2, …, n
  gives 2a(n) = 2(A000130(2) + … + A000130(n)).

Together with the proof of the A000130 recurrence on its page, the program
is right for every n ≥ 2, and a(1) = 1 is the special case above.

**Notes**

- The sum costs 12 bytes on top of A000130's 88: `s=` in the first chain,
  `s+=c;`, and ` or 1`. `s|1>>s` and `s+0**s` tie with `s or 1`. Summing
  inside the print, `print((s:=s+b)or 1)` with no `s+=c;`, is 1 byte
  longer.
- a(n) has a recurrence of its own that fits the first 300 terms,
  (n−3)a(n) = (n−3)(n+2)a(n−1) − 2(n²−3n+1)a(n−2) + 2n·a(n−3)
  + (n−1)(2n−7)a(n−4) − (n−1)(n−2)a(n−5) for n ≥ 7, but it needs a
  five-term window, five seeds and a separate a(1), so it comes out longer.
- Generating function: with z = x(1−x)/(1+x) and E(z) = Σ k!·zᵏ (the
  generating function of [A002464](https://oeis.org/A002464)),
  Σ a(n)xⁿ = x + ((1−z)E(z) − 1)/(1−x)³. It comes from A000130's
  x²/(1+x)²·E′(z) and z²E′(z) = (1−z)E(z) − 1.
- Checked: brute force over all permutations for n = 2, …, 10, and the
  first 300 terms against the sum of Robbins's inclusion–exclusion count of
  permutations with one succession ([A086852](https://oeis.org/A086852)).
- a(1559) has 4302 digits, past Python's 4300-digit limit for converting an
  int to a string, so `print` stops with a `ValueError` after the 1558 terms
  a(1)..a(1558), in under a second here. The b-file has the 40 terms
  a(1)..a(40); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000239), CC BY-SA 4.0.
