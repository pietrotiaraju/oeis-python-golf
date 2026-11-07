# A000810

> Expansion of e.g.f. (sin x + cos x)/cos 3x.
> — [OEIS A000810](https://oeis.org/A000810)

Offset 0: 1, 1, 8, 26, 352, 1936, 38528, 297296, 7869952, 78098176, 2583554048, 31336418816, …

### Python 3 — 71 bytes

```python
r=[]
while[print(abs(s:=4**len(r)-3*sum(r)))]:r=[s:=s+x*6for x in[0]+r]
```

**How it works**

- Write F(x) = (cos x + sin x)/cos 3x = Σ a(n)·xⁿ/n!. Replacing x by ix
  in the even part and by ix (then dividing by i) in the odd part
  multiplies the n-th coefficient by (−1)^⌊n/2⌋ and turns cos into cosh
  and sin into sinh. Since sec 3x is even, the twisted series is
  (cosh x + sinh x)·sech 3x = eˣ·sech 3x = 2e^(4x)/(1 + e^(6x)), whose
  coefficients are d(n) = (−1)^⌊n/2⌋·a(n).
- So (1 + e^(6x))·D(x) = 2e^(4x), that is
  d(n) + Σ_j C(n,j)·6^j·d(n−j) = 2·4ⁿ.
- The binomial sum is the end of a Seidel triangle: row n starts at
  T(n,0) = d(n) and T(n,k) = T(n,k−1) + 6·T(n−1,k−1). Then
  T(n,k) = Σ_j C(k,j)·6^j·d(n−j), and the row ends at
  T(n,n) = d(n) + 6·(sum of row n−1). Hence
  d(n) = 4ⁿ − 3·(sum of row n−1): the new term needs only the previous
  row.
- In the program `r` is row n−1 (so `len(r)` is n),
  `s:=4**len(r)-3*sum(r)` is d(n), and `[s:=s+x*6for x in[0]+r]` builds
  row n from it (the leading 0 keeps s = d(n) as the first entry, the
  walrus carries the running sum).
- Printing |d(n)| is right because a(n) ≥ 0 for every n: the
  Seidel–Entringer–Arnold triangle [A008280](https://oeis.org/A008280)
  has e.g.f. (cos x + sin x)/cos(x + y), and y = 2x gives
  a(n) = Σ_m C(n,m)·2ⁿ⁻ᵐ·T(n,m), a sum of nonnegative terms.

**Notes**

- The even terms are [A000436](../A000436/) (cos x/cos 3x).
- Row n has n+1 entries, so a(n) costs about n big-integer additions;
  the whole b-file (201 terms) prints in a few hundredths of a second.
  The bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1431) (about 2.5 s here).
- `4**len(r)` is 1 byte under a separate power `p` (`;p=1`, `p*=4;`).
  R. J. Mathar's recurrence with binomials (as on the A000436 page) is
  over 100 bytes, and the weighted boustrophedon of
  [A000187](../A000187/) only gives sec 3x times an even or an odd
  function, not cos x + sin x.
- `x*6for`: a digit followed by a keyword needs no space (only a
  SyntaxWarning on stderr).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000810), CC BY-SA 4.0.
