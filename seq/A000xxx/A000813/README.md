# A000813

> Expansion of (sin x + cos x)/cos 4x.
> — [OEIS A000813](https://oeis.org/A000813)

Offset 0: 1, 1, 15, 47, 1185, 6241, 230895, 1704527, 83860545, 796079041, 48942778575, …

### Python 3 — 71 bytes

```python
r=[]
while[print(abs(s:=5**len(r)-4*sum(r)))]:r=[s:=s+x*8for x in[0]+r]
```

**How it works**

- Write F(x) = (cos x + sin x)/cos 4x = Σ a(n)·xⁿ/n!. Replacing x by ix
  in the even part and by ix (then dividing by i) in the odd part
  multiplies the n-th coefficient by (−1)^⌊n/2⌋ and turns cos into cosh
  and sin into sinh. Since sec 4x is even, the twisted series is
  (cosh x + sinh x)·sech 4x = eˣ·sech 4x = 2e^(5x)/(1 + e^(8x)), whose
  coefficients are d(n) = (−1)^⌊n/2⌋·a(n).
- So (1 + e^(8x))·D(x) = 2e^(5x), that is
  d(n) + Σ_j C(n,j)·8^j·d(n−j) = 2·5ⁿ.
- The binomial sum is the end of a Seidel triangle: row n starts at
  T(n,0) = d(n) and T(n,k) = T(n,k−1) + 8·T(n−1,k−1). Then
  T(n,k) = Σ_j C(k,j)·8^j·d(n−j), and the row ends at
  T(n,n) = d(n) + 8·(sum of row n−1). Hence
  d(n) = 5ⁿ − 4·(sum of row n−1): the new term needs only the previous
  row.
- In the program `r` is row n−1 (so `len(r)` is n),
  `s:=5**len(r)-4*sum(r)` is d(n), and `[s:=s+x*8for x in[0]+r]` builds
  row n from it (the leading 0 keeps s = d(n) as the first entry, the
  walrus carries the running sum).
- Printing |d(n)| is right because a(n) ≥ 0 for every n: the
  Seidel–Entringer–Arnold triangle [A008280](https://oeis.org/A008280)
  has e.g.f. (cos x + sin x)/cos(x + y), and y = 3x gives
  a(n) = Σ_m C(n,m)·3ⁿ⁻ᵐ·T(n,m), a sum of nonnegative terms.

**Notes**

- Same program as [A000810](../A000810/) ((cos x + sin x)/cos 3x) with
  the constants for cos 4x.
- Row n has n+1 entries, so a(n) costs about n big-integer additions;
  the whole b-file (201 terms) prints in a few hundredths of a second.
  The bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1381) (about 2.5 s here).
- `x*8for`: a digit followed by a keyword needs no space (only a
  SyntaxWarning on stderr).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000813), CC BY-SA 4.0.
