# A001077

> Numerators of continued fraction convergents to sqrt(5).
> — [OEIS A001077](https://oeis.org/A001077)

Offset 0: 1, 2, 9, 38, 161, 682, 2889, 12238, 51841, 219602, 930249, …

### Python 3 — 34 bytes

```python
a=b=1
while[print(a)]:a+=b;b=4*a-b
```

**How it works**

- √5 = [2; 4, 4, 4, …], so the convergents p/q obey p(k) = 4p(k−1) + p(k−2).
  The data starts with the formal p = 1 of 1/0, then 2, 9, 38, …: a(n) is
  the numerator of the (n−1)-th convergent, and a(n) = 4a(n−1) + a(n−2)
  with a(0) = 1, a(1) = 2.
- The program keeps the first difference d(n) = a(n+1) − a(n) instead of
  the previous term. The recurrence gives
  d(n+1) = 3a(n+1) + a(n) = 4a(n+1) − d(n), so `a+=b` steps `a` and
  `b=4*a-b` uses the new `a`.
- The start is a(0) = 1 and d(0) = 2 − 1 = 1: `a=b=1`. Exact integers.

**Notes**

- The tuple form `a,b=1,2` / `while[print(a)]:a,b=b,a+4*b` is 35 bytes. The
  [A001076](../A001076/) program (same recurrence, 33 bytes) would need
  `a=-2;b=-1` here, 37 bytes.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter; the mirror
  `while[print(b)]:b+=a;a=4*b-a` is the same length.
- a(n) = L(3n)/2 (Lucas numbers), and the differences in `b` are
  1, 7, 29, 123, … = L(3n+1). With [A001076](../A001076/) (the
  denominators) it gives a(n)² − 5·A001076(n)² = (−1)ⁿ.
- Python's 4300-digit int-to-str limit stops the program at a(6859), the
  first term with 4301 digits, after printing a(0) to a(6858).
- The b-file has 1001 terms (a(0) to a(1000), 627 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001077), CC BY-SA 4.0.
