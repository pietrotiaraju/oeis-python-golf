# A001948

> These numbers when multiplied by all powers of 4 give the numbers that are not the sums of 4 distinct squares.
> — [OEIS A001948](https://oeis.org/A001948)

Offset 1: 1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 17, 18, 19, 22, 23, 25, 27, 31, …

### Python 3 — 111 bytes

```python
f=lambda n,k,j=4:any(f(n-i*i,i,j-1)for i in range(k*(n>=0<j)))or n|j==0
n=0
while[f(n,n)<1<=n%4==print(n)]:n+=1
```

**Definition used**

The program prints the numbers n ≥ 1 that are not divisible by 4 and are
not sums of four distinct squares w² + x² + y² + z² with 0 ≤ w < x < y < z.
That is this sequence: by Pall's theorem (G. Pall, On sums of squares,
Amer. Math. Monthly 40 (1933), 10–18, linked from the OEIS entry, whose
comment quotes the statement from [A004437](https://oeis.org/A004437)),
the numbers that are not sums of
four distinct squares are exactly 4^k·m with k ≥ 0 and m among the 31
numbers 1, 2, 3, 5, …, 97, 103. None of the 31 is divisible by 4, so they
are exactly the non-sums that 4 does not divide, and no other number is.

**How it works**

- `f(n,k,j)` is the exhaustive search of [A001944](../A001944/): it tells
  whether n is a sum of j distinct squares i² with 0 ≤ i < k, choosing the
  largest square first (f(n, k, j) holds when f(n − i², i, j − 1) holds
  for some i < k; with no squares left only n = 0 counts). `range(k*(n>=0<j))`
  is empty once the remainder is negative or no squares are left, and
  `n|j==0` then decides. `f(n,n)` asks for four squares below n, which is
  enough because a square in a sum equal to n is at most n.
- `f(n,n)<1<=n%4==print(n)` is a chained comparison: `print` runs only
  when f is false and n is not a multiple of 4 (n = 0 is skipped too).
  The list `[False]` keeps the loop going.

**Notes**

- Nothing is stored: the program follows the definition for every n, and
  Pall's theorem is only needed to say that the list it prints is the
  whole sequence. After 103 it keeps searching forever without printing
  anything more.
- All 31 terms come at once (n ≤ 103 takes a few milliseconds); the bar is
  the whole list in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001948), CC BY-SA 4.0.
