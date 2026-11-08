# A001076

> Denominators of continued fraction convergents to sqrt(5).
> — [OEIS A001076](https://oeis.org/A001076)

Offset 0: 0, 1, 4, 17, 72, 305, 1292, 5473, 23184, 98209, 416020, 1762289, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(a:=b-a)]:b+=4*a
```

**How it works**

- √5 = [2; 4, 4, 4, …], so the convergents p/q obey q(k) = 4q(k−1) + q(k−2).
  The data starts with the formal q = 0 of 1/0, then 1, 4, 17, …: a(n) is
  the denominator of the (n−1)-th convergent, and a(n) = 4a(n−1) + a(n−2)
  with a(0) = 0, a(1) = 1.
- This is the [Fibonacci](../../A000xxx/A000045/) program with `b+=a`
  turned into `b+=4*a`. Before the print of a(n), `a` = a(n−1) and
  `b` = a(n−1) + a(n); the walrus `a:=b-a` leaves a(n) and prints it.
- `b+=4*a` makes `b` = a(n−1) + 5a(n) = a(n) + a(n+1), the same shape one
  step on, so only one variable moves and there is no tuple swap.
- The start is a(−1) = a(1) − 4a(0) = 1 and b = a(−1) + a(0) = 1:
  `a=b=1`. Exact integers.

**Notes**

- The tuple form `a,b=0,1` / `while[print(a)]:a,b=b,a+4*b` is 35 bytes.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter; the mirror
  `while[print(b:=a-b)]:a+=4*b` is the same length.
- a(n) = F(3n)/2, and `b` runs through 1, 1, 5, 21, 89, … = F(3n−1) (from
  F(m) + F(m−3) = 2F(m−1)). The numerators are [A001077](../A001077/).
- Python's 4300-digit int-to-str limit stops the program at a(6860), the
  first term with 4301 digits, after printing a(0) to a(6859).
- The b-file has 1001 terms (a(0) to a(1000), 627 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001076), CC BY-SA 4.0.
