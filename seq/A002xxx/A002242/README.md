# A002242

> Numbers k such that 45*2^k - 1 is prime.
> — [OEIS A002242](https://oeis.org/A002242)

Offset 1: 1, 2, 3, 4, 5, 6, 8, 9, 14, 15, 16, 22, 28, 29, 36, 37, 54, 59, 85, …

### Python 3 — 132 bytes

```python
m=k=0;N=89
while 1:
 while pow(k*k+4,N//2,N)<2:k+=1
 a,s=2,k;exec('a,s=s,k*s+a;'*90+'a=a*a%N-2;'*m);(a+2)%N or print(m+1);m+=1;N-=~N
```

**How it works**

- **Choosing P (Rödseth).** The Lucas–Lehmer–Riesel test: for N = h·2ⁿ − 1
  with h odd and h < 2ⁿ, and P with Jacobi symbols (P − 2 | N) = 1 and
  (P + 2 | N) = −1, N is prime exactly when N divides V_{h·2ⁿ⁻²}(P), where
  V₀ = 2, V₁ = P, Vⱼ₊₁ = P·Vⱼ − Vⱼ₋₁ (Riesel 1969 with P = 4 when 3 ∤ h;
  Rödseth 1994 for any such P). Here h = 45 is a multiple of 3, so N ≡ 2
  mod 3, (6 | N) = 1 and P = 4 fails: P must be found for each n. The
  program takes P = k² + 2, so that P − 2 = k² is a square, and
  `while pow(k*k+4,N//2,N)<2:k+=1` moves k on until (k² + 4)^((N−1)/2) mod
  N is neither 0 nor 1: for a prime N, Euler's criterion makes that
  exactly (k² + 4 | N) = −1. k is never reset, so each n starts where the
  last search stopped (any k with the right symbol will do).
- **The test, run on V(k, −1).** With P = k² + 2, V_j(P) = V₂ⱼ(k, −1),
  where V(k, −1) is xⱼ₊₁ = k·xⱼ + xⱼ₋₁ from x₀ = 2, x₁ = k. `a,s=2,k` and
  90 steps `a,s=s,k*s+a;` give a = V_90(k, −1) = V_45(P) (small numbers,
  no reduction needed); then m = n − 1 steps `a=a*a%N-2;` (V₂ⱼ = Vⱼ² − 2)
  give V_{45·2ⁿ⁻¹}(P) = V_((N+1)/2)(P) mod N. The program prints n when
  this is ≡ −2 mod N, which is the theorem's test one squaring later:
  V_((N+1)/2) = (V_((N+1)/4))² − 2.
- **Bookkeeping.** m = n − 1 counts the squarings and `print(m+1)` prints
  n; `N-=~N` turns N = 45·2ⁿ − 1 into 2N + 1 = 45·2ⁿ⁺¹ − 1, starting from
  N = 89 at n = 1. `a*a%N-2` reduces before subtracting, so after a
  squaring a lies in −2 … N − 3 and a ≡ −2 means a = −2; `(a+2)%N` also
  covers n = 1, where no squaring runs.

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

- The argument needs 2ⁿ > 45, so n ≥ 6. For n = 1 … 5, N = 89, 179, 359,
  719, 1439 are all prime and are printed by the half that needs no size
  condition.
- Exact integer arithmetic throughout, so the program is right for every
  n. Each n costs one modular power and n − 1 squarings modulo an
  (n + 6)-bit number, and the `exec` string grows with n. The bar is 40
  terms (up to 1724) in 120 s, reached after about 46 s here; the next
  term, 2063, is much further out. The b-file's 70 terms reach 818648.
- The 40 required terms would fit in a table shorter than the program, so
  this record went through a review.
- H. Riesel, Lucasian criteria for the primality of N = h·2ⁿ − 1, Math.
  Comp. 23 (1969) 869–875; Ø. J. Rödseth, A note on primality tests for
  N = h·2ⁿ − 1, BIT 34 (1994) 451–454.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 132 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002242), CC BY-SA 4.0.
