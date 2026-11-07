# A000749

> a(n) = 4*a(n-1) - 6*a(n-2) + 4*a(n-3), n > 3, with a(0)=a(1)=a(2)=0, a(3)=1.
> — [OEIS A000749](https://oeis.org/A000749)

Offset 0: 0, 0, 0, 1, 4, 10, 20, 36, 64, 120, 240, 496, 1024, 2080, 4160, 8256, 16384, …

### Python 3 — 44 bytes

```python
x=y=1
while[print(x*x+y*y>>2)]:x,y=x+y-1,y-x
```

**How it works**

- a(n) = Σₖ C(n, 4k+3) (OEIS), and the roots-of-unity filter gives
  4a(n) = 2ⁿ − 2·Im (1+i)ⁿ − 0ⁿ.
- Write (1+i)ⁿ = u + iv. Then u² + v² = |1+i|²ⁿ = 2ⁿ, so for n ≥ 1
  4a(n) + 1 = u² + v² − 2v + 1 = u² + (1−v)².
- The program keeps x = u and y = 1 − v. Multiplying by 1+i sends
  (u, v) to (u − v, u + v), which in the new variables is
  x → x + y − 1, y → y − x.
- `x*x+y*y>>2` drops the extra 1. For n = 0 (x = y = 1) it gives
  2 >> 2 = 0, which is right too.

**Notes**

- Exact integer arithmetic, two small multiplications per term.
- Other forms tried: the four binomial sums Σ C(n, 4k+r) rotated with
  `a,b,c,d=a+b,b+c,c+d,d+a` (51 bytes), the Gaussian pair plus 2ⁿ kept
  separately (49), and y = v − 1 with update `x,y=x+~y,x+y` (46).
- The whole b-file (201 terms) prints at once; it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000749), CC BY-SA 4.0.
