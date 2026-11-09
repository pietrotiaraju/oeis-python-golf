# A001371

> Number of n-bead necklaces with beads of 2 colors and primitive period n, when turning over is allowed.
> — [OEIS A001371](https://oeis.org/A001371)

Offset 0: 1, 2, 1, 2, 3, 6, 8, 16, 24, 42, 69, 124, 208, 378, 668, 1214, 2220, 4110, …

### Python 3 — 126 bytes

```python
import math
r=[n:=1]
while[print(r[-1])]:r+=sum(2**~-(c:=math.gcd(j,n))+2**(n-j%2>>1)-n*r[j]*(c==j)for j in range(n))//n,;n+=1
```

**How it works**

- **All bracelets.** By Burnside's lemma over the dihedral group, the number
  B(n) of binary bracelets of length n ([A000029](../../A000xxx/A000029/))
  satisfies n·B(n) = Σⱼ (2^(gcd(j, n) − 1) + 2^⌊(n − (j mod 2))/2⌋) over
  j = 0 … n − 1: the first part is half the sum over the rotations, the second
  half the sum over the reflections (for odd n each reflection has
  (n + 1)/2 cycles; for even n half of them have n/2 + 1 and half n/2). This
  is the sum of the A000029 program.
- **Primitive ones.** A bracelet of length n with primitive period d is a
  primitive bracelet of length d repeated n/d times, and this is a bijection
  for every d | n. So B(n) = Σ_{d|n} a(d) for n ≥ 1, and
  a(n) = B(n) − Σ a(d) over the divisors d < n (Möbius inversion, the formula
  of the entry, without the Möbius function).
- **One sum.** The divisors are found inside the Burnside sum: with
  c = gcd(j, n), c = j holds for 0 < j < n exactly when j divides n, and never
  for j = 0 (c = n). So each such j subtracts n·a(j), and the whole sum is
  n·a(n); `//n` is exact.
- `r` holds a(0), a(1), …, so `r[j]` is a(j) and `r[-1]` is the newest term;
  the start `r=[n:=1]` prints the conventional a(0) = 1 and sets n = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (401 terms, up to a(400)) prints in about 0.1 s; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 126 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001371), CC BY-SA 4.0.
