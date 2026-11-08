# A001079

> a(n) = 10*a(n-1) - a(n-2); a(0) = 1, a(1) = 5.
> — [OEIS A001079](https://oeis.org/A001079)

Offset 0: 1, 5, 49, 485, 4801, 47525, 470449, 4656965, 46099201, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a)]:a+=4*b;b+=2*a
```

**How it works**

- The recurrence a(n+1) = 10a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 8a(n). So the program keeps the first
  difference d(n) = a(n+1) − a(n) instead of the previous term:
  a(n+1) = a(n) + d(n) and d(n+1) = d(n) + 8a(n+1).
- Every d(n) is a multiple of 4: every a(n) is 1 mod 4 (true for 1 and 5,
  and 10·1 − 1 ≡ 1), so `b` holds d(n)/4. `a+=4*b` steps `a`, then
  `b+=2*a` uses the new `a`.
- The start is a(0) = 1 and d(0)/4 = (5 − 1)/4 = 1: `a=b=1`. Exact
  integers.

**Notes**

- Keeping d(n) itself, `a=1;b=4` / `while[print(a)]:a+=b;b+=8*a`, is also
  35 bytes (the start costs the 2 bytes that `4*` saves), and so is the
  walrus form of [A001078](../A001078/), `a=5;b=4` /
  `while[print(a:=a-b)]:b-=8*a`. The tuple form `a,b=1,5` /
  `while[print(a)]:a,b=b,10*b-a` is 37.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = T(n, 5) (Chebyshev); with [A001078](../A001078/) (same
  recurrence) (5 + 2√6)ⁿ = a(n) + A001078(n)·√6. [A001075](../A001075/),
  [A001091](../A001091/), [A001081](../A001081/) and
  [A001085](../A001085/) are the same program for T(n, 2), T(n, 4),
  T(n, 8) and T(n, 10).
- Python's 4300-digit int-to-str limit stops the program at a(4320), the
  first term with 4301 digits, after printing a(0) to a(4319).
- The b-file has 201 terms (a(0) to a(200), 199 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001079), CC BY-SA 4.0.
