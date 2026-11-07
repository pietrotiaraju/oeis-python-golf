# A000773

> Number of numbers == 0 (mod 3) in range 2^n to 2^(n+1) with odd number of 1's in binary expansion.
> — [OEIS A000773](https://oeis.org/A000773)

Offset 1: 0, 0, 0, 1, 1, 6, 8, 29, 45, 130, 220, 561, 1001, 2366, 4368, 9829, 18565, 40410, …

### Python 3 — 46 bytes

```python
n=1
while[print((2**n+3-3**(n+1>>1))//6)]:n+=1
```

**How it works**

- Count m in [2ⁿ, 2ⁿ⁺¹) with a roots-of-unity filter: cube roots of 1
  for 3 | m, and ±1 for the parity of the bits. The bits below the top
  one contribute products of (1 ± ω^(2ⁱ)); since 2ⁱ mod 3 alternates
  1, 2 and (1+ω)(1+ω²) = 1, (1−ω)(1−ω²) = 3, this gives the OEIS formula
  a(n) = (2ⁿ − (−1)ⁿ − 3^⌈n/2⌉)/6.
- `n+1>>1` is ⌈n/2⌉. For n ≥ 1, 2ⁿ ≡ 2 or 4 and 3^⌈n/2⌉ ≡ 3 (mod 6), so
  X = 2ⁿ − 3^⌈n/2⌉ is 5 (mod 6) for odd n and 1 (mod 6) for even n. In
  both cases (X − (−1)ⁿ)/6 = ⌊(X + 3)/6⌋, which drops the sign term:
  `(2**n+3-3**(n+1>>1))//6`.

**Notes**

- Exact integer arithmetic.
- Adding the parity instead, `(2**n-3**(n+1>>1))//6+n%2`, is 2 bytes
  longer.
- The whole b-file (501 terms) prints at once; it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000773), CC BY-SA 4.0.
