# A002234

> Numbers k such that the Woodall number k*2^k - 1 is prime.
> — [OEIS A002234](https://oeis.org/A002234)

Offset 1: 2, 3, 6, 30, 75, 81, 115, 123, 249, 362, 384, 462, 512, 751, 822, …

### Python 3 — 132 bytes

```python
n=k=1
while 1:
 n+=1;N=(n<<n)-1
 while pow(k*k+4,N//2,N)<2:k+=1
 a,s=2,k;exec('a,s=s,k*s+a;'*2*n+'a=a*a%N-2;'*(n-2));a%N or print(n)
```

**How it works**

- **Choosing P (Rödseth).** The Lucas–Lehmer–Riesel test: for N = h·2ⁿ − 1
  with h odd and h < 2ⁿ, and P with Jacobi symbols (P − 2 | N) = 1 and
  (P + 2 | N) = −1, N is prime exactly when N divides V_{h·2ⁿ⁻²}(P), where
  V₀ = 2, V₁ = P, Vⱼ₊₁ = P·Vⱼ − Vⱼ₋₁ (Riesel 1969 with P = 4 when 3 ∤ h;
  Rödseth 1994 for any such P). Here N = n·2ⁿ − 1 = h·2ᵉ − 1 with h the
  odd part of n and e ≥ n, so h ≤ n < 2ᵉ and the theorem applies for every
  n ≥ 2; but h changes with n (3 | h when 3 | n), so P is searched for
  every n. The program takes P = k² + 2, so that P − 2 = k² is a square,
  and `while pow(k*k+4,N//2,N)<2:k+=1` moves k on until (k² + 4)^((N−1)/2)
  mod N is neither 0 nor 1: for a prime N, Euler's criterion makes that
  exactly (k² + 4 | N) = −1. k is never reset, so each n starts where the
  last search stopped (any k with the right symbol will do).
- **The test, run on V(k, −1).** With P = k² + 2, Vⱼ(P) = V₂ⱼ(k, −1),
  where V(k, −1) is xⱼ₊₁ = k·xⱼ + xⱼ₋₁ from x₀ = 2, x₁ = k. `a,s=2,k` and
  2n steps `a,s=s,k*s+a;` give a = V₂ₙ(k, −1) = Vₙ(P); then n − 2 steps
  `a=a*a%N-2;` (V₂ⱼ = Vⱼ² − 2) give V_{n·2ⁿ⁻²}(P) = V_((N+1)/4)(P) mod N,
  the theorem's value, and the program prints n when it is 0 mod N (`a%N`
  because at n = 2 no squaring runs).
- **Bookkeeping.** n = 1 gives N = 1, not a prime, so the loop starts at
  n = 2 (`n=k=1`, then `n+=1`). When n ≡ 4 or 5 mod 6, 3 divides N and the
  test fails, as it must.

**Why it prints exactly the n with N prime**

Write α = (k + √(k² + 4))/2, a root of x² − kx − 1 (the other root is
−1/α), and E = (N + 1)/2 = n·2ⁿ⁻¹, even for n ≥ 2. Then
Vⱼ(k² + 2) = α²ʲ + α⁻²ʲ, and the value the program tests against 0 is
VAL = α^E + α^−E. Write N + 1 = h·2ᵉ with h odd (e ≥ n, h ≤ n < 2ᵉ).

- *The search ends.* Let p be a prime factor of N. Of the k mod p, the
  conic y² − k² = 4 leaves (p + 1 − z)/2 ≥ 1 with k² + 4 a non-residue
  (z ≤ 2 counts the roots of k² + 4), and for such k the power
  (k² + 4)^((N−1)/2) is a non-residue mod p, since (N − 1)/2 is odd (N ≡ 3
  mod 4): it is neither 0 nor 1. So the search stops within p steps. For a
  prime N it stops exactly at a k with (k² + 4 | N) = −1; such k exist and
  also make k² a non-zero square.
- *N prime ⇒ printed.* √(k² + 4) is not in GF(N), so the Frobenius map
  swaps the two roots: α^N = −1/α and α^(N+1) = −1. Then
  VAL² = α^(N+1) + 2 + α^−(N+1) = 0, so N divides VAL.
- *Printed ⇒ N prime.* Let q be a prime factor of N; VAL ≡ 0 (mod q) gives
  α^(N+1) = −1 in GF(q²). If q divided k² + 4, α would be k/2 with α² = −1
  and α^(N+1) = (−1)^E = 1; so it does not, and the order of α is a
  multiple of 2ᵉ⁺¹. It divides q − 1 if α ∈ GF(q), and 2(q + 1) otherwise
  (α^q = −1/α), so q ≡ ±1 mod 2ᵉ and q ≥ 2ᵉ − 1. A composite N has either
  two prime factors, one ≡ 1 and one ≡ −1 mod 2ᵉ (their product is
  N ≡ −1), so N ≥ 4ᵉ − 1, or at least three, so N ≥ (2ᵉ − 1)³ ≥ 4ᵉ − 1;
  both exceed N = h·2ᵉ − 1 since h < 2ᵉ.

**Notes**

- Exact integer arithmetic throughout, so the program is right for every
  n. Each n costs one modular power, 2n small steps and n − 2 squarings
  modulo an (n + log₂ n)-bit number; compiling the `exec` string, which
  grows with n, is a good part of the time. The bar is 15 terms (up to
  822) in 60 s, reached after about 20 s here; the next term, 5312, would
  take hours. The b-file's 34 terms reach 17016602.
- The 15 required terms would fit in a table shorter than the program, so
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
Sequences](https://oeis.org/A002234), CC BY-SA 4.0.
