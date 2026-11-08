# A001080

> a(n) = 16*a(n-1) - a(n-2) with a(0) = 0, a(1) = 3.
> — [OEIS A001080](https://oeis.org/A001080)

Offset 0: 0, 3, 48, 765, 12192, 194307, 3096720, 49353213, 786554688, …

### Python 3 — 35 bytes

```python
a=b=-3
while[print(a:=a-b)]:b-=14*a
```

**How it works**

- The recurrence a(n+1) = 16a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 14a(n), so the first difference
  d(n) = a(n+1) − a(n) obeys d(n) = d(n−1) + 14a(n).
- Before the print of a(n), `a` = a(n−1) and `b` = −d(n−1). The walrus
  `a:=a-b` adds the difference and prints a(n); `b-=14*a` then makes `b`
  = −d(n−1) − 14a(n) = −d(n), the same shape one step on.
- The start is one step back: a(−1) = 16a(0) − a(1) = −3 and
  b = −d(−1) = a(−1) − a(0) = −3, so `a=b=-3`. Exact integers.

**Notes**

- This is the [A001078](../A001078/) program with 8 turned into 14 (and
  [A001084](../A001084/) has 18). Without the step back,
  `a=0;b=3` / `while[print(a)]:a+=b;b+=14*a` is 36 bytes, and so is the
  tuple form `a,b=0,3` / `while[print(a)]:a,b=b,16*b-a`.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter; the mirror
  `while[print(b:=b-a)]:a-=14*b` is the same length.
- With [A001081](../A001081/) (1, 8, 127, …, same recurrence) it gives the
  solutions of x² − 7y² = 1: (8 + 3√7)ⁿ = A001081(n) + a(n)·√7.
- Python's 4300-digit int-to-str limit stops the program at a(3577), the
  first term with 4301 digits, after printing a(0) to a(3576).
- The b-file has 201 terms (a(0) to a(200), 240 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001080), CC BY-SA 4.0.
