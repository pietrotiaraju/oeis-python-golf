# A000508

> Generalized class numbers c_(n,3).
> — [OEIS A000508](https://oeis.org/A000508)

Offset 1: 61, 2763, 38528, 249856, 1066590, 3487246, 9493504, 22634496, 48649086, 96448478, …

### Python 3 — 143 bytes

```python
D=[b:=0]
while 1:b+=2;D+=0,sum((v:=y*y%(2*b)-b)**5*(abs(v)-3*b)+5*b**3*v**3-3*b**5*v-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(D[b]>>(b>2))
```

**How it works**

- This is the Gauss-sum and odd-divisor inversion used in
  [A000362](../A000362/), at L(7) rather than L(5). With b=2n and
  v=y² mod 2b−b, the scaled odd-frequency sine polynomial is
  v⁵(|v|−3b)+5b³v³−3b⁵v.
- Indeed Σₖ odd sin(πkt)/k⁷ = π⁷(3t−5t³+3t⁵−t⁶)/2880 on [0,1].
  This follows by twice integrating the L(5) polynomial and using the
  zero endpoint values. Shifting t by 1 and using the odd symmetries
  yields the polynomial in v above.
- Summing over a complete residue system gives twice c_(n,3), together
  with contributions from proper odd divisors of n. The `D` lookup
  subtracts these exactly; index 0 is zero and odd indices are padding.
- At n=1 Shanks's Euler-number normalization is doubled. The final
  right shift preserves that first value, 61, and halves the later ones.

**Notes**

- Only integer powers and exact divisor inversion are used. Each new
  term takes O(n) arithmetic operations.
- The reference file is transcribed from the published entry because its
  linked b-file was unavailable during this addition.
- The reference file contains 21 terms from the published OEIS entry; the verification
  bar is 21 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 143 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000508), CC BY-SA 4.0.
