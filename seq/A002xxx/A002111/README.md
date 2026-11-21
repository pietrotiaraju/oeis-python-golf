# A002111

> Glaisher's G numbers.
> — [OEIS A002111](https://oeis.org/A002111)

Offset 1: 1, 5, 49, 809, 20317, 722813, 34607305, 2145998417, 167317266613, …

### Python 3 — 103 bytes

```python
r=[s:=1]
while 1:
 for s in 0,-r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
 k=len(r);print(3*k*s//(4**k+2**k))
```

**How it works**

- **Triangle.** The loop is the program of [A000436](../A000436/), a
  weighted boustrophedon triangle T(m, 0) = u_m,
  T(m, k) = T(m, k−1) + 3·T(m−1, m−k), whose diagonal has e.g.f.
  (sec 3x + tan 3x)·U(x) (weight c scales row m by c^m). With
  U = cos x (u_(2j) = (−1)^j, u_odd = 0; `-r[0]` flips the sign of the
  last even row's start) the even diagonal is
  s_n = (2n)!·[x^(2n)] sec 3x·cos x = A000436(n), which ends each pass,
  and `r` is then row 2n, of length 2n + 1.
- **Glaisher's G.** a(n) = (2n+1)!·[x^(2n)] F, F = (3/2)/(1 + 2 cos x)
  (Conn's and Somos's formulas in the entry), so with
  f_n = (2n)!·[x^(2n)] 1/(1 + 2 cos x), a(n) = (3/2)(2n+1)·f_n.
- **Reduction to H′.** Put H = 1/(2 cos x − 1). Then
  H − 1/(1 + 2 cos x) = 2/(4cos²x − 1) = 2/(1 + 2 cos 2x), that is
  F₁(x) = H(x) − 2F₁(2x) for F₁ = 1/(1 + 2 cos x). On the x^(2n)
  coefficients, f_n = h_n − 2·4ⁿ·f_n, so f_n = h_n/(2^(2n+1) + 1), where
  h_n = 2·[A002114](../A002114/)(n) = A000436(n)/4ⁿ (cos 3y identity, as
  on that page).
- **Formula.** With k = 2n + 1 = `len(r)` and s = A000436(n):
  a(n) = 3k·s/(2^k·(2^k + 1)) = `3*k*s//(4**k+2**k)`, exact because a(n) is
  an integer (check: n = 1, k = 3, s = 8: 72/72 = 1).

**Notes**

- Equivalently a(n) = (2n+1)·H(n)/(2^(2n+1) + 1) with H =
  [A002112](../A002112/). The usual formulas go through Bernoulli numbers
  (a(n) = (−1)^(n+1)·3^(2n+1)·B_(2n+1)(1/3)); the identity above keeps it
  in integers.
- The b-file has 254 terms (n = 1 to 254), and the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002111), CC BY-SA 4.0.
