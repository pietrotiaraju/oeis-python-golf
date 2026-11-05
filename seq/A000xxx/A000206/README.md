# A000206

> Even sequences with period 2n.
> — [OEIS A000206](https://oeis.org/A000206)

Offset 0: 1, 1, 3, 4, 12, 22, 71, 181, 618, 1957, 6966, 24367, 89010, …

### Python 3 — 122 bytes

```python
import math
n=0
while[print(-~sum((3-n%2<<n)+2**((2-n%2>>n%(g:=math.gcd(j,2*n)))+g)for j in range(2*n))//(n*16or 1))]:n+=1
```

**How it works**

a(n) counts the binary strings of length 2n with an even number of 1s, up to
rotation, reversal and complementing every bit (a brute-force count of these
orbits matches the b-file for n ≤ 7). Burnside's lemma over the 8n symmetries,
with the parity filter written as (1 + (−1)^weight)/2, gives 16n·a(n) as a sum
over the symmetries of (fixed strings) + (fixed strings counted with sign
(−1)^weight).

- **Rotations.** Rotation by j splits the 2n positions into g = gcd(j, 2n)
  cycles of length k = 2n/g. On its own it fixes 2^g strings, and the signed
  count is 2^g if k is even, else 0. With complement, every cycle has to
  alternate, so k must be even; then it fixes 2^g strings, each of weight n,
  and the signed count is (−1)^n·2^g. Per j that is 2^g·w with w = 1 if k is
  odd, w = 2 if k is even and n odd, w = 4 if both are even.
- **w as a shift.** k is even exactly when g divides n, so w = 2^X with
  X = (2 − n mod 2)·[g | n]. The program writes X as `2-n%2>>n%g`. When g does
  not divide n, n mod g = g/2 (because 2n/g is odd), and that shift clears the
  value: for odd n, g/2 ≥ 1 and 1 >> 1 = 0; for even n, g carries one more
  factor 2 than n, so g ≥ 4, g/2 ≥ 2 and 2 >> 2 = 0.
- **Reflections.** The n reflections through two opposite beads fix 2^(n+1)
  strings and nothing else survives (fixed beads have no complement partner,
  and the signed count vanishes on the fixed points). The n reflections
  through edges contribute 2^n three times plus (−1)^n·2^n. In all,
  n·2^n·(5 + (−1)^n), spread over the 2n values of j as `3-n%2<<n` each.
- **n = 0.** As in [A000011](../A000011/): the divisor is `(n*16or 1)` and
  `-~` adds 1, which the floor division drops for n ≥ 1 because the total is
  exactly 16n·a(n). For n = 0 the range is empty and 1 // 1 = 1.

The result is the OEIS formula of Randall L Rathbun (a(n) = A000011(2n)/2 for
odd n, plus the A000011(n) correction for even n) merged into one divisor sum:
2·Σ_{d|n} φ(2d)·2^(n/d) equals the even-d part of Σ_{d|2n} φ(2d)·2^(2n/d), so
the even-n correction becomes the extra factor 2 in w.

**Notes**

- `(1<<(g:=math.gcd(j,2*n))+(2>>n%2+n%g))` for the rotation term is the same
  length.
- Summing over m in (2n, n), with the second one only for even n, as two
  A000011-style sums (`for m in(2*n,~n%2*n)for j in range(m)`) is 133 bytes;
  `(1+(n%g<1))**(2-n%2)<<g` for w is 130.
- Storing p = 2 − n mod 2 once (`while[p:=2-n%2,print(…)]`) saves 6 bytes
  inside and costs 9.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000206), CC BY-SA 4.0.
