# A000489

> Card matching: Coefficients B[n,3] of t^3 in the reduced hit polynomial A\[n,n,n\](t).
> — [OEIS A000489](https://oeis.org/A000489)

Offset 1: 1, 16, 435, 7136, 99350, 1234032, 14219212, 155251840, 1628202762, 16550991200, …

a(n) counts the arrangements of n A's, n B's and n C's in a row of 3n places,
cut into three blocks of n places, with exactly three letters in their own
block (an A in the first block, a B in the second, a C in the third).

### Python 3 — 132 bytes

```python
n=r=q=p=0
while 1:
 n+=1;s=0;w=1
 for j in range(n+4):s+=w*j*(~-j*(j-2)*(r*w+6*q*p)//2+j*j*w*w);r,q,p,w=q,p,w,w*(n-j)//-~j
 print(s)
```

**How it works**

- Record an arrangement as the 3×3 table M whose entry M_ik is the number
  of letters i in block k: rows and columns sum to n, the hits are the
  diagonal, and the table occurs in Π_k n!/(M_0k!·M_1k!·M_2k!) arrangements.
  Once the diagonal (d₁, d₂, d₃) is fixed, the entry x = M_01 determines the
  rest, and the count is
  S(d) = C(n,d₁)C(n,d₂)C(n,d₃)·Σ_x C(n−d₂, x)·C(n−d₁, x+d₂−d₃)·C(n−d₃, x+d₁−d₃),
  where a binomial is 0 exactly when an entry would be negative. This is
  the three-sum formula in the entry (Riordan 1958).
- Three hits means d is (1,1,1), a permutation of (3,0,0) (three of them)
  or of (2,1,0) (six), and renaming letters and blocks together shows the
  permutations give equal counts. With n·C(n−1, x) = (x+1)·C(n, x+1) and
  C(n,c)·C(n−c, m) = C(n, m+c)·C(m+c, c), every piece becomes a product of
  binomials C(n, ·) from row n alone; putting j for the largest lower index,
  a(n) = Σ_j C(n,j)·(3C(j,3)·C(n,j−3)·C(n,j) + 6(j−2)C(j,2)·C(n,j−2)·C(n,j−1)
  + j³·C(n,j)²)
  = Σ_j j·w·((j−1)(j−2)/2·(r·w + 6q·p) + j²w²),
  with w, p, q, r = C(n, j), C(n, j−1), C(n, j−2), C(n, j−3).
- The inner loop walks row n with that window: `r,q,p,w=q,p,w,w*(n-j)//-~j`
  shifts it and makes C(n, j+1) = C(n, j)·(n−j)/(j+1), an exact division.
  Past j = n the new entries are 0, so after `range(n+4)` the window is
  all zeros again and only `w=1` (that is C(n, 0)) needs resetting for the
  next row; `n=r=q=p=0` sets it up for the first.
- `~-j*(j-2)` is (j−1)(j−2), a product of two consecutive integers, so the
  `//2` is exact.

**Notes**

- Same length: `s=w=1` and `print(s-1)`. Mark van Hoeij's identity in
  the entry, a(n) = n²((27n³+54n²−57n+8)(n+2)Bₙ − (189n³+189n²−30n+16)(n−1)Bₙ₋₁)/96
  with the Baxter numbers B (A001181) and their order-2 recurrence, was the
  previous record at 162 bytes.
- Exact integer arithmetic, so the program is right for every n. A direct
  count over all tables M with trace 3 agrees with the b-file for n ≤ 8.
- Each term costs O(n) big-number products: about 2050 terms in 60 s here.
  The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(n) has about 0.9n digits, so the 4300-digit int-to-str limit is not
  reached in a minute.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 162 | first entry |
| 2026-11-07 | Python 3 | 132 | one sum over row n of Pascal's triangle |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000489), CC BY-SA 4.0.
