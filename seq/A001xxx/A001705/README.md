# A001705

> Generalized Stirling numbers, [n+2,3]_2: a(n) = n! * Sum_{k=0..n-1} (k+1)/(n-k).
> — [OEIS A001705](https://oeis.org/A001705)

Offset 0: 0, 1, 5, 26, 154, 1044, 8028, 69264, 663696, 6999840, 80627040, 1007441280, 13575738240, …

### Python 3 — 43 bytes

```python
a=-1;f=c=1
while[print(a:=a*c+f)]:f*=c;c+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). With N = n + 2, K = 3, r = 2 that is the coefficient of x in
  Pₙ(x) = (x+2)(x+3)⋯(x+n+1) (n factors; P₀ = 1). Multiplying by the next
  factor, x + n + 1, gives a(n) = (n+1)·a(n−1) + Pₙ₋₁(0) = (n+1)·a(n−1) + n!,
  the recurrence in the entry.
- Before a(n) is printed, c = n + 1 and f = n!: the walrus `a:=a*c+f` applies
  the recurrence inside `print`, then `f*=c` and `c+=1` move on.
- The loop starts one step before a(0). With c = 1 and f = 0! = 1 the
  recurrence reads a(0) = a(−1) + 1, and a(0) = 0 (P₀ has no x term) needs
  a(−1) = −1. So a starts at −1, and f and c share one assignment.

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1556); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (446 terms, n = 0 to 445) prints in well under a second; the bar is the whole b-file in 60 s.
- With `print(a)` first and the update in the body, `a=0;f=c=1` /
  `while[print(a)]:c+=1;a=a*c+f;f*=c`, it is 45 bytes, like
  [A000254](../../A000xxx/A000254/) (r = 1).
- [A001711](../A001711/), [A001716](../A001716/) and [A001721](../A001721/) are
  the coefficients of x for r = 3, 4, 5.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001705), CC BY-SA 4.0.
