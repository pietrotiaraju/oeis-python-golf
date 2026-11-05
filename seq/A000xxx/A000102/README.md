# A000102

> a(n) = number of compositions of n in which the maximum part size is 4.
> — [OEIS A000102](https://oeis.org/A000102)

Offset 0: 0, 0, 0, 0, 1, 2, 5, 12, 27, 59, 127, 269, 563, 1167, 2400, …

### Python 3 — 63 bytes

```python
b=1,1,2;a=*b,4
while 1:x,*a=*a,sum(a);y,*b=*b,sum(b);print(x-y)
```

**How it works**

- Compositions of n with parts at most 4 are counted by the tetranacci
  number Q(n) = [A000078](../A000078/)(n+3) (1, 1, 2, 4, 8, 15, …), and
  those with parts at most 3 by the tribonacci number
  T(n) = [A000073](../A000073/)(n+2) (1, 1, 2, 4, 7, 13, …). The ones
  whose largest part is exactly 4 are the difference: a(n) = Q(n) − T(n).
- `a` is a sliding window of four tetranacci numbers and `b` one of three
  tribonacci numbers. `x,*a=*a,sum(a)` pops the oldest value into `x` and
  appends the sum of the window, which is the next term; the same with
  `b` gives `y`. Each turn `x` = Q(n) and `y` = T(n), and `print(x-y)`
  prints a(n).
- Both start at n = 0: Q(0…3) = 1, 1, 2, 4 and T(0…2) = 1, 1, 2. The two
  agree up to n = 3, so `a=*b,4` builds the first window from the second.
- The start is forced: if other windows printed the same differences,
  their errors would satisfy both recurrences at once, and
  x⁴ − x³ − x² − x − 1 = x·(x³ − x² − x − 1) − 1 shares no root with
  x³ − x² − x − 1.

**Notes**

- Same idea as [A000100](../A000100/) (largest part exactly 3), one size
  up. There, five plain variables in a `while[print(…)]` loop win; here
  the windows are longer and seven variables cost more than two starred
  unpackings: `a=b=c=w=x=y=0;z=1` +
  `while[print(c)]:a,b,c,w,x,y,z=b,c,a+b+c+w,x,y,z,w+x+y+z`
  (a(n) = a(n−1) + a(n−2) + a(n−3) + Q(n−4)) is 73 bytes.
- The same recurrence with windows, `a=0,0,0;b=0,1,1,2` +
  `while 1:x,*b=*b,sum(b);y,*a=*a,sum(a)+x;print(y)`, is 66 bytes.
- The sequence has an order-7 recurrence (g.f.
  x⁴/((1−x−x²−x³)(1−x−x²−x³−x⁴))), so any linear update needs seven
  numbers.
- Exact integers, so every term is right. The whole b-file (201 terms)
  prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000102), CC BY-SA 4.0.
