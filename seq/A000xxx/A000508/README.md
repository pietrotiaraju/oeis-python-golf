# A000508

> Generalized class numbers c_(n,3).
> — [OEIS A000508](https://oeis.org/A000508)

Offset 1: 61, 2763, 38528, 249856, 1066590, 3487246, 9493504, 22634496, 48649086, 96448478, …

Shanks's c_(n,3) measures the L-value L(7) = Σ_{k odd} (−n|k)/k⁷ of the
Jacobi symbol (−n|k): L(7) = (π/2n)⁷·√n·c/6!. For n = 1 the data carry an
extra factor 2, so a(1) = 61 is the Euler number |E₆|.

### Python 3 — 135 bytes

```python
D=[b:=0]
while 1:b+=2;D+=0,sum((-1)**(y*y//b)*((b*b+y*y%b*(-y*y%b))**3-b**6)-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(D[b]>>(b>2))
```

**How it works**

- This is the template of [A000233](../A000233/) (c_(n,1)) at s = 7. For odd
  k prime to n the Gauss sum gives Σ_{y mod 2n} sin(πky²/2n) = √n·(−n|k)
  (proof on that page), so √n·L(7) is a double sum of sin(πky²/2n)/k⁷ over
  y and odd k, once the k sharing a factor with n are taken out.
- The k-sum has a closed form. The Fourier series of the Euler polynomial
  E₆(t) = t⁶ − 3t⁵ + 5t³ − 3t (DLMF §24.8) is
  Σ_{k odd} sin(πkt)/k⁷ = −π⁷·E₆(t)/2880 for 0 ≤ t ≤ 1, and with
  w = t(1 − t) one has 3w + 3w² + w³ = 3t − 5t³ + 3t⁵ − t⁶, so

  Σ_{k odd} sin(πkt)/k⁷ = π⁷·((1 + t(1 − t))³ − 1)/2880   (0 ≤ t ≤ 1).

  Moving t by 1 flips the sign of every odd-k term.
- With b = 2n write y² = q·b + x with 0 ≤ x < b. Then t = y²/b, and the
  k-sum is π⁷·F/(2880·b⁶) with the integer

  F = (−1)^q·((b² + x(b − x))³ − b⁶).

  Summing over y and putting in the normalisation, π and √n cancel:
  c_(n,3) = 6!·(2n/π)⁷·L(7)/√n = ½·ΣF, up to the k that share a factor
  with n.
- Those k are peeled off as on the A000233 page: if e = gcd(k, n), the sine
  sum for (k, n) is e times the one for (k/e, n/e), and the n⁶ in the
  scaling absorbs the 1/e⁷·e, so d(n) = 2·c_(n,3) satisfies
  d(n) = ΣF − Σ_{odd e | n, e > 1} d(n/e) with no weights.
- `(-1)**(y*y//b)` is (−1)^q. `y*y%b*(-y*y%b)` is x(b − x): for x > 0,
  −y² mod b is b − x, and for x = 0 both are 0. This is 2 bytes under
  `(x:=y*y%b)*(b-x)`.
- `D` holds d(n) at index 2n with a 0 between entries, so d(n/e) is
  `D[b//y]`; `y%2>b%y` means "y odd and y | b", and a failed test reads
  D[0] = 0. y runs over 2 … b+1, a full residue system mod 2n without
  y = 0 (division by zero) and y = 1 (d(n) itself is not there yet).
- d(1) = 61 = a(1) (Shanks's doubled n = 1 value) and d(n) = 2·a(n) for
  n > 1, so the program prints `D[b]>>(b>2)`.

**Notes**

- The same sum written in v = y² mod 2b − b, F = v⁵(|v| − 3b) + 5b³v³ − 3b⁵v,
  was 143 bytes. The cube form comes from the symmetry of E₆ about t = ½;
  the sign (−1)^q replaces the `abs`.
- Exact integer arithmetic, correct for every n by the identities above. The
  first 150 terms also agree with a 50-digit evaluation of the defining
  series with 4000 terms of Jacobi symbols.
- Each term takes O(n) steps: about 5200 terms in 60 s here.
- The b-file has 21 terms (up to a(21)), the data section of the entry; the
  bar is the whole b-file in 60 s.
- a(n) grows like n^6.5, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 143 | first entry |
| 2026-11-07 | Python 3 | 135 | E₆ as a cube with a sign: (−1)^q·((b²+x(b−x))³−b⁶) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000508), CC BY-SA 4.0.
