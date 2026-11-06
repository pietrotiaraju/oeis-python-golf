# A000362

> Generalized class numbers c_(n,2).
> — [OEIS A000362](https://oeis.org/A000362)

Offset 1: 5, 57, 352, 1280, 3522, 7970, 15872, 29184, 49410, 79042, …

### Python 3 — 129 bytes

```python
D=[b:=0]
while 1:b+=2;D+=0,sum((v:=y*y%(2*b)-b)**3*(2*b-abs(v))-b**3*v-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(D[b]>>(b>2))
```

**How it works**

- This is the template of [A000233](../A000233/) (Shanks's c_(n,1)) one
  step up, at s = 5 instead of s = 3. The OEIS comment defines c by
  L(5) = (π/2n)⁵·√n·c/4!, with L(5) = Σ_{k odd} (−n|k)/k⁵ and (−n|k) the
  Jacobi symbol, so c = 24·(2n)⁵·L(5)/(π⁵√n). For n = 1 this gives 5/2,
  while a(1) = 5 is the Euler number E₄: as for A000233, Shanks's c_(1,m)
  carry an extra factor 2.
- The Gauss-sum identity of the A000233 page,
  Σ_{y mod 2n} sin(πky²/2n) = √n·(−n|k) for odd k prime to n, turns L(5)
  into a finite sum of the odd-k sine series
  f(t) = Σ_{k odd} sin(πkt)/k⁵. Integrating Σ_{k odd} sin(πkt)/k = π/4
  four times gives f(t) = (π⁵/96)(t − 2t³ + t⁴) on [0, 1] (at t = ½ this is
  β(5) = 5π⁵/1536); f is odd and changes sign under t → t + 1.
- With b = 2n, x = y² mod 2b, t = x/b and v = x − b ∈ [−b, b), those
  symmetries give b⁴·(96/π⁵)·f(t) = 2b·v³ − |v|·v³ − b³·v, which is the
  term `v**3*(2*b-abs(v))-b**3*v` (written to reuse the walrus). The
  constants cancel as in A000233: ΣF over y is 2c, plus the contribution
  of the odd k that share a factor with n.
- Those k are removed by the same recursion: if e = gcd(k, n), the sine sum
  for (k, n) is e times the one for (k/e, n/e), and with the n⁴ scaling the
  1/e⁴ weights cancel, so d(n) = ΣF − Σ_{odd e | n, e > 1} d(n/e) with
  d = 2c. `D` holds d(n) at index 2n with a 0 between entries, and
  `D[b//y*(y%2>b%y)]` reads d(n/y) exactly when y is an odd divisor of n
  (and the 0 in D[0] otherwise), with y running over 2 … b+1, a full
  residue system mod 2n (the A000233 page has the details).
- d(1) = 5 = a(1) and d(n) = 2·a(n) for n > 1, so `D[b]>>(b>2)` prints
  every term. (A000233's `-~D[b]>>1` works there only because d(1) = 1.)

**Notes**

- Exact integer arithmetic, correct for every n by the identities above;
  the program also reproduces the b-file terms it reaches.
- `(v:=…)*(v*v*(2*b-abs(v))-b**3)` is 1 byte longer, and the factored
  forms v·u·(b² − u(u + b)) with u = |v| − b, or F3·(b² + |F3|) with
  F3 = v(|v| − b), the A000233 term, are 5 and 6 bytes longer. Looping
  over 4n (the A000233 variant) saves 2 bytes in the term but costs more in
  the padding and the final shift.
- Each term takes O(n) steps. Here it printed 6173 terms in 60 s (term
  5000 at about 38 s) of the 10000 in the b-file; the bar is 4700 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000362), CC BY-SA 4.0.
