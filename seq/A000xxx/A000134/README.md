# A000134

> Positive zeros of Bessel function of order 0 rounded to nearest integer.
> — [OEIS A000134](https://oeis.org/A000134)

Offset 1: 2, 6, 9, 12, 15, 18, 21, 24, 27, 31, 34, 37, 40, 43, 46, 49, 53, …

The zeros of J₀ are 2.405, 5.520, 8.654, 11.79, …, about π apart.

### Python 3 — 92 bytes

```python
p=k=1
while u:=p:
 k+=2;j=b=0
 while b*b<u*u:b=b*j*j+u;j+=4;u*=-k*k
 if b<0:print(k//2);p=-p
```

**How it works**

- **Rounding as a sign change.** The zero that rounds to m lies between
  m − ½ and m + ½. So the program walks over the half-integers x = k/2
  (k = 3, 5, 7, …) and prints k//2 = m when J₀ has a different sign at
  m + ½ than at m − ½. `p` is the sign at the previous half-integer; it
  starts at +1 because J₀ > 0 on [0, 2.4].
- **The series.** J₀(x) = Σ tᵢ with tᵢ = (−y)ⁱ/(i!)² and
  y = x²/4 = k²/16. Write Dᵢ = 16ⁱ(i!)² = (4·1)²(4·2)²⋯(4i)². Then
  `b` = p·Dᵢ·(t₀ + ⋯ + tᵢ) and `u` = p·(−k²)ⁱ⁺¹ = p·Dᵢ·(−k²)·tᵢ, all
  integers. One pass does `b=b*j*j+u` with j = 4i (multiply the old sum
  by (4i)² and add the new term), then `j+=4` and `u*=-k*k`. At j = 0
  the old `b` is multiplied by 0, so the reset `b=0` is only there to
  enter the loop.
- **When to stop.** The loop stops at the first i with
  |Sᵢ| ≥ k²·|tᵢ|, where Sᵢ = t₀ + ⋯ + tᵢ; in integers that is
  `b*b>=u*u`. The sign of J₀(x) is then the sign of Sᵢ, which is the sign
  of p·`b`:
  - |tᵢ₊₁|/|tᵢ| = y/(i+1)², so the terms grow while i² < y and then
    shrink for good. While they are still growing,
    |Sᵢ| ≤ (i+1)·|tᵢ|, and i + 1 ≤ k/4 + 1 < k². So the loop cannot
    stop before the peak.
  - After the peak the rest of the series, tᵢ₊₁ + tᵢ₊₂ + ⋯, alternates
    with shrinking terms, so its size is below |tᵢ₊₁| < |tᵢ| ≤ |Sᵢ|/k².
    Adding it cannot change the sign of Sᵢ.
- `b<0` therefore means that J₀(k/2) has the sign opposite to `p`: a zero
  was passed, so the program prints k//2 and flips `p`.

**Notes**

- Exact integer arithmetic, correct for every n. Three facts make it so:
  - The loop ends: Sᵢ → J₀(k/2) and tᵢ → 0, and J₀(k/2) ≠ 0, because
    J₀(α) is transcendental for every nonzero algebraic α (Siegel, 1929).
    For the same reason no zero is exactly a half-integer, so the rounding
    never ties.
  - Each window (m − ½, m + ½) holds at most one zero. With
    w(x) = √x·J₀(x), w'' + (1 + 1/(4x²))·w = 0, and Sturm comparison with
    w'' + (1 + 1/23)·w = 0 for x ≥ 2.4 puts consecutive zeros at least
    π/√(1 + 1/23) > 3 apart. So a sign change between m − ½ and m + ½
    means exactly one zero there.
  - The first zero, 2.405, is above 3/2, so starting with the sign at ½
    misses nothing.
- Every half-integer costs about 0.69k passes (686 at k = 1001) on
  integers of tens of thousands of bits: the exact series has huge
  cancellation, with terms of size about eˣ for a sum of size at most
  about 1/√x. The program prints
  200 terms in about 19 s and 277 in a minute. The bar is 200 terms in
  60 s; the b-file has 1000.
- Other versions that print the same terms:
  - stopping with the usual alternating-series test, "partial sums
    Sᵢ₋₁ and Sᵢ have the same sign", needs a separate guard that the terms
    have started to shrink (`while j<k or b*b<b*u:` with `j` running
    over 4i): 100 bytes. Asking for |Sᵢ| ≥ k²·|tᵢ| does both jobs in one
    test.
  - stepping through every k/2, integers included, and printing k//2
    also works (the window (m − ½, m) or (m, m + ½) of the zero rounds
    to m either way), but is the same length and twice as slow.
  - `fractions.Fraction` instead of scaled integers: the import alone
    costs 24 bytes.
- `while u:=p:` resets `u` in the loop condition, 1 byte under
  `while 1:` plus `;u=p`: p is ±1, so the condition is always true.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 93 | first entry |
| 2026-11-05 | Python 3 | 92 | `u=p` moved into the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000134), CC BY-SA 4.0.
