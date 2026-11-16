# A001834

> a(0) = 1, a(1) = 5, a(n) = 4*a(n-1) - a(n-2).
> — [OEIS A001834](https://oeis.org/A001834)

Offset 0: 1, 5, 19, 71, 265, 989, 3691, 13775, 51409, 191861, 716035, 2672279, 9973081, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(b)]:a+=b;b+=2*a
```

**How it works**

- One pass maps (a, b) to (a + b, b + 2(a + b)) = (a + b, 2a + 3b): the
  matrix [[1, 1], [2, 3]] has trace 4 and determinant 1, so by
  Cayley–Hamilton every coordinate obeys x(n + 1) = 4x(n) − x(n − 1).
- From `a=b=1` the values of `b` are 1, 5, …, the two seeds a(0) = 1,
  a(1) = 5, so `b` runs through the sequence. (The same loop printing `a`
  is [A001075](../A001075/), and `b` holds its differences.)
- `a+=b` steps `a`, then `b+=2*a` uses the new `a`; exact integers.

**Notes**

- The tuple form `a,b=1,5` / `while[print(a)]:a,b=b,4*b-a` is 35 bytes.
- With a walrus in the print, `a=-1;b=2` /
  `while[print(a:=a+b)]:b+=2*a` runs the same map but needs a longer start.
- 3·[A001835](../A001835/)(n + 1)² − a(n)² = 2.
- Python's 4300-digit int-to-str limit stops the program at a(7518) (an
  interpreter limit, not a wrong term).
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001834), CC BY-SA 4.0.
