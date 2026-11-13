# A001626

> Number of 3-line Latin rectangles.
> — [OEIS A001626](https://oeis.org/A001626)

Offset 1: 0, 0, 2, 36, 840, 29680, 1429920, 90318144, 7237943552, …

### Python 3 — 95 bytes

```python
a=n=1;b=c=x=0;f=-1
while f:=2**n*~-n-n*f:a,b,c=n*(n*a+b+2*c)-f,n*a,n*b;print(x:=a+2*~-n*x);n+=1
```

**How it works**

- This is one of the auxiliary numbers in Jacob's (1928) and Kerawala's
  (1941) difference equations for 3-line Latin rectangles. The entry
  gives it by the recurrence (Sean A. Irvine, 2015)
  **a(1) = 0, a(n) = N(n) + 2(n−1)·a(n−1)**, where
  N = [A000186](../../A000xxx/A000186/) counts the 3 × n Latin rectangles
  with the first row in order. The program follows that recurrence; it
  matches all 17 terms of the entry.
- N comes from the A000186 program: from Gessel's e.g.f. it derives
  u(n) = n·u(n−1) + u(n−2) + 2u(n−3) + E(n) for u(n) = N(n)/n!, and at
  the top of the pass for n keeps `a` = N(n−1), `b` = (n−1)·N(n−2),
  `c` = (n−1)(n−2)·N(n−3) and the correction `f`, so
  N(n) = n(n·a + b + 2c) − f (see that page).
- The loop starts at n = 1 with the state A000186 has after n = 0:
  a = N(0) = 1, b = c = 0, f = −1. The start value of `x` is never seen,
  because the recurrence multiplies a(0) by 2(1−1) = 0; so the first
  pass prints a(1) = N(1) = 0 without a guard.
- `print(x:=a+2*~-n*x)` updates and prints a(n) in one expression.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  loop condition never stops it: A000186's page shows f is never
  divisible by 3.
- The b-file has the 17 listed terms and prints at once; the bar is the
  whole b-file in 60 s.
- a(860) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001626), CC BY-SA 4.0.
