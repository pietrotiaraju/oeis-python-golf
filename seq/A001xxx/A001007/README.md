# A001007

> a(n) = ( Sum C(p,i); i=1,...,floor(2p/3) ) / p^2, where p = prime(n).
> — [OEIS A001007](https://oeis.org/A001007)

Offset 3: 1, 2, 15, 42, 421, 1331, 15119, 618765, 2155578, 98032875, 1290154807, …

### Python 3 — 77 bytes

```python
P=6;k=3
while k:=k+1:~P%k or print(((2**k+1)**k>>-k//3*-k)%~-2**k//k//k);P*=k
```

**How it works**

- Primes by Wilson's theorem, as in [A000040](../../A000xxx/A000040/):
  P = (k−1)! (it is 3! = 6 when k first becomes 4) and `~P%k` is 0 exactly
  when k divides (k−1)! + 1, i.e. when k is prime. Starting at k = 4 skips
  p = 2 and 3, where the quotient is not an integer (offset 3).
- The binomial sum is the digit sum of one big power. With B = 2ᵏ,
  (B+1)ᵏ = Σ C(k,i)·Bⁱ and every C(k,i) < B, so the digits do not overlap.
  Shifting right by k·⌈k/3⌉ bits (`-k//3*-k` is ⌈k/3⌉·k) drops the digits
  i < ⌈k/3⌉. As B ≡ 1 (mod B−1), the rest taken mod B−1 (`~-2**k` is 2ᵏ−1)
  is its digit sum Σ_{i≥⌈k/3⌉} C(k,i) = Σ_{i≤⌊2k/3⌋} C(k,i) by symmetry.
  That sum is at most 2ᵏ−1−k < B−1, so the remainder is the sum itself.
- The sum includes the term i = 0, so it is 1 + p²·a(n), and `//k//k`
  removes the 1 < p².
- Why p² divides Σ_{1≤i≤m} C(p,i), m = ⌊2p/3⌋: C(p,i) = (p/i)·C(p−1,i−1)
  ≡ p·(−1)ⁱ⁻¹/i (mod p²), so the sum is p times H_m − H_⌊m/2⌋ (mod p),
  with ⌊m/2⌋ = ⌊p/3⌋. Since 1/(p−i) ≡ −1/i and H_{p−1} ≡ 0, H_{p−1−j} ≡ H_j
  (mod p), and p−1−⌊p/3⌋ = ⌊2p/3⌋ for p > 3.

**Notes**

- Exact integer arithmetic.
- The power (2ᵏ+1)ᵏ has about k² bits (1.5 Mbit at p = 1223): the whole
  b-file (198 terms) prints in about 4 s; the bar is the whole b-file.
- The same sum with `from math import*` and
  `sum(map(comb,[k]*k,range(2*k//3+1)))` is about 20 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001007), CC BY-SA 4.0.
