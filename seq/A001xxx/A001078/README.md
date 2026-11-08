# A001078

> a(n) = 10*a(n-1) - a(n-2) with a(0) = 0, a(1) = 2.
> — [OEIS A001078](https://oeis.org/A001078)

Offset 0: 0, 2, 20, 198, 1960, 19402, 192060, 1901198, 18819920, …

### Python 3 — 34 bytes

```python
a=b=-2
while[print(a:=a-b)]:b-=8*a
```

**How it works**

- The recurrence a(n+1) = 10a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 8a(n), so the first difference
  d(n) = a(n+1) − a(n) obeys d(n) = d(n−1) + 8a(n).
- Before the print of a(n), `a` = a(n−1) and `b` = −d(n−1). The walrus
  `a:=a-b` adds the difference and prints a(n); `b-=8*a` then makes `b`
  = −d(n−1) − 8a(n) = −d(n), the same shape one step on.
- The start is one step back: a(−1) = 10a(0) − a(1) = −2 and
  b = −d(−1) = a(−1) − a(0) = −2, so `a=b=-2`. Storing the difference
  negated is what makes the two start values equal. Exact integers.

**Notes**

- Without the step back, `a=0;b=2` / `while[print(a)]:a+=b;b+=8*a` is 35
  bytes, and the tuple form `a,b=0,2` / `while[print(a)]:a,b=b,10*b-a` is 37.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter; the mirror
  `while[print(b:=b-a)]:a-=8*b` is the same length.
- a(n) = 2·[A004189](https://oeis.org/A004189)(n), and with
  [A001079](../A001079/) (same recurrence) (5 + 2√6)ⁿ = A001079(n) + a(n)·√6.
  [A001080](../A001080/), [A001084](../A001084/) and [A001090](../A001090/)
  use the same shape.
- Python's 4300-digit int-to-str limit stops the program at a(4320), the
  first term with 4301 digits, after printing a(0) to a(4319).
- The b-file has 1001 terms (a(0) to a(1000), 995 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001078), CC BY-SA 4.0.
