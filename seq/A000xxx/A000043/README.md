# A000043

> Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1 is
> called a Mersenne prime.
> — [OEIS A000043](https://oeis.org/A000043)

Offset 1: 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, …

### Python 3 — 65 bytes

```python
k=s=0
while[s or print(k+2)]:k+=1;s=4;exec('s=s*s%~-(4<<k)-2;'*k)
```

**How it works**

- The Lucas–Lehmer test: with s₀ = 4 and sᵢ₊₁ = sᵢ² − 2, the number
  M = 2ⁿ − 1 (n ≥ 3) is prime exactly when M divides sₙ₋₂.
- The program runs it for every n, prime or not, and k is n − 2. The string
  `'s=s*s%~-(4<<k)-2;'*k` is the step repeated n − 2 times, and `~-(4<<k)`
  is 2ᵏ⁺² − 1 = M (`~-x` is x − 1). Counting with n itself needs `(n-2)` and
  `~-2**n` and is 67 bytes; k pays for `k+2` in the print and saves 2.
- `s*s%M-2` reduces before it subtracts, so it needs no parentheses and s
  stays in −2 … M − 3 instead of 0 … M − 1. The only multiple of M in that
  range is 0, so `s or print(k+2)` prints n exactly when M divides sₙ₋₂.
- n = 2 is the one case the test misses: M = 3 and s₀ = 4. `k=s=0` makes the
  first loop condition see s = 0 and print 2 before any test runs.
- `while[…]:` is a non-empty list, so always true, and `s=4` resets the seed
  for each n.

**Why composite n is safe**

The theorem is usually stated for odd prime n, but only the direction
"M prime ⇒ M divides sₙ₋₂" needs that, and M prime already forces n prime.
The other direction holds for every n ≥ 3. Let ω = 2 + √3, so ω(2 − √3) = 1
and sᵢ = ω^(2ⁱ) + ω^(−2ⁱ). If M divides sₙ₋₂ and q is the smallest prime
factor of M, then ω^(2ⁿ⁻¹) ≡ −1 modulo q, so ω has order 2ⁿ among the units
of ℤ_q[√3], of which there are fewer than q². That gives q² > 2ⁿ > M, so M is
prime. A composite n therefore never passes.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each n costs
  n − 2 squarings modulo an n-bit number, and every n is tested, not only the
  primes: 1279 (15 terms) prints after about 8 s, 2203 after 35 s and 3217
  after 2 minutes. The bar is 15 terms in 60 s. The b-file's 51 terms reach
  82 589 933, which took the GIMPS project years.
- The string handed to `exec` is about 19·n bytes, so near the b-file's last
  terms it would need gigabytes of memory to compile.
- Testing sₙ₋₁ ≡ −2 instead (`*~-n` steps, `s+2or print(n)`, starting from
  `n=2;s=-2`) is also 67 bytes with n.
- Two more steps, sₙ ≡ 2, also accept n = 2: `n=s=1` /
  `while[s-2or print(n)]:n+=1;s=4;exec('s=(s*s-2)%~-2**n;'*n)` is 64 bytes and
  agrees with this sequence for every n ≤ 1300. It is not a proof, though:
  sₙ − 2 = 12(s₀s₁⋯sₙ₋₂)², so it would accept a composite M whose prime factors
  all divide some sᵢ, and nothing known rules that out.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000043), CC BY-SA 4.0.
