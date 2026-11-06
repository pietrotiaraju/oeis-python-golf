# A000131

> Number of asymmetrical dissections of n-gon.
> — [OEIS A000131](https://oeis.org/A000131)

Offset 7: 2, 5, 21, 61, 214, 669, 2240, 7330, 24695, 83257, 284928, …

These are the triangulations of a regular n-gon into n − 2 triangles that
have no symmetry except the identity. Two triangulations count as the same
when a rotation or reflection of the polygon takes one to the other. The
first ones appear at n = 7, hence the offset.

### Python 3 — 117 bytes

```python
c=n=1;L=c,
while[n>6==print((9*L[m:=3*n]+2*L[2*n]-6*c//n-6*(L[m//2]+L[n]-L[m-3]))//24)]:c=4*c-6*c//n;L+=*[0]*5,c;n+=1
```

**How it works**

- **The formula.** Write C(k) for the Catalan numbers
  ([A000108](../A000108/)), with C(x) = 0 when x is not an integer. Joseph
  Myers's formula in the OEIS entry, derived from Guy (1958), is
  2n·a(n) = C(n−2) − (n/2)·C(n/2−1) − n·C(⌊n/2⌋−1) − (n/3)·C(n/3−1) +
  n·C(n/4−1) + n·C(n/6−1). Multiplying by 6/n and splitting C(⌊n/2⌋−1) into
  its even-n and odd-n cases gives

  **12·a(n) = 6·C(n−2)/n − 9·C(n/2−1) − 6·C((n−3)/2) − 2·C(n/3−1) +
  6·C(n/4−1) + 6·C(n/6−1)**,

  where C(n/2−1) is only used for even n and C((n−3)/2) only for odd n. The
  same coefficients appear in Robert A. Russell's generating function in the
  entry.
- **The table.** `L` holds −2·C(k−1) at index 6k and 0 at every index
  that is not a multiple of 6. For d = 2, 3, 4, 6 the index ⌊6n/d⌋ is 3n,
  2n, ⌊3n/2⌋ and n. It is a multiple of 6, namely 6·(n/d), exactly when d
  divides n. If n = qd + r with 0 < r < d, then ⌊6n/d⌋ = 6q + ⌊6r/d⌋,
  and 1 ≤ ⌊6r/d⌋ ≤ 5 because d ≤ 6. So `L[3*n]`, `L[2*n]`, `L[3*n//2]`
  and `L[n]` are −2 times C(n/2−1), C(n/3−1), C(n/4−1) and C(n/6−1), and
  each one is 0 when d does not divide n, as the formula needs. The
  odd-n term is `L[3*n-3]`. For odd n, 3n − 3 = 6·(n−1)/2 holds
  −2·C((n−3)/2). For even n, 3n − 3 is odd, so the entry is 0. With
  `m:=3*n` (an assignment inside an index, Python 3.10+) these three
  lookups are written `L[m]`, `L[m//2]` and `L[m-3]`.
- **The Catalan numbers.** `c` is −2·C(n−2). Running the recurrence
  backwards gives C(−1) = −1/2, so the start is c = 1 at n = 1 and the
  scale −2 comes from that. As in A000108, one step multiplies by
  (4n−6)/n, written `c=4*c-6*c//n`. 6c/n is an integer (4c minus the next
  term), so `6*c//n` (read as `(6*c)//n`) is exact. It is also −2 times
  the formula's first term 6·C(n−2)/n, so the formula uses the same
  expression.
- **The sum.** Each term is −2 times its value in the formula, and the
  signs are flipped too. So
  `9*L[m]+2*L[2*n]-6*c//n-6*(L[m//2]+L[n]-L[m-3])` equals 24·a(n), and
  `//24` divides exactly.
- **The loop.** Each pass appends five zeros and the new c with
  `L+=*[0]*5,c` (a starred tuple after `+=`, Python 3.9+). `L` starts as the
  one-item tuple `c,`. After pass k it has 6k + 1 entries, and its last
  one, at index 6k, is −2·C(k−1). Index 0 is never read. A tuple is 1 byte
  shorter to start than `[c]`, and `+=` just builds a new tuple.
- `n>6==print(…)` is a chained comparison: n > 6 and 6 == print(…). For
  n ≤ 6 it stops at n > 6, so nothing is printed and the lookups past
  the end of `L` never run. The passes still fill `L` and step `c`.
  `[False]` is a non-empty list, so the loop never ends.

**Notes**

- Exact integer arithmetic. Correctness for every n rests on the formula
  above, which comes from Guy's count of dissections (1958). The first
  term with more than 4300 digits is a(7162). At that point `print` hits
  Python's int-to-str limit.
- The tuple is copied on every pass, so the time grows like n². The whole
  b-file (994 terms) still prints in about 0.2 s; the bar is the whole
  b-file in 60 s.
- Other versions that print the same terms:
  - computing 6c/n once per pass, before the guard, and using it twice:
    `while[d:=6*c//n,n>6==print(…-d-…)]:c=4*c-d;…`, also 117 bytes;
  - spacing 12 instead of 6 (`L[6*n]`, `L[4*n]`, `L[3*n]`, `L[2*n]`,
    `L[6*n-6]`, `[0]*11`): no division in the indexes, but the `m` trick
    no longer pays off, so 118 bytes;
  - without `c`, reading −2·C(n−2) back as `L[-1]` (`n=1;L=n,`,
    `d:=6*L[-1]//n`, `L+=*[0]*5,4*L[-1]-d`): 119 bytes;
  - with a list `L=[c]` instead of the tuple and without `m`: 119 bytes;
  - a dict of Catalan numbers read with `D.get(n/3,0)`, where a float key
    like 3.0 finds the int key 3: about 140 bytes. It also relies on floats
    (n/d is exact only below 2⁵³), which the rules do not accept.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000131), CC BY-SA 4.0.
