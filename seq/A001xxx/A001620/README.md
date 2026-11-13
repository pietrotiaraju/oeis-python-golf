# A001620

> Decimal expansion of Euler's constant (or the Euler-Mascheroni constant), gamma.
> — [OEIS A001620](https://oeis.org/A001620)

Offset 0: 5, 7, 7, 2, 1, 5, 6, 6, 4, 9, 0, 1, 5, 3, 2, 8, 6, 0, 6, 0, 6, 5, 1, 2, 0, 9, …

### Python 3 — 172 bytes

```python
k=0;m=3
while m:=m+1:
 n=2**m;S=T=q=10**n;r=5**n;G=-r;c=k
 for j in range(1,4*n):T=T*-n//j;G-=(T+m*(S>>j))//j
 while G//(q:=q//10)==(G+2*r)//q:c-=1;k+=c<0!=print(G//q);G%=q
```

**How it works**

- Sweeney's method (Math. Comp. 17, 1963): for every x > 0,
  **γ = Ein(x) − ln x − E₁(x)**, where Ein(x) = Σ (−1)ʲ⁻¹xʲ/(j·j!) over
  j ≥ 1 and 0 < E₁(x) = ∫ₓ^∞ e⁻ᵗ/t dt < e⁻ˣ/x (Abramowitz–Stegun 5.1.11).
  The program takes x = n = 2ᵐ, so ln n = m·ln 2 with
  ln 2 = Σ 1/(j·2ʲ).
- Everything is in fixed point with S = 10ⁿ: `T` is
  ⌊S·(−n)ʲ/j!⌋ step by step, and each pass subtracts
  ⌊(T + m·⌊S/2ʲ⌋)/j⌋, so after j = 1, …, 4n − 1, G + 5ⁿ ≈ S·(Ein(n) −
  m·ln 2). (G starts at −r, r = 5ⁿ, which shifts the whole interval.)
- The error is below r = 5ⁿ = S/2ⁿ. Each floor costs less than 1, and the
  error in T grows by at most a factor n/j per step, so its total stays
  below K·eⁿ for K = 4n terms; the two tails are below S·(e/4)⁴ⁿ and
  m·S·2¹⁻⁴ⁿ (alternating, decreasing terms), and E₁ adds less than
  S·e⁻ⁿ/n. All together this is far below 5ⁿ already for n = 16, and the
  ratio only improves as n grows. So γ·10ⁿ lies strictly between G and
  G + 2r.
- A digit is certain when G and G + 2r agree in it: the loop compares
  ⌊G/q⌋ and ⌊(G + 2r)/q⌋ for q = 10ⁿ⁻¹, 10ⁿ⁻², …, prints the digit and
  keeps only the remainders, so each step is cheap. γ is irrational, so the
  interval never stays on a digit boundary, and n doubles at every stage.
  The counter `c` skips the digits already printed at earlier stages, and
  `k+=c<0!=print(…)` prints and counts each new one.

**Notes**

- The arithmetic is exact and the error bound proven, so every printed
  digit is right; stage m gives about 0.3·2ᵐ digits (4931 at m = 14, about
  9860 at m = 15).
- Digits are taken by division, not with `str`, so the 4300-digit
  int-to-str limit does not apply.
- Stage m costs 4·2ᵐ steps on 2ᵐ-digit numbers, so time grows about four
  times per stage.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001620), CC BY-SA 4.0.
