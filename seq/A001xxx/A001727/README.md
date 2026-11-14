# A001727

> Weight distribution of [64,42,8] 3rd-order Reed-Muller code of length 64.
> — [OEIS A001727](https://oeis.org/A001727)

Offset 0: 1, 0, 0, 0, 11160, 0, 1749888, 22855680, 232081500, 1717223424, 9366150528, … (finite: 33 terms)

### Python 3 — 136 bytes

```python
l=1,0,0,0,2604,0,291648,888832;Y=2**70;N=0;q=1
for a in l+(1828134,)+l[::-1]:N=N*(1+Y)**4+a*q;q*=(1-Y)**4
while N:print(N%Y>>22);N>>=140
```

**How it works**

The sequence is finite: a(n) is the number of words of weight 2n in the
third-order Reed–Muller code RM(3, 6), n = 0, …, 32 (every weight is
even). The program does not store these 33 numbers: it derives them from
the much smaller weight distribution of RM(2, 6).

- RM(3, 6) is the dual of RM(2, 6) (RM(r, m)^⊥ = RM(m−r−1, m);
  MacWilliams and Sloane, *The Theory of Error-Correcting Codes*, ch. 13,
  Thm. 4). So the MacWilliams identity gives its weight enumerator from
  the one of RM(2, 6), a code with 2^22 words:

  **Σ_w B_w y^w = 2^(−22) · Σ_w A_w (1+y)^(64−w) (1−y)^w,**

  where A_w is the distribution of RM(2, 6) and B_w the one wanted here.
- `l` holds A_w for w = 0, 4, …, 28; with the middle value 1828134 and the
  mirror image it is the whole RM(2, 6) list: 1 word of weight 0 and 64,
  2604 of weight 16 and 48, 291648 of 24 and 40, 888832 of 28 and 36 and
  1828134 of 32. This is [A001726](https://oeis.org/A001726), and a
  theorem (Sloane and Berlekamp 1970; MacWilliams and Sloane, ch. 15):
  A(2^5 ± 2^(5−h)) = 2^(h(h+1)) · ∏_{i=7−2h..6} (2^i − 1) / ∏_{i=1..h} (4^i − 1)
  for h = 1, 2, 3, and the remaining 2^22 − 2 − 2·(2604 + 291648 + 888832)
  words have weight 32. A Gray-code walk over all 2^22 words of RM(2, 6)
  gives the same counts.
- The polynomial is evaluated at the single integer y = Y = 2^70, by
  Horner's rule in two variables: after the k-th list entry,
  N = Σ_{j≤k} A_{4j} (1+Y)^(4(k−j)) (1−Y)^(4j), with `q` = (1−Y)^(4k).
  At the end N = Σ_w 2^22·B_w·Y^w exactly.
- Every coefficient 2^22·B_w is below 2^22·2^42 = 2^64 < Y, so N written
  in base Y = 2^70 has exactly these coefficients as digits: the 70-bit
  block w of N is 2^22·B_w. `N%Y>>22` reads B_w from the lowest block and
  `N>>=140` moves two blocks on, to the next even weight. B_64 = 1 is the
  top block, so N reaches 0 right after the 33rd term and the loop ends.

**Golf tricks**

- Only weights 4j occur in RM(2, 6), so the factors are fourth powers and
  one multiplication per list entry builds the whole sum; carrying
  q = (1−Y)^(4k) is a byte under writing `(1-Y)**i` with a counter.
- `while N:` stops by itself after the last term, 2 bytes under
  `exec("…"*33)`.

**Notes**

- Exact integer arithmetic; the inputs are the RM(2, 6) distribution, the
  duality RM(2, 6)^⊥ = RM(3, 6) and the MacWilliams identity.
- It prints the 33 terms (the whole b-file) and stops, in a few
  milliseconds. Writing the 33 terms out would take about 170 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 136 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001727), CC BY-SA 4.0.
