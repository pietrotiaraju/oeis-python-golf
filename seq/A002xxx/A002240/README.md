# A002240

> Numbers k such that 33*2^k - 1 is prime.
> — [OEIS A002240](https://oeis.org/A002240)

Offset 1: 2, 3, 6, 8, 10, 22, 35, 42, 43, 46, 56, 91, 102, 106, 142, 190, 208, …

### Python 3 — 128 bytes

```python
m=k=0;N=65
while 1:
 while pow(k*k+4,N//2,N)<2:k+=1
 a,s=2,k;exec('a,s=s,k*s+a;'*66+'a=a*a%N-2;'*m);a+2 or print(m+1);m+=1;N-=~N
```

**How it works**

- **Choosing P (Rödseth).** The Lucas–Lehmer–Riesel test: for N = h·2ⁿ − 1
  with h odd and h < 2ⁿ, and P with Jacobi symbols (P − 2 | N) = 1 and
  (P + 2 | N) = −1, N is prime exactly when N divides V_{h·2ⁿ⁻²}(P), where
  V₀ = 2, V₁ = P, Vⱼ₊₁ = P·Vⱼ − Vⱼ₋₁ (Riesel 1969 with P = 4 when 3 ∤ h;
  Rödseth 1994 for any such P). Here h = 33 is a multiple of 3, so N ≡ 2
  mod 3, (6 | N) = 1 and P = 4 fails: P must be found for each n. The
  program takes P = k² + 2, so that P − 2 = k² is a square, and
  `while pow(k*k+4,N//2,N)<2:k+=1` moves k on until (k² + 4)^((N−1)/2) mod
  N is neither 0 nor 1: for a prime N, Euler's criterion makes that
  exactly (k² + 4 | N) = −1. k is never reset, so each n starts where the
  last search stopped (any k with the right symbol will do).
- **The test, run on V(k, −1).** With P = k² + 2, V_j(P) = V₂ⱼ(k, −1),
  where V(k, −1) is xⱼ₊₁ = k·xⱼ + xⱼ₋₁ from x₀ = 2, x₁ = k. `a,s=2,k` and
  66 steps `a,s=s,k*s+a;` give a = V_66(k, −1) = V_33(P) (small numbers,
  no reduction needed); then m = n − 1 steps `a=a*a%N-2;` (V₂ⱼ = Vⱼ² − 2)
  give V_{33·2ⁿ⁻¹}(P) = V_((N+1)/2)(P) mod N. The program prints n when
  this is ≡ −2 mod N, which is the theorem's test one squaring later:
  V_((N+1)/2) = (V_((N+1)/4))² − 2.
- **Bookkeeping.** m = n − 1 counts the squarings and `print(m+1)` prints
  n; `N-=~N` turns N = 33·2ⁿ − 1 into 2N + 1 = 33·2ⁿ⁺¹ − 1, starting from
  N = 65 at n = 1. `a*a%N-2` reduces before subtracting, so after a
  squaring a lies in −2 … N − 3 and a ≡ −2 means a = −2; n = 1 is the one
  case without a squaring, and it is not a term (see the notes).

**Why it prints exactly the n with N prime**

Write α = (k + √(k² + 4))/2, a root of x² − kx − 1 (the other root is
−1/α). Then V_j(k² + 2) = α²ʲ + α⁻²ʲ, and the value the program tests
against −2 is VAL = α^(N+1) + α^−(N+1).

- *The search ends.* Let p be a prime factor of N. Of the k mod p, the
  conic y² − k² = 4 leaves (p + 1 − z)/2 ≥ 1 with k² + 4 a non-residue
  (z ≤ 2 counts the roots of k² + 4), and for such k the power
  (k² + 4)^((N−1)/2) is a non-residue mod p, since (N − 1)/2 is odd (N ≡ 3
  mod 4 once n ≥ 2): it is neither 0 nor 1. So the search stops within p
  steps. For a prime N it stops exactly at a k with (k² + 4 | N) = −1;
  such k exist and also make k² a non-zero square.
- *N prime ⇒ printed.* √(k² + 4) is not in GF(N), so the Frobenius map
  swaps the two roots: α^N = −1/α, α^(N+1) = −1 and VAL = −2. (This half
  needs neither 2ⁿ > h nor n ≥ 2.)
- *Printed ⇒ N prime.* Let q be a prime factor of N; VAL ≡ −2 (mod q)
  reads (α^(N+1) + 1)² ≡ 0, so α^(N+1) = −1 in GF(q²). If q divided
  k² + 4, α would be k/2 with α² = −1 and α^(N+1) = (−1)^((N+1)/2) = 1; so
  it does not, and as N + 1 = h·2ⁿ the order of α is a multiple of 2ⁿ⁺¹.
  It divides q − 1 if α ∈ GF(q), and 2(q + 1) otherwise (α^q = −1/α), so
  q ≡ ±1 mod 2ⁿ and q ≥ 2ⁿ − 1. A composite N has either two prime
  factors, one ≡ 1 and one ≡ −1 mod 2ⁿ (their product is N ≡ −1), so
  N ≥ (2ⁿ + 1)(2ⁿ − 1) = 4ⁿ − 1, or at least three, so
  N ≥ (2ⁿ − 1)³ ≥ 4ⁿ − 1 (n ≥ 2); both exceed N = h·2ⁿ − 1 when h < 2ⁿ.
  This is the step that needs 2ⁿ > h.

**Notes**

- The argument needs 2ⁿ > 33, so n ≥ 6. n = 2, 3 (N = 131, 263, prime) are
  printed by the half that needs no size condition; for n = 4 and 5
  (N = 527 = 17·31, 1055 = 5·211) the program was run and prints neither.
  At n = 1 (N = 65) no squaring runs and a is the positive number V₆₆(k,
  −1), so `a+2` is not 0 and 1 is not printed, as it should not be.
- Exact integer arithmetic throughout, so the program is right for every
  n. Each n costs one modular power and n − 1 squarings modulo an
  (n + 6)-bit number, and the `exec` string grows with n. The bar is 29
  terms (up to 1992) in 120 s, reached after about 45 s here; the next
  term, 2232, is much further out. The b-file's 56 terms reach 773030.
- The 29 required terms would fit in a table shorter than the program, so
  this record went through a review.
- H. Riesel, Lucasian criteria for the primality of N = h·2ⁿ − 1, Math.
  Comp. 23 (1969) 869–875; Ø. J. Rödseth, A note on primality tests for
  N = h·2ⁿ − 1, BIT 34 (1994) 451–454.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002240), CC BY-SA 4.0.
