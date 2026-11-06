# A000308

> a(n) = a(n-1)*a(n-2)*a(n-3) with a(1)=1, a(2)=2 and a(3)=3.
> — [OEIS A000308](https://oeis.org/A000308)

Offset 1: 1, 2, 3, 6, 36, 648, 139968, 3265173504, 296148833645101056, …

### Python 3 — 43 bytes

```python
a,b,c=1,2,3
while[print(a)]:a,b,c=b,c,a*b*c
```

**How it works**

- A window of three terms: a is printed, b and c are the next two, and
  `a,b,c=b,c,a*b*c` moves the window one step with the recurrence. It is the
  tribonacci loop of [A000213](../A000213/) with `*` in place of `+`.
- `while[print(…)]:` is a non-empty list, so it is always true.

**Notes**

- Products of integers, so every term is exact. In logarithms the recurrence
  is tribonacci: a(n) = 2^x(n)·3^y(n) where x and y follow
  x(n) = x(n−1) + x(n−2) + x(n−3).
- The seeds cannot be shortened. Running backwards gives a(0) = 3/2, and
  three equal seeds (`a=b=c=1` in A000213) would make every term a power of
  one number, while the terms need both 2 and 3; two equal seeds, as in
  `a=b=2;c=3`, would save 2 bytes.
- A search over update chains in the style of [A000301](../A000301/)
  (printing x or `x:=…`, then up to three statements `x*=…`, `x//=…`, `x=…`,
  with products, exact quotients and walruses of the three variables, up to
  17 bytes of printed expression plus body) found nothing that prints this
  sequence, so none of them beats the 16 bytes of `a` plus the tuple. In-place
  forms such as `c=a*(a:=b)*(b:=c)` (17 bytes) are longer than the tuple (15).
- a(19) has about 7740 digits, past Python's 4300-digit limit for converting
  an int to a string: the program prints a(1)…a(18) and stops with a
  `ValueError`. That is an interpreter limit, not a wrong term. The b-file
  has 15 terms (n = 1 to 15); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000308), CC BY-SA 4.0.
