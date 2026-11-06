# A000289

> A nonlinear recurrence: a(n) = a(n-1)^2 - 3*a(n-1) + 3 (for n>1).
> — [OEIS A000289](https://oeis.org/A000289)

Offset 0: 1, 4, 7, 31, 871, 756031, 571580604871, …

### Python 3 — 32 bytes

```python
p=a=1
while[print(a)]:p*=a;a=p+3
```

**How it works**

- Shevelev's form on the OEIS page: a(n) = 3 + a(0)·a(1)·…·a(n−1) for
  n ≥ 1. It follows from the recurrence by induction: it holds at n = 1
  (3 + 1 = 4), and if a(n) = 3 + P with P the product before it, then
  3 + P·a(n) = 3 + (a(n) − 3)·a(n) = a(n)² − 3·a(n) + 3 = a(n+1).
- `p` is the product of the terms printed so far and `a` is the next term.
  Both start at 1: the empty product, and a(0) = 1.
- `print(a)` runs in the loop condition and always lets the loop go on;
  then `p*=a` multiplies the printed term in and `a=p+3` makes the next one.
- a(0) = 1 does not change the product, so the same two statements give
  a(1) = 4, which the quadratic recurrence cannot (it sends 1 to 1).

**Notes**

- With the recurrence itself the first step needs its own case:
  `a=1` + `while[print(a)]:a=max(4,a*a-3*a+3)` is 38 bytes.
- The number of digits doubles each step: a(12) has 753 digits, a(14) has
  3010 and a(15) has 6020, so Python's 4300-digit int-to-str limit stops the
  program after a(0) to a(14). Exact integers, so those are all right.
- The b-file has 13 terms (a(0) to a(12)) and they print at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000289), CC BY-SA 4.0.
