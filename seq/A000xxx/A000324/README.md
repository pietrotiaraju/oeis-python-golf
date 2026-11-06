# A000324

> A nonlinear recurrence: a(0) = 1, a(1) = 5, a(n) = a(n-1)^2 - 4*a(n-1) + 4 for n>1.
> — [OEIS A000324](https://oeis.org/A000324)

Offset 0: 1, 5, 9, 49, 2209, 4870849, 23725150497409, …

### Python 3 — 32 bytes

```python
p=a=1
while[print(a)]:p*=a;a=p+4
```

**How it works**

- Shevelev's form on the OEIS page: a(n) = 4 + a(0)·a(1)·…·a(n−1) for
  n ≥ 1. It follows from the recurrence by induction: it holds at n = 1
  (4 + 1 = 5), and if a(n) = 4 + P with P the product before it, then
  4 + P·a(n) = 4 + (a(n) − 4)·a(n) = a(n)² − 4·a(n) + 4 = a(n+1).
- `p` is the product of the terms printed so far and `a` is the next term.
  Both start at 1: the empty product, and a(0) = 1.
- `print(a)` runs in the loop condition and always lets the loop go on;
  then `p*=a` multiplies the printed term in and `a=p+4` makes the next one.
- a(0) = 1 does not change the product, so the same two statements give
  a(1) = 5, which the quadratic recurrence cannot (it sends 1 to 1). This is
  the [A000289](../A000289/) program with 4 in place of 3.

**Notes**

- Exact integers, so every term is right.
- The recurrence itself is (a − 2)², and it needs a case for the first step.
  Keeping b = a − 1 turns it into b·(b − 2), which is 0 at the start, so an
  `or` supplies b(1) = 4: `b=0` + `while[print(b+1)]:b=b*(b-2)or 4` is
  35 bytes. `a=1` + `while[print(a)]:a=(a-2)**2+4//a` (4//a is 4 only at
  a = 1) is 36, and printing a(0) on its own, `print(1);b=3` +
  `while[print(b+2)]:b=b*b-2` (the Lucas numbers L(2ᵏ)), is 38.
- The number of digits doubles each step: a(12) has 857 digits, a(14) has
  3425 and a(15) about 6850, so Python's 4300-digit int-to-str limit stops
  the program after a(0) to a(14).
- The b-file has 13 terms (a(0) to a(12)) and they print at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000324), CC BY-SA 4.0.
