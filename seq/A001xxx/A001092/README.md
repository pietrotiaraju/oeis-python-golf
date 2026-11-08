# A001092

> Union of all numbers {p, q} where p and q are both primes or powers of primes and q = p+2.
> — [OEIS A001092](https://oeis.org/A001092)

Offset 1: 1, 2, 3, 4, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 41, 43, 47, 49, …

### Python 3 — 79 bytes

```python
s=k=0
while 1:k+=1;s+=s+all(d*d%k-d for d in range(2,k));s&4>0<s&17!=print(k-2)
```

**How it works**

- The data count 1 as a prime power (a(1) = 1, paired with 3), as in
  [A000961](https://oeis.org/A000961); the program does the same.
- k is 1 or a prime power exactly when Z/k has no idempotents other than
  0 and 1: by the Chinese remainder theorem a split k = uv with
  gcd(u, v) = 1 and u, v > 1 gives an idempotent e ≡ 1 (mod u),
  e ≡ 0 (mod v), while Z/pᵉ is a local ring and has none. So
  `all(d*d%k-d for d in range(2,k))` (d² ≢ d for every 2 ≤ d < k) is the
  test; it is also true for k = 1 and 2 (empty range).
- s is a shift register of those flags, bit i standing for k − i. When k
  arrives, k − 2 is printed if bit 2 is set and bit 0 or bit 4 is
  (k − 2 has a partner k or k − 4). `s&4>0<s&17!=print(k-2)` is the chain
  (s&4) > 0 < (s&17) ≠ None; print runs only when the first two hold, and
  an int is always ≠ None.
- Bits for k ≤ 0 are 0, so nothing below 1 is printed.

**Notes**

- Exact integer arithmetic; the only facts used are the idempotent test
  above and the definition.
- `all` stops at the first idempotent, so composites are cheap and the
  cost is about k steps per prime power. 1170–1340 terms print in 60 s (the
  b-file has 10 000), and the bar is 900.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001092), CC BY-SA 4.0.
