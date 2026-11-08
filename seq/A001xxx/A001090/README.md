# A001090

> a(n) = 8*a(n-1) - a(n-2); a(0) = 0, a(1) = 1.
> — [OEIS A001090](https://oeis.org/A001090)

Offset 0: 0, 1, 8, 63, 496, 3905, 30744, 242047, 1905632, 15003009, 118118440, …

### Python 3 — 34 bytes

```python
a=b=-1
while[print(a:=a-b)]:b-=6*a
```

**How it works**

- `b` holds minus the first difference: before a(n) is printed, `a` is
  a(n−1) and `b` is a(n−1) − a(n), so the walrus `a:=a-b` in the print
  steps `a` to a(n).
- The recurrence a(n+1) = 8·a(n) − a(n−1) gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 6·a(n), which is `b-=6*a`.
- The start is one step before a(0), with the recurrence run backwards:
  a(−1) = 8·0 − 1 = −1 and a(−1) − a(0) = −1, so `a=b=-1`. Exact
  integers.

**Notes**

- The tuple form `a,b=0,1` / `while[print(a)]:a,b=b,8*b-a` and the
  [A001091](../A001091/) layout `a=0;b=1` / `while[print(a)]:a+=b;b+=6*a`
  are 35 bytes: the shift to a(−1) makes the two start values equal.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, `x=-x-K*y`, either order, K ≤ 24), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = U(n−1, 4) (Chebyshev). With [A001091](../A001091/) (1, 4, 31, …,
  same recurrence) it gives the solutions of x² − 15y² = 1;
  [A001084](../A001084/) is the same program for 3·U(n−1, 10).
- Python's 4300-digit int-to-str limit stops the program at a(4800), the
  first term with 4301 digits, after printing a(0) to a(4799).
- The b-file has 1001 terms (a(0) to a(1000), 896 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001090), CC BY-SA 4.0.
