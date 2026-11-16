# A001857

> a(1)=2, a(2)=3; for n >= 3, a(n) is smallest number that is uniquely of the form a(j) + a(k) with 1 <= j < k < n.
> — [OEIS A001857](https://oeis.org/A001857)

Offset 1: 2, 3, 5, 7, 8, 9, 13, 14, 18, 19, 24, 25, 29, 30, 35, 36, 40, 41, 46, 51, 56, …

### Python 3 — 78 bytes

```python
s={0};m=1
while m:=m+1:
 if m<4or len(s&{m-y for y in s})|1==3:print(m);s|={m}
```

**How it works**

- An Ulam-type sequence: after 2 and 3, each term is the least number above the previous one
  with exactly one representation a(j) + a(k), j < k. The scan goes up through m = 2, 3, …; `s`
  holds the terms found so far, all below m. A number skipped once stays skipped, since later
  terms are larger than m and add no representation of it, so scanning upward is the same as
  the definition.
- `s&{m-y for y in s}` is the set of terms z with m − z also a term. Each pair {z, m − z} with
  z ≠ m − z is counted twice and z = m/2 once, so m has exactly one representation with two
  distinct terms when the count is 2 or 3: `|1==3`.
- m < 4 lets 2 and 3 in. `s` starts as `{0}`, which is shorter than `set()` and harmless: 0
  pairs only with m itself, which is not in `s`.

**Notes**

- Exact integer arithmetic. Each candidate costs a pass over `s` (about n²/2·11 set lookups
  for n terms, since the terms grow like 11n), so the program slows down quadratically: term
  5000 comes after about 11 reference seconds and all 10000 terms of the b-file after about 46.
  The bar is 7000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001857), CC BY-SA 4.0.
