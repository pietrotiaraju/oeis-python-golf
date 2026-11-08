# A001084

> a(n) = 20*a(n-1) - a(n-2) with a(0) = 0, a(1) = 3.
> — [OEIS A001084](https://oeis.org/A001084)

Offset 0: 0, 3, 60, 1197, 23880, 476403, 9504180, 189607197, 3782639760, …

### Python 3 — 35 bytes

```python
a=b=-3
while[print(a:=a-b)]:b-=18*a
```

**How it works**

- `b` holds minus the first difference: before a(n) is printed, `a` is
  a(n−1) and `b` is a(n−1) − a(n), so the walrus `a:=a-b` in the print
  steps `a` to a(n).
- The recurrence a(n+1) = 20·a(n) − a(n−1) gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 18·a(n), which is `b-=18*a`.
- The start is one step before a(0), with the recurrence run backwards:
  a(−1) = 20·0 − 3 = −3 and a(−1) − a(0) = −3, so `a=b=-3`. Exact
  integers.

**Notes**

- The tuple form `a,b=0,3` / `while[print(a)]:a,b=b,20*b-a` and the
  [A001085](../A001085/) layout `a=0;b=3` / `while[print(a)]:a+=b;b+=18*a`
  are 36 bytes: the shift to a(−1) makes the two start values equal.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, `x=-x-K*y`, either order, K ≤ 24), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = 3·U(n−1, 10) (Chebyshev). With [A001085](../A001085/)
  (1, 10, 199, …, same recurrence) it gives the solutions of
  x² − 11y² = 1; [A001090](../A001090/) is the same program for U(n−1, 4).
- Python's 4300-digit int-to-str limit stops the program at a(3309), the
  first term with 4301 digits, after printing a(0) to a(3308).
- The b-file has 201 terms (a(0) to a(200), 260 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001084), CC BY-SA 4.0.
