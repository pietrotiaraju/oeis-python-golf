# A000233

> Generalized class numbers c_(n,1).
> — [OEIS A000233](https://oeis.org/A000233)

Offset 1: 1, 3, 8, 16, 30, 46, 64, 96, 126, 158, …

### Python 3 — 115 bytes

```python
D=[b:=0]
while 1:b+=2;D+=0,sum((v:=y*y%(2*b)-b)*(abs(v)-b)-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(-~D[b]>>1)
```

**How it works**

- The OEIS comment defines c by L(3) = (π/2n)³·√n·c/2!, with
  L(3) = Σ_{k odd} (−n|k)/k³ and (−n|k) the Jacobi symbol (0 when k shares a
  factor with n). That gives c = 16n²·T/π³ with T = √n·L(3). For n = 1 it
  gives ½, while a(1) = 1 is the Euler number E₂: Shanks's c_(1,m) carry an
  extra factor 2 (the Mathematica program in the entry has it too).
- Gauss sums turn the character into sines. For odd k prime to n,
  Σ_{y mod 4n} e^{2πiky²/4n} = (1 + i^k)·2√n·(n|k), and the imaginary part
  of 1 + i^k is (−1|k), so Σ_{y mod 2n} sin(πky²/2n) = √n·(−n|k) (y and
  y + 2n give the same y² mod 4n, so half the sum is enough).
- The odd-k sine series Σ_{k odd} sin(πkt)/k³ = π³t(1 − t)/8 on [0, 1],
  odd and of period 2, sums over k in closed form. With b = 2n,
  x = y² mod 2b and v = x − b, it is (π³/8b²)·v(|v| − b), so π and √n cancel
  and each y leaves the integer F = v(|v| − b). Summing over y gives
  ½·ΣF = 16n²·S/π³, where S also counts the odd k that share a factor with n.
- Those k are peeled off by recursion. If e = gcd(k, n), the sine sum for
  (k, n) is e times the one for (k/e, n/e), so S(n) = Σ_{odd e | n} T(n/e)/e²,
  and in the scaled form d(n) = 2·16n²·T/π³ this reads
  d(n) = ΣF − Σ_{odd e | n, e > 1} d(n/e). No weights survive: the 1/e² is
  exactly what the n² scaling absorbs.
- `D` holds d(n) at index 2n, with a 0 between consecutive entries
  (`D+=0,…`), so the index of d(n/e) is just b//e. The y-loop runs over
  2 … b+1, a full residue system mod 2n; its odd members > 1 that divide n
  are exactly the e above, and `y%2>b%y` means "y odd and y | b". When the
  test fails the index is 0 and D[0] = 0, so the correction vanishes.
  Starting at 2 keeps out y = 0 (division by zero) and y = 1 (d(n) itself is
  not there yet); y = b stands in for residue 0, and y = b+1 for residue 1.
- d(n) = 2·a(n) for n > 1 and d(1) = 1, so `-~D[b]>>1` = ⌊(d + 1)/2⌋ gives
  every term, a(1) = 1 included.

**Notes**

- Exact integer arithmetic, correct for every n by the identities above;
  the program also reproduces all 10000 terms of the b-file. Each term takes
  O(n) steps: about 8900 terms in 60 s here, the whole b-file in about 85 s.
  The bar is 6500 terms in 60 s.
- The same template as [A000176](../A000176/) (Shanks's d_(n,2), an even
  character at s = 4), but at s = 3 the series is a quadratic instead of a
  cubic, so no folding with `abs` around the Euler polynomial is needed.
- Looping over 4n instead (`(v:=y*y%c*2-c)*(abs(v)-c)`, two residue systems
  mod 2n, d scaled by 8) saves 2 bytes in the term but costs them back in
  the padding or the index. Printing at the top of the loop
  (`while[print(…)]:`) needs a(1) set up by hand and comes out longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 115 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000233), CC BY-SA 4.0.
