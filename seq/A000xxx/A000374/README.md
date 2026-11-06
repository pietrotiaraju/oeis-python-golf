# A000374

> Number of cycles (mod n) under doubling map.
> — [OEIS A000374](https://oeis.org/A000374)

Offset 1: 1, 1, 2, 1, 2, 2, 3, 1, 3, 2, 2, 2, 2, 3, 5, 1, 3, 3, 2, 2, …

### Python 3 — 77 bytes

```python
n=1
while r:=range(n):print(len({min((x<<j+n)%n for j in r)for x in r}));n+=1
```

**How it works**

- Under x ↦ 2x mod n every residue runs into a cycle. For each x the
  program takes the smallest element of the cycle it reaches, and the
  number of distinct such minima is the number of cycles.
- `(x<<j+n)%n` is x·2^(n+j) mod n (`+` binds tighter than `<<`). Write
  n = 2ᵏ·m with m odd: after k ≤ log₂ n < n steps every orbit is inside the
  multiples of 2ᵏ, where doubling is a permutation, so x·2ⁿ is already on
  the cycle. The cycle has at most m ≤ n elements, so the n values for
  j = 0…n−1 run through all of it, and their minimum is the cycle's
  minimum.
- Every cycle is reached by its own elements, and different cycles have
  different minima, so `len({…})` is exactly a(n).
- `r` names `range(n)` in the loop condition (never empty, since n ≥ 1)
  and serves for both x and j.

**Notes**

- Exact integers, so every term is right.
- Same idea, longer: `while[print(…)]` with two `range(n)` is 80 bytes;
  counting the x that equal the minimum of their own forward orbit,
  `sum(x==min((x<<j+1)%n for j in r)for x in r)`, is 78; and
  `x*2**j%n for j in range(n,2*n)` is 82.
- Burnside over the powers of 2 (Σ gcd(2ʲ − 1, n) over one period, divided
  by the period) is exact too, but finding the period of 2 modulo the odd
  part costs more bytes than it saves.
- Term n does n² shifts of up to 2n bits, so the program prints about 640
  terms in 60 s. The bar is 480 terms; the b-file has 10000.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000374), CC BY-SA 4.0.
