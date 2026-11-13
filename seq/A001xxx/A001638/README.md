# A001638

> A Fielder sequence: a(n) = a(n-1) + a(n-3) + a(n-4), n >= 4.
> — [OEIS A001638](https://oeis.org/A001638)

Offset 0: 4, 1, 1, 4, 9, 11, 16, 29, 49, 76, 121, 199, 324, 521, 841, 1364, …

### Python 3 — 46 bytes

```python
l=4,1,1,4
while 1:a,*l=*l,sum(l)-l[2];print(a)
```

**How it works**

- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(0) to a(3) = 4, 1, 1, 4.
- `*l,sum(l)-l[2]` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l)-l[2]` = a(n) + a(n+1) + a(n+3), which is a(n+4) by the recurrence a(n+4) = a(n+3) + a(n+1) + a(n).
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(0).
- Integers are exact, so every term is right, for every n.

**Notes**

- The entry carries the keyword "changed"; its name, its g.f.
  (1 − x)(4 + x + x²)/((1 + x²)(1 − x − x²)) and its data agree, and the
  program follows them.
- x⁴ − x³ − x − 1 = (x² + 1)(x² − x − 1), so a(n) = L(n) + iⁿ + (−i)ⁿ with
  the Lucas numbers L ([A000032](../../A000xxx/A000032/)): a Fielder
  sequence, the sum of the n-th powers of the four roots. A Lucas pair
  plus a quarter-turn pair, `a=c=2;b=1;d=0` /
  `while[print(a+c)]:a,b,c,d=b,a+b,d,-c`, is 50 bytes.
- A search over chains of four in-place statements on four variables
  (`x+=y`, `x-=y`, `x=y-x`, `x±=2*y`, `x=-x`, any start) found none with
  this characteristic polynomial below 46 bytes.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(20575), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1001 terms (a(0) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001638), CC BY-SA 4.0.
