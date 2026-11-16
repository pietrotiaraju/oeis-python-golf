# A001774

> Numbers k such that 17*2^k - 1 is prime.
> — [OEIS A001774](https://oeis.org/A001774)

Offset 1: 2, 4, 6, 16, 20, 36, 54, 60, 96, 124, 150, 252, 356, 460, 612, 654, …

### Python 3 — 75 bytes

```python
k=s=0
while[s or print(k+2)]:k+=2;s=5285770564;exec('s=s*s%~-(68<<k)-2;'*k)
```

**How it works**

- The Lucas–Lehmer–Riesel test, as in [A001770](../A001770/) (5·2ⁿ − 1).
  Let N = h·2ⁿ − 1 with h odd and h < 2ⁿ, u₀ = V_h(4) = (2 + √3)ʰ +
  (2 − √3)ʰ and uᵢ₊₁ = uᵢ² − 2. If 3 does not divide N, then N is prime
  exactly when N divides uₙ₋₂ (Riesel 1969; Rödseth 1994 for any P with
  Jacobi symbols (P − 2 | N) = 1 and (P + 2 | N) = −1, which for P = 4 are
  (2 | N) = 1, true because N ≡ 7 mod 8 when n ≥ 3, and (3 | N) = −1, true
  by reciprocity because N ≡ 3 mod 4 and N ≡ 1 mod 3). Here h = 17 and
  V_17(4) = 5285770564.
- 17 ≡ 2 mod 3, so for odd n, 17·2ⁿ ≡ 1 mod 3 and 3 divides N > 3:
  never prime. For even n, N ≡ 1 mod 3. So only even n are tried
  (`k+=2`), and for those the theorem applies once 2ⁿ > 17.
- k is n − 2 (even, so n is even), the number of squarings:
  `'s=s*s%~-(68<<k)-2;'*k` runs them, with `68<<k` = 17·2ⁿ and
  `~-x` = x − 1.
- As in [A000043](../../A000xxx/A000043/), `s*s%N-2` reduces before it
  subtracts, so s stays in −2 … N − 3, whose only multiple of N is 0, and
  the loop condition prints n exactly when N divides uₙ₋₂.
- Two n lie below the theorem (2ⁿ < 17). n = 2 (N = 67, prime): `k=s=0`
  makes the first loop condition see s = 0 and print 2 before any test runs.
  n = 4 (N = 271, prime): the program runs the test and it passes (as it
  must for a prime N whose Jacobi symbols are right; here it is checked
  directly), so 4 is printed. From n = 6 on, 2ⁿ > 17.

**Why a passing N is prime**

If N divides uₙ₋₂, take a prime q | N (q ≠ 2, 3). With ω = 2 + √3, of norm
ω(2 − √3) = 1, uₙ₋₂ ≡ 0 gives ω^(17·2ⁿ⁻¹) ≡ −1 mod q, so ω^17 has order
exactly 2ⁿ in the norm-1 group of 𝔽_q[√3], whose order is q − 1 or q + 1.
So every prime factor of N is ±1 mod 2ⁿ. As N ≡ −1 mod 2ⁿ, a composite N
would need a factor ≡ +1 and one ≡ −1 (product ≥ 4ⁿ − 1) or three factors
≡ −1 (product ≥ (2ⁿ − 1)³); both exceed N = 17·2ⁿ − 1 once 2ⁿ > 17. The
converse, that a prime N passes, is where the Jacobi symbols come in.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each n
  costs n − 2 squarings modulo an n-bit number. 1312 (22 terms) prints after
  about 9 s here; the next term, 3062, did not arrive within 80 s. The bar
  is 22 terms in 30 s; the b-file's 40 terms reach 605394.
- Only 22 terms are required, so they would fit in a table shorter than the
  program: this record went through a review.
- H. Riesel, Lucasian criteria for the primality of N = h·2ⁿ − 1, Math.
  Comp. 23 (1969) 869–875; Ø. J. Rödseth, A note on primality tests for
  N = h·2ⁿ − 1, BIT 34 (1994) 451–454.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001774), CC BY-SA 4.0.
