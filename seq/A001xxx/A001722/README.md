# A001722

> Generalized Stirling numbers, [n+7,7]_5.
> — [OEIS A001722](https://oeis.org/A001722)

Offset 0: 1, 18, 251, 3325, 44524, 617624, 8969148, 136954044, 2201931576, 37272482280, 663644774880, …

### Python 3 — 55 bytes

```python
a=0;b=1;f=c=5
while 1:c+=1;print(a:=a*c+b);b=b*c+f;f*=c
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). Here r = 5 and K = r + 2, so a(n) is the coefficient of x² in
  (x+5)(x+6)⋯(x+n+6), n + 2 factors.
- The program keeps the three lowest coefficients of the running product:
  f (constant term), b (x) and a (x²). Multiplying by x + c turns them into
  c·f, c·b + f and c·a + b; updating a, b, f in that order lets each update
  read the old value of the next one.
- It starts from the single factor x + 5 (a = 0, b = 1, f = 5) with c = 5.
  Each pass first moves c to the next factor and updates a inside `print`,
  so the first print is the coefficient of x² in (x+5)(x+6),
  a(0) = 1.

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1552); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (101 terms, n = 0 to 100) prints in well under a second; the bar is the whole b-file in 60 s.
- With the update of a as the loop condition (the form of
  [A000399](../../A000xxx/A000399/)), `while[print(a:=a*c+b)]:b=b*c+f;f*=c;c+=1`,
  c has to start one factor ahead of f, `f=5;c=6`, and the total is
  56 bytes.
- The same template gives [A001706](../A001706/) (r = 2), [A001712](../A001712/) (r = 3), [A001717](../A001717/) (r = 4); [A001723](../A001723/) is the coefficient of
  x³.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001722), CC BY-SA 4.0.
