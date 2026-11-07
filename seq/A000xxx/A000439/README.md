# A000439

> Powers of rooted tree enumerator.
> — [OEIS A000439](https://oeis.org/A000439)

Offset 1: 9, 30, 69, 133, 230, 369, 560, 814, 1143, 1560, …

Let T(x) = x + x² + 2x³ + 4x⁴ + 9x⁵ + … count rooted trees
([A000081](../A000081/)). Riordan tabulates the powers T(x)ⁿ; this is the
column a(n) = [x^(n+4)] T(x)ⁿ, the fifth coefficient of the n-th power.

### Python 3 — 45 bytes

```python
n=1
while[print((n*n+9*n+1)**2//24+4*n)]:n+=1
```

**How it works**

- With T(x) = x(1 + u), u = x + 2x² + 4x³ + 9x⁴ + …, a(n) = [x⁴](1 + u)ⁿ
  = Σ_k C(n, k)·[x⁴]u^k. The x⁴ coefficients of u, u², u³, u⁴ are
  9, 2·4 + 2² = 12, 3·2 = 6 and 1, so

  a(n) = 9·C(n,1) + 12·C(n,2) + 6·C(n,3) + C(n,4)
       = (n⁴ + 18n³ + 83n² + 114n)/24,

  the polynomial on the OEIS page (Plouffe), now with a proof.
- Complete the square: (n² + 9n + 1)² = n⁴ + 18n³ + 83n² + 18n + 1, so
  24a(n) = t² − 1 + 96n with t = n² + 9n + 1, that is
  a(n) = (t² − 1)/24 + 4n.
- t² ≡ 1 (mod 24): n(n+9) is even (n and n+9 have opposite parity), so t
  is odd and t² ≡ 1 (mod 8); and n(n+9) ≡ n² ≡ 0 or 1 (mod 3), so 3 ∤ t
  and t² ≡ 1 (mod 3). Hence (t² − 1)/24 = ⌊t²/24⌋, which is
  `(n*n+9*n+1)**2//24`.
- `while[print(…)]:n+=1` is the usual loop: the list holding print's
  `None` is truthy.

**Notes**

- Other forms: Horner `n*(n*(n*(n+18)+83)+114)//24` in a `while 1:` loop,
  51 bytes; the factored `n*(n+3)*(n*n+15*n+38)//24`, 48 bytes, or 46
  as `(m-3)*m*(m*m+9*m+2)//24` with m = n+3; four running differences
  `a=0;b=9;c=12;d=6` / `while[print(a:=a+b)]:b+=c;c+=d;d+=1`, 52 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The b-file has 43 terms (up to a(43));
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |
| 2026-11-07 | Python 3 | 45 | complete the square: ⌊(n²+9n+1)²/24⌋ + 4n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000439), CC BY-SA 4.0.
