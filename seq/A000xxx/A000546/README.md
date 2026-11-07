# A000546

> First occurrence of n consecutive numbers that take same number of steps to reach 1 in 3x+1 problem.
> — [OEIS A000546](https://oeis.org/A000546)

Offset 1: 1, 12, 28, 314, 98, 386, 943, 1494, 1680, 4722, …

The Collatz map sends x to x/2 if x is even and to 3x + 1 if x is odd; the
number of steps x takes to reach 1 is its stopping time. a(n) is the
smallest start of a maximal block of exactly n consecutive numbers with the
same stopping time: 12 and 13 both take 9 steps, while 11 takes 14 and 14
takes 17, so a(2) = 12.

### Python 3 — 121 bytes

```python
f=lambda n:n>1and-~f(n%2*(5*n+2)+n>>1)
D={};n=p=k=1
while n:=n+1:f(n)==f(n-1)or[D:={n-p:p}|D,p:=n];k+=k in D!=print(D[k])
```

**How it works**

- **Maximal blocks.** The blocks must be maximal on both sides: a(5) = 98
  starts a block of five, 98 to 102, yet a(4) = 314 is larger, so the four
  numbers 98 to 101 inside it do not count. The scan cuts the numbers into
  maximal blocks, and blocks end in increasing order, so the first block of
  each length found is the earliest one.
- **The stopping time.** `n%2*(5*n+2)+n>>1` is (6n + 2)/2 = 3n + 1 for odd
  n and n/2 for even n (`>>` binds after `+` and `*`). `f(n)` adds 1 per
  step (`-~`) and returns `False`, that is 0, at n = 1.
- **The scan.** `p` is the start of the current block. When f(n) differs
  from f(n − 1), the block p, …, n − 1 of length n − p has ended:
  `{n-p:p}|D` adds it only if that length is new, since in a dict union
  the right operand wins, and `p` moves to n. The `or` skips this while
  the block goes on. The walrus in `while n:=n+1:` steps n, and n is never
  0.
- **Printing in order.** `k` is the next length to print. In
  `k in D!=print(D[k])`, a chained comparison, `print` runs only when
  `k in D` holds; it returns `None`, `D!=None` is `True`, and `k` goes up
  by 1. So at most one term prints per n, always in order of n, even when
  longer blocks turn up before shorter ones (a(20) = 79592 waits for
  a(19) = 159116).

**Notes**

- Other versions that print the same terms: keeping the last stopping
  time, `t=D={};n=p=k=1` and `t==(t:=f(n))or…`: 123 bytes, about twice as
  fast (27 terms in 60 s here); the previous program (a loop for the
  stopping time and `setdefault`): 190 bytes.
- Exact integer arithmetic. The program prints the right terms as long as
  every number it scans reaches 1 (the Collatz conjecture, checked far
  beyond any n reached here), and it can only go on printing if blocks of
  every length exist, which is not proved.
- The 20 terms of the bar print in about 25 s here (a(19) = 159116 is the
  slow one), and 27 terms in 60 s; under load it has fallen to 22. The
  b-file has 100 terms (up to a(100)).
- The recursion is f(n) + 1 calls deep. Every n < 1412987847 takes at most
  987 steps ([A006877](https://oeis.org/A006877)), so Python's default
  recursion limit of 1000 is far beyond the scan.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 190 | first entry |
| 2026-11-07 | Python 3 | 121 | recursive lambda, dict union keeps the first block, chained print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000546), CC BY-SA 4.0.
