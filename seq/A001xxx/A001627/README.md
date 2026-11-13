# A001627

> Related to Latin rectangles.
> — [OEIS A001627](https://oeis.org/A001627)

Offset 1: 1, 0, 2, 44, 1008, 34432, 1629280, 101401344, 8030787968, …

### Python 3 — 105 bytes

```python
a=n=1;b=c=g=0;f=-1
while f:=2**n*~-n-n*f:a,b,c=n*(n*a+b+2*c)-f,n*a,n*b;print(b//n+a+3*g);g=n*(a+2*g);n+=1
```

**How it works**

- One of the auxiliary numbers in Kerawala's (1941) difference equation
  for 3-line Latin rectangles. The entry defines it by the recurrence
  (Sean A. Irvine, 2015)
  **a(n) = N(n) + N(n−1) + 3(n−1)·x(n−1)**, a(1) = 1, with
  N = [A000186](../../A000xxx/A000186/) (3 × n Latin rectangles with the
  first row in order) and x = [A001626](../A001626/),
  x(n) = N(n) + 2(n−1)·x(n−1), x(1) = 0. The program follows it and
  matches all 17 terms of the entry.
- N comes from the A000186 program (see that page): at the top of the
  pass for n, `a` = N(n−1), `b` = (n−1)·N(n−2), `c` = (n−1)(n−2)·N(n−3)
  and N(n) = n(n·a + b + 2c) − f. After the update `a` = N(n) and
  `b` = n·N(n−1), so `b//n` is the old N(n−1).
- x itself is never stored: `g` keeps (n−1)·x(n−1), the product both
  recurrences use. Then a(n) = N(n−1) + N(n) + 3g, and the next g is
  n·x(n) = n·(N(n) + 2g). That is 4 bytes under keeping x and writing
  `3*~-n*x` and `2*~-n*x`.
- The loop starts at n = 1 with the state A000186 has after n = 0
  (a = N(0) = 1, b = c = 0, f = −1) and g = 0·x(0) = 0, so the first
  pass prints a(1) = N(0) + N(1) = 1.

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
| 2026-11-13 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001627), CC BY-SA 4.0.
