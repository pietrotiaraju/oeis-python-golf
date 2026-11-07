# A000488

> Generalized tangent numbers d_(n,3).
> — [OEIS A000488](https://oeis.org/A000488)

Offset 1: 16, 361, 3362, 16384, 55744, 152166, 355688, 739328, 1415232, 2529614, …

Shanks's d-numbers: for n ≥ 2, a(n) = 5!·(2n/π)⁶·L/√n with
L = Σ_{k odd} (n|k)/k⁶ and (n|k) the Jacobi symbol (the formula in the
entry's Mathematica program); a(1) = 16 is the tangent number
T₅ = 2·5!·(2/π)⁶·Σ_{k odd} 1/k⁶, twice the general formula at n = 1.

### Python 3 — 129 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(5*a*a-u*u)**2-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

- This is the [A000176](../A000176/) program (d_(n,2), fourth powers) with
  sixth powers. Write δ(n) = 5!·(2n/π)⁶·L/√n for every n ≥ 1, so
  δ(n) = a(n) for n ≥ 2 and δ(1) = 8.
- Gauss sums turn the character into cosines: for odd k prime to n,
  Σ_{y mod 2n} cos(πky²/2n) = √n·(n|k). The odd-k Fourier series
  Σ_{k odd} cos(πkx)/k⁶ = −π⁶E₅(x)/480 on [0, 1] (DLMF 24.8.5) then sums
  over k in closed form. Folding x = y²/2n mod 2 into [0, 1] gives
  x = (n − u)/2n with u = |y² mod 4n − 2n| − n, and
  −32n⁵·E₅((n − u)/2n) = u(5n² − u²)² =: g(u), an integer: π and √n cancel.
- The odd k with gcd(k, n) = e > 1 add the values for n/e, so
  ½·Σ_y g(u) = Σ_{odd e | n} δ(n/e). The program peels them off:
  `D` holds 2δ(n), and each pass appends Σ_y g(u) − Σ_{odd e | n, e > 1} D[n/e].
- `range(2,2*a+2)` is a full set of 2n residues (g depends only on y² mod 4n,
  and (y + 2n)² ≡ y² mod 4n); starting at 2 avoids y = 0 (division by zero)
  and y = 1 (D[n] is not there yet). `y%2>a%y` is "y odd and y | n", and for
  y > n the index `a//y` is 0, where D[0] = 0.
- `D[a]>>1%a` halves 2δ(n) for n ≥ 2 and leaves D[1] = 2δ(1) = 16 = a(1)
  alone, since 1%1 = 0 (`%` binds tighter than `>>`).

**Notes**

- At n = 1 the two residues give g = 16 and 0, so D[1] = 16; at n = 2 they
  give −512, 361, 512, 361, so a(2) = 722/2 = 361.
- Exact integer arithmetic, so the program is right for every n by the
  Gauss-sum and Fourier identities above. Moving the divisor test into the
  index, `D[a//y*(y%2>a%y)]`, is the same length.
- Each term takes 2n steps: about 5060 terms in 60 s here. The b-file has
  1000 terms (up to a(1000)); the bar is the whole b-file in 60 s.
- a(n) grows like n^5.5, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000488), CC BY-SA 4.0.
