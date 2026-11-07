# A000968

> Sum of odd Fermat coefficients rounded to nearest integer.
> — [OEIS A000968](https://oeis.org/A000968)

Offset 1: 1, 1, 2, 4, 9, 20, 46, 105, 246, 583, 1393, 3355, 8133, 19825, 48554, 119412, 294761, 729980, 1813107, 4515225, …

### Python 3 — 54 bytes

```python
u,v,m=1,4,3
while[print(-~v//m+1>>1)]:u,v=v,3*v-u;m+=2
```

**How it works**

- As in [A000967](../A000967/), with m = 2n+1 the Fermat coefficient
  (n:c) = C(2n−c, c−1)/c is the coefficient of xᶜ in the Lucas polynomial
  L_m(x) = Σ m/(m−c)·C(m−c, c)·xᶜ, divided by m. The odd-c part of L_m is
  (L_m(1) − L_m(−1))/2. L_m(−1) follows L_m = L_{m−1} − L_{m−2} from 2, 1,
  so it has period 6: for odd m it is e = 1 when 3 ∤ m and e = −2 when 3 | m.
  So the sum is S = N/(2m) with N = L(m) − e, where L(m) = L_m(1) is the
  Lucas number.
- L(m) is even exactly when 3 | m, so N is always even and N + m is odd:
  S is never a half-integer and round(S) = ⌊(N + m)/(2m)⌋.
- The program drops e and prints ⌊(L(m) + 1 + m)/(2m)⌋, written
  `-~v//m+1>>1` (= ⌊(⌊(v+1)/m⌋ + 1)/2⌋). This is the same number:
  if 3 | m, L+1+m is one below N + m = L+2+m, and they could only differ if
  2m divided the odd L+2+m. If 3 ∤ m, L+1+m is two above N + m = L−1+m;
  the floors could only differ if 2m divided L+m+1 (odd) or L+m, and the
  latter needs m | L(m).
- No odd m > 1 divides L(m): let p be the least prime factor of m. If
  p | L(m), then p | F(2m) = F(m)L(m) and p ∤ F(m) (L² − 5F² = ±4), so the
  rank of apparition z(p) divides 2m but not m: z(p) = 2d with d | m and
  d > 1 (F(2) = 1), so z(p) ≥ 2p. But z(p) divides p ± 1 (and z(5) = 5 is
  odd), so z(p) ≤ p + 1, a contradiction.
- `u,v` are L(m−2), L(m), stepped by L(m+2) = 3L(m) − L(m−2), as in
  A000967; dropping e saves 13 bytes over `(v-1+3*(m%3<1)+m)//(2*m)`.

**Notes**

- Exact integer arithmetic; uses Lucas' formula and the lemma above (both
  proved, no conjecture). Also checked against the defining sum of
  Fractions for n ≤ 200.
- The b-file has 500 terms and all of them print in under 0.1 s; the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000968), CC BY-SA 4.0.
