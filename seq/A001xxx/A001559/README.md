# A001559

> a(0) = 1, a(1) = 4; thereafter a(n)*(2n + 10) - a(n-1)*(11n + 35) + a(n-2)*(8n + 2) + a(n-3)*(15n + 7) + a(n-4)*(4n - 2) = 0.
> — [OEIS A001559](https://oeis.org/A001559)

Offset 0: 1, 4, 15, 54, 193, 690, 2476, 8928, 32358, 117866, 431381, 1585842, …

### Python 3 — 66 bytes

```python
k=5
while[print(((B:=8**k)-1)*(B+1)**(2*k-5)//(B+2)//B**k%B)]:k+=1
```

**How it works**

- **A closed form.** With C(x) the Catalan generating function and
  v = xC² = C − 1 (so v = x(1 + v)²), Michael Somos's g.f. in the entry,
  2/(1 − 4x + x² + 2x³ + (1 − 2x − x²)√(1 − 4x)), equals
  (1 + v)⁶/(1 + 2v) = C⁴·F, where F = C/(1 + xC) = 1/(1 − x(C − 1)) is
  Fine's g.f. (hill-free Dyck paths). Lagrange inversion for
  v = x·(1 + v)², [xⁿ] H(v) = [tⁿ] H(t)·(1 + t)^(2n)·(1 − 2t/(1 + t)),
  with H = (1 + t)⁶/(1 + 2t) gives
  a(n) = [tⁿ] f(t), f(t) = (1 − t)(1 + t)^(2n+5)/(1 + 2t).
- **Reading the coefficient off a number.** Put t = 1/B, B = 8ᵏ with
  k = n + 5. Then Bⁿ·f(1/B) = (B − 1)(B + 1)^(2n+5)/((B + 2)·B^(n+5)) =
  Σ_j r_j·B^(n−j), with r_j = [tʲ] f. The terms j ≤ n add up to an integer
  ≡ r_n = a(n) (mod B); the terms j > n add E = Σ_{i≥1} r_{n+i}·B^(−i).
  When 0 ≤ E < 1 and 0 ≤ a(n) < B, the floor taken mod B is a(n): that is
  `((B:=8**k)-1)*(B+1)**(2*k-5)//(B+2)//B**k%B` (two floor divisions in a
  row are one by the product).
- **Why B = 8ᵏ = 2^(3n+15) is enough.** The coefficients of
  (1 − t)(1 + t)^(2n+5) have absolute sum at most 2^(2n+6), so
  |r_j| ≤ 2^(j+2n+6) and 0 ≤ a(n) ≤ 2^(3n+6) < B. The same Lagrange step
  with H = (1 + t)⁴/(1 + 2t) shows r_{n+1} = [x^(n+1)] C²·F ≥ C_{n+2} ≥ 1
  (C and F have nonnegative coefficients). Hence
  E ≥ 1/B − Σ_{i≥2} 2^(3n+6+i)·B^(−i) ≥ (1 − 2^(3n+9)/B)/B > 0 and
  E ≤ (2^(3n+7) + 1)/B < 1.
- **It is the title's sequence.** The g.f. satisfies
  2xA′ + 10A − x(11xA′ + 46A) + x²(8xA′ + 18A) + x³(15xA′ + 52A) +
  x⁴(4xA′ + 14A) = 10 + 2x, an identity in ℚ(x, √(1 − 4x)) checked by exact
  computer algebra. Comparing coefficients, that says a(0) = 1, a(1) = 4
  and the title's recurrence for every n ≥ 2 (with a(m) = 0 for m < 0).
  As 2n + 10 ≠ 0, those values and the recurrence fix the sequence, so the
  program prints it for every n.

**Notes**

- The recurrence itself, started at n = 1 with a virtual a(−3) = −1
  (`a=1;b=c=0;d=-1;n=1` /
  `while[print(a)]:a,b,c,d=(n*(11*a-8*b-15*c-4*d)+35*a-2*b-7*c+2*d)//(2*n+10),a,b,c;n+=1`),
  is 105 bytes.
- Exact integer arithmetic. The power (B + 1)^(2n+5) has about 6n² bits,
  so the terms slow down gradually: the 201 terms of the b-file take about
  half a second here. a(n) grows like 4ⁿ, so Python's 4300-digit int-to-str
  limit would stop the program at about n = 7100, far beyond 60 s.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001559), CC BY-SA 4.0.
