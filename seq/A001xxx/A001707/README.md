# A001707

> Generalized Stirling numbers, [n+5,5]_2.
> — [OEIS A001707](https://oeis.org/A001707)

Offset 0: 1, 14, 155, 1665, 18424, 214676, 2655764, 34967140, 489896616, 7292774280, 115119818736, …

### Python 3 — 68 bytes

```python
a=0;b=1;d=5;f=6;c=4
while[print(a:=a*c+b)]:b=b*c+d;d=d*c+f;f*=c;c+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). With N = n + 5, K = 5, r = 2, a(n) is the coefficient of x³ in
  (x+2)(x+3)⋯(x+n+4), n + 3 factors.
- The program keeps the four lowest coefficients of the running product,
  f, d, b, a (of 1, x, x², x³). Multiplying by x + c turns them into c·f,
  c·d + f, c·b + d and c·a + b; updating from the top down lets each update
  read the old value of the next one.
- The state starts at (x+2)(x+3) = x² + 5x + 6 (a = 0, b = 1, d = 5, f = 6)
  with c = 4, the next factor. The update of a sits in the loop condition, so
  the first print is the coefficient of x³ in (x+2)(x+3)(x+4), a(0) = 1.

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1553); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (101 terms, n = 0 to 100) prints in well under a second; the bar is the whole b-file in 60 s.
- The base-B digit read of [A001708](../A001708/), `import math` / `s=3` /
  `while[print(math.perm((B:=s**s)-~s,s)//B**3%B)]:s+=1`, ties at 68 bytes.
  Starting the row form from fewer factors would print zeros first.
- [A001706](../A001706/) is the coefficient of x², [A001708](../A001708/) and
  [A001709](../A001709/) those of x⁴ and x⁵; [A001713](../A001713/),
  [A001718](../A001718/) and [A001723](../A001723/) are x³ for r = 3, 4, 5.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001707), CC BY-SA 4.0.
