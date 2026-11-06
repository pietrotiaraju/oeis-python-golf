# A000158

> Number of partitions into non-integral powers.
> — [OEIS A000158](https://oeis.org/A000158)

Offset 3: 1, 2, 8, 19, 41, 78, 134, 218, 339, 506, 730, 1023, 1397, 1884, 2477, …

### Python 3 — 172 bytes

```python
n=3
while F:={r:=n**49}:
 for x in range(-n**74,0,n**72):
  while r**3>x*x:r=(2*r+x*x//r//r)//3
  F|={r}
 print(sum(a<=b<=c<=r*n-a-b for a in F for b in F for c in F));n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the triples 1 ≤ x ≤ y ≤ z of
  integers with x^(2/3) + y^(2/3) + z^(2/3) ≤ n. This is the three-term
  version of [A000148](../A000148/), but the trick used there (cube the
  inequality once) does not close up for three cube roots, so this program
  rounds instead, with enough digits to be exact.
- With K = n⁴⁸, each k gets the integer F_k = ⌊K·k^(2/3)⌋, the integer cube
  root of k²·n¹⁴⁴. The loop runs x = −k·n⁷², k = n², …, 1, so x² = k²n¹⁴⁴
  directly; x is negative only so that k goes down.
- The cube root is integer Newton from above: r → ⌊(2r + ⌊x²/r²⌋)/3⌋ never
  drops below ⌊∛x²⌋ (AM–GM on r, r, x²/r²) and goes down strictly while
  r³ > x², so it stops exactly at the floor of the cube root. Going down in
  k, the root for k + 1 is a ready starting point above the root for k, and
  each k takes a few steps.
- r starts at n⁴⁹ = K·n. When k^(2/3) ≥ n the root is at least that, so r
  does not move and every such k puts the same n⁴⁹ into the set F. Below
  that the values are distinct (they are about K·(2/3)·k^(−1/3) ≫ 1 apart),
  so F holds one number per k with k^(2/3) < n, plus n⁴⁹, which can never
  be part of a counted triple. A triple needs z^(2/3) ≤ n − 2, so no k
  above n² is missed.
- After the loop r is the root for k = 1, that is K itself, so the bound
  K·n is `r*n`. The chain `a<=b<=c<=r*n-a-b` counts each multiset of
  three values once, which is each triple x ≤ y ≤ z once.
- `while F:={r:=n**49}:` resets r and F in the loop header: a non-empty set
  is true.

**Why rounding is exact**

Write s = x^(2/3) + y^(2/3) + z^(2/3). The test is F_x + F_y + F_z ≤ Kn.

- If s ≤ n, the sum of floors is at most Ks ≤ Kn, so the triple passes.
  This includes s = n exactly, as for (1, 1, 1) at n = 3 or (1, 8, 8) at
  n = 9.
- If s > n, the triple must fail, and here a gap is needed. θ = s − n is a
  nonzero algebraic integer in the field made by three real cube roots,
  of degree d ≤ 27. Its other conjugates are ζ₁x^(2/3) + ζ₂y^(2/3) +
  ζ₃z^(2/3) − n with ζᵢ cube roots of unity, each of absolute value at most
  s + n, and the product of all d conjugates (the norm) is a nonzero
  integer. So θ ≥ (s + n)^(−26), which is at least (2n + 1)^(−26) when
  s ≤ n + 1 (above n + 1 the gap is 1 anyway).
- Each floor loses less than 1, so the sum of floors is more than
  Ks − 3 ≥ Kn + K(2n + 1)^(−26) − 3. Since n⁴⁸ ≥ 3(2n + 1)²⁶ for every
  n ≥ 3 (at n = 3 the ratio is about 2.8, and it grows with n), this is
  more than Kn and the triple fails.

**Notes**

- Round n tries |F|³ ≈ n^4.5 triples. The program prints the whole
  b-file (41 terms) in about 40 s and 44 terms in 60 s. The bar is 35
  terms in 60 s.
- Taking k over `range(-n*n,0)` with `Y=k*k*n**144` costs 2 bytes more
  than stepping x by n⁷². Adding to F in the while condition
  (`or F.add(r)`) costs 3 more than the `F|={r}` line, and
  `combinations_with_replacement` with its import costs 29 more than the
  three loops.
- The test only needs n⁴⁸ ≥ 3(2n + 1)²⁶; any exponent from 48 up works for
  n ≥ 3, and they all cost the same bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000158), CC BY-SA 4.0.
