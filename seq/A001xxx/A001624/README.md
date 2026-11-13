# A001624

> Related to Latin rectangles.
> — [OEIS A001624](https://oeis.org/A001624)

Offset 2: 1, 5, 58, 1274, 41728, 1912112, 116346400, 9059742176, …

### Python 3 — 157 bytes

```python
a=c=x=z=w=0;b=y=f=1;n=2
while f:=2**n*~-n-n*f:b,c,y,x,z,w=n*a,n*b,a+~-n*x+(X:=(a:=n*(n*a+b+2*c)-f)+2*~-n*x),X,X+x+y+(n-2)*(z+w),X+2*y+2*(n-2)*z;print(z);n+=1
```

**How it works**

- One of the auxiliary numbers in Kerawala's (1941) difference equation
  for 3-line Latin rectangles; the entry has no other definition than the
  recurrence (Sean A. Irvine, 2015, from that paper):
  **a(2) = 1, a(n) = x(n) + x(n−1) + y(n−1) + (n−2)·(a(n−1) + w(n−1))**,
  where x = [A001626](../A001626/), y = [A001627](../A001627/) and
  w = [A001625](../A001625/), which the entry links in turn:
  - x(n) = N(n) + 2(n−1)·x(n−1), x(1) = 0;
  - y(n) = N(n) + N(n−1) + 3(n−1)·x(n−1), y(1) = 1;
  - w(n) = x(n) + 2y(n−1) + 2(n−2)·a(n−1), w(2) = 2;

  with N = [A000186](../../A000xxx/A000186/), the 3 × n Latin rectangles
  with the first row in order. A001625's entry prints its factor as
  2(n−1); its terms need 2(n−2) (a(3) = 4 = 2 + 0 + 2·1·1), and that is
  what the program uses. With it the system reproduces every listed term
  of all four sequences (15, 15, 17 and 17 terms), so the program follows
  this system for every n.
- N comes from the A000186 program (see that page): at the top of the
  pass for n, `a` = N(n−1), `b` = (n−1)·N(n−2), `c` = (n−1)(n−2)·N(n−3),
  and N(n) = n(n·a + b + 2c) − f.
- One tuple assignment does the whole step. Its right side is evaluated
  left to right before anything is stored: `n*a`, `n*b` (the new b, c)
  read the old a, b; the y entry reads the old N(n−1) = `a` and x(n−1),
  then its walruses set `a` = N(n) (from the old b, c, which are not yet
  replaced) and `X` = x(n). The z and w entries read only old x, y, z, w
  and the new X. With x(n) − N(n) = 2(n−1)x(n−1) the y recurrence becomes
  y(n) = N(n−1) + (n−1)x(n−1) + x(n), which is what the y entry computes.
- The loop starts at n = 2 with the state after n = 1: N(1) = 0, b = N(0)
  = 1, c = 0, f = 1, x(1) = 0, y(1) = 1. The values of z and w there are
  never seen (both are multiplied by n − 2 = 0), so the first pass prints
  a(2) = x(2) + x(1) + y(1) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  loop condition never stops it: A000186's page shows f is never
  divisible by 3.
- The b-file has the 15 listed terms and prints at once; the bar is the
  whole b-file in 60 s. Fifteen terms fit in a table shorter than the
  program, so the program went through review.
- a(860) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 157 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001624), CC BY-SA 4.0.
