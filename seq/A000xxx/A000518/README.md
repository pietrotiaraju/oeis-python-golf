# A000518

> Generalized tangent numbers d_(n,4).
> — [OEIS A000518](https://oeis.org/A000518)

Offset 1: 272, 24611, 515086, 4456448, 23750912, 93241002, 296327464, 806453248, 1951153920, 4300685074, …

For n ≥ 2, a(n) = 7!·(2n/π)⁸·L/√n with L = Σ_{k odd} (n|k)/k⁸, the
eighth-power analogue of the Dirichlet series behind
[A000176](../A000176/) (fourth powers) and [A000488](../A000488/) (sixth
powers); a(1) = 272 is the tangent number T₈ (Shanks 1967).

### Python 3 — 151 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*((7*a*a-u*u)**3+28*a**4*(3*a*a-u*u))-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

- The method is the one on the [A000176](../A000176/) page, with the
  Fourier series one degree higher. Quadratic Gauss sums turn the Jacobi
  symbol into Σ_{y mod 2n} cos(πky²/2n) = √n·(n|k) for odd k prime to n,
  and the odd-k series Σ_{k odd} cos(πkx)/k⁸ = π⁸E₇(x)/(4·7!) on [0, 1]
  (DLMF 24.8.5) sums over k in closed form. π and √n cancel, and every
  residue y leaves an integer polynomial in u = |y² mod 4n − 2n| − n,
  which is the Fourier argument folded into [0, 1] as x = (n − u)/(2n).
- Here that polynomial is g(u) = 2⁷n⁷·E₇(x) =
  u·(427n⁶ − 175n⁴u² + 21n²u⁴ − u⁶): with z = u/n, x = (1 − z)/2, and
  E₇(1 − x) = −E₇(x) with 2⁷·E₇((1+z)/2) = z⁷ − 21z⁵ + 175z³ − 427z
  give it. In s = n², v = u² the cubic
  factor is (7s − v)³ + 28s²(3s − v): (7s − v)³ = 343s³ − 147s²v + 21sv² − v³
  and 28s²(3s − v) supplies the missing 84s³ − 28s²v. That form,
  `(7*a*a-u*u)**3+28*a**4*(3*a*a-u*u)`, is 4 bytes under the expanded one.
- Odd k sharing a factor e with n are picked up too, so ½·Σ_y g(u) is
  Σ_{odd e | n} d(n/e), with d the formula value (d(n) = a(n) for n ≥ 2,
  d(1) = T₈/2). `D` holds 2·d, and each pass subtracts the stored
  2·d(n/e) for the odd divisors e > 1 of n: over y = 2 … 2n+1, a full
  residue system mod 2n, `y%2>a%y` is true exactly for those e, and for
  y > n the index `a//y` is 0 with D[0] = 0. Starting at y = 2 avoids a
  division by zero (y = 0) and the missing D[n] (y = 1).
- `D[a]>>1%a` halves 2·d(n) for n > 1; for n = 1, 1%1 = 0 and the stored
  value g(1) + g(0) = 216 + 56 + 0 = 272 is printed as it is.

**Notes**

- The expanded polynomial `(427*a**6-175*a**4*u*u+21*a*a*u**4-u**6)`:
  155 bytes. Naming w = a² once per pass (`w=a*a;`) saves exactly what it
  costs.
- Exact integer arithmetic; correctness for every n rests on the Gauss-sum
  and Fourier identities above (as for [A000176](../A000176/), the
  character (n|k) is the one that matches the data).
- Each term takes O(n) steps: the whole b-file in about 3 s, about 4100
  terms in 60 s here. a(n) grows like n^7.5, far from the 4300-digit
  int-to-str limit.
- The b-file has 1000 terms (up to a(1000)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 155 | first entry |
| 2026-11-07 | Python 3 | 151 | cubic factor as (7n²−u²)³ + 28n⁴(3n²−u²) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000518), CC BY-SA 4.0.
