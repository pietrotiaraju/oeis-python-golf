# A001770

> Numbers k such that 5*2^k - 1 is prime.
> — [OEIS A001770](https://oeis.org/A001770)

Offset 1: 2, 4, 8, 10, 12, 14, 18, 32, 48, 54, 72, 148, 184, 248, 270, 274, 420, 1340, …

### Python 3 — 68 bytes

```python
k=s=0
while[s or print(k+2)]:k+=2;s=724;exec('s=s*s%~-(20<<k)-2;'*k)
```

**How it works**

- The Lucas–Lehmer–Riesel test. Let N = h·2ⁿ − 1 with h odd and h < 2ⁿ,
  u₀ = V_h(4) = (2 + √3)ʰ + (2 − √3)ʰ and uᵢ₊₁ = uᵢ² − 2. If 3 does not
  divide N, then N is prime exactly when N divides uₙ₋₂ (Riesel 1969;
  Rödseth 1994 states it for any P with Jacobi symbols (P − 2 | N) = 1 and
  (P + 2 | N) = −1, and for P = 4 these are (2 | N) = 1, true because
  N ≡ 7 mod 8 when n ≥ 3, and (3 | N) = −1, true by reciprocity because
  N ≡ 3 mod 4 and N ≡ 1 mod 3). Here h = 5 and V₅(4) = 724.
- For odd n, 5·2ⁿ ≡ 1 mod 3, so 3 divides N > 3 and N is composite. For
  even n, N = 5·4ⁿᐟ² − 1 ≡ 1 mod 3. So only even n are tried (`k+=2`), and
  those are exactly the n where the theorem applies once 2ⁿ > 5.
- k is n − 2, the number of squarings: `'s=s*s%~-(20<<k)-2;'*k` runs
  them, with `20<<k` = 5·2ⁿ and `~-x` = x − 1. As in
  [A000043](../../A000xxx/A000043/), `s*s%N-2` reduces before subtracting,
  so s stays in −2 … N − 3, whose only multiple of N is 0, and
  `s or print(k+2)` prints n exactly when N divides uₙ₋₂.
- n = 2 (N = 19, prime) lies below the theorem (2² < 5): `k=s=0` makes the
  first loop condition see s = 0 and print 2 before any test runs. From
  n = 4 on, 2ⁿ > 5.

**Why a passing N is prime**

If N divides uₙ₋₂, take a prime q | N (q ≠ 2, 3). With ω = 2 + √3, which
has norm ω(2 − √3) = 1, uₙ₋₂ = ω^(5·2ⁿ⁻²) + ω^(−5·2ⁿ⁻²) ≡ 0 gives
ω^(5·2ⁿ⁻¹) ≡ −1 mod q, so ω⁵ has order exactly 2ⁿ in the norm-1 group of
𝔽_q[√3], whose order is q − 1 or q + 1. Every prime factor of N is then
±1 mod 2ⁿ. Since N ≡ −1 mod 2ⁿ, a composite N would need a factor ≡ +1 and
one ≡ −1 (product ≥ (2ⁿ + 1)(2ⁿ − 1) = 4ⁿ − 1) or three factors ≡ −1
(product ≥ (2ⁿ − 1)³); both exceed N = 5·2ⁿ − 1 when n ≥ 3. The converse,
that a prime N passes, is where the Jacobi symbols above come in (Riesel,
Rödseth).

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each n
  costs n − 2 squarings modulo an n-bit number: 1340 (18 terms) prints
  after about 10 s here, 2170 (25 terms) after 31 s, 2704 (29 terms) after
  56 s. The next term, 13510, would take hours. The bar is 25 terms in
  90 s; the b-file's 40 terms reach 1194164.
- The string handed to `exec` is about 19·n bytes; compiling it is part of
  the cost, but a `for` loop costs 10 bytes more.
- Riesel's paper: H. Riesel, Lucasian criteria for the primality of
  N = h·2ⁿ − 1, Math. Comp. 23 (1969) 869–875. Rödseth: Ø. J. Rödseth, A
  note on primality tests for N = h·2ⁿ − 1, BIT 34 (1994) 451–454.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001770), CC BY-SA 4.0.
