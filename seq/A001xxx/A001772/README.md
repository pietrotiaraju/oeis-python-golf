# A001772

> Numbers k such that 11*2^k - 1 is prime.
> — [OEIS A001772](https://oeis.org/A001772)

Offset 1: 2, 26, 50, 54, 126, 134, 246, 354, 362, 950, 1310, 2498, 6926, …

### Python 3 — 72 bytes

```python
k=s=0
while[s or print(k+2)]:k+=2;s=1956244;exec('s=s*s%~-(44<<k)-2;'*k)
```

**How it works**

- The Lucas–Lehmer–Riesel test, as in [A001770](../A001770/) (5·2ⁿ − 1).
  Let N = h·2ⁿ − 1 with h odd and h < 2ⁿ, u₀ = V_h(4) = (2 + √3)ʰ +
  (2 − √3)ʰ and uᵢ₊₁ = uᵢ² − 2. If 3 does not divide N, then N is prime
  exactly when N divides uₙ₋₂ (Riesel 1969; Rödseth 1994 for any P with
  Jacobi symbols (P − 2 | N) = 1 and (P + 2 | N) = −1, which for P = 4 are
  (2 | N) = 1, true because N ≡ 7 mod 8 when n ≥ 3, and (3 | N) = −1, true
  by reciprocity because N ≡ 3 mod 4 and N ≡ 1 mod 3). Here h = 11 and
  V_11(4) = 1956244.
- 11 ≡ 2 mod 3, so for odd n, 11·2ⁿ ≡ 1 mod 3 and 3 divides N > 3:
  never prime. For even n, N ≡ 1 mod 3. So only even n are tried
  (`k+=2`), and for those the theorem applies once 2ⁿ > 11.
- k is n − 2 (even, so n is even), the number of squarings:
  `'s=s*s%~-(44<<k)-2;'*k` runs them, with `44<<k` = 11·2ⁿ and
  `~-x` = x − 1.
- As in [A000043](../../A000xxx/A000043/), `s*s%N-2` reduces before it
  subtracts, so s stays in −2 … N − 3, whose only multiple of N is 0, and
  the loop condition prints n exactly when N divides uₙ₋₂.
- n = 2 (N = 43, prime) lies below the theorem (2² < 11): `k=s=0` makes the
  first loop condition see s = 0 and print 2 before any test runs. From
  n = 4 on, 2ⁿ > 11.

**Why a passing N is prime**

If N divides uₙ₋₂, take a prime q | N (q ≠ 2, 3). With ω = 2 + √3, of norm
ω(2 − √3) = 1, uₙ₋₂ ≡ 0 gives ω^(11·2ⁿ⁻¹) ≡ −1 mod q, so ω^11 has order
exactly 2ⁿ in the norm-1 group of 𝔽_q[√3], whose order is q − 1 or q + 1.
So every prime factor of N is ±1 mod 2ⁿ. As N ≡ −1 mod 2ⁿ, a composite N
would need a factor ≡ +1 and one ≡ −1 (product ≥ 4ⁿ − 1) or three factors
≡ −1 (product ≥ (2ⁿ − 1)³); both exceed N = 11·2ⁿ − 1 once 2ⁿ > 11. The
converse, that a prime N passes, is where the Jacobi symbols come in.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each n
  costs n − 2 squarings modulo an n-bit number. 1310 (11 terms) prints after
  about 13 s here and 2498 (12 terms) after 55 s; the next term, 6926, would
  take hours. The bar is 11 terms in 30 s; the b-file's 24 terms reach
  1261478.
- Only 11 terms are required, so they would fit in a table shorter than the
  program: this record went through a review.
- H. Riesel, Lucasian criteria for the primality of N = h·2ⁿ − 1, Math.
  Comp. 23 (1969) 869–875; Ø. J. Rödseth, A note on primality tests for
  N = h·2ⁿ − 1, BIT 34 (1994) 451–454.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001772), CC BY-SA 4.0.
