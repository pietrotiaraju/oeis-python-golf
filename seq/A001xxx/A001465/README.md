# A001465

> Number of degree-n odd permutations of order 2.
> — [OEIS A001465](https://oeis.org/A001465)

Offset 0: 0, 0, 1, 3, 6, 10, 30, 126, 448, 1296, 4140, 17380, 76296, 296088, 1126216, …

### Python 3 — 58 bytes

```python
a=b=n=1;c=d=0
while[print(c)]:a,b,c,d=b,b+n*c,d,d+n*a;n+=1
```

**How it works**

- A permutation of order 2 is an involution other than the identity; it is
  odd when it has an odd number of 2-cycles (the identity is even, so it
  never counts). Let E(n) and O(n) count the involutions of n points with
  an even and an odd number of 2-cycles; a(n) = O(n).
- Point n is fixed (the rest is an involution of n−1 points with the same
  parity) or swapped with one of the other n−1 points, which adds one
  2-cycle and flips the parity of what is left on n−2 points:
  **E(n) = E(n−1) + (n−1)·O(n−2)** and
  **O(n) = O(n−1) + (n−1)·E(n−2)**, the involution recurrence of
  [A000085](../A000085/) split by parity.
- The four variables hold E(m), E(m+1), O(m), O(m+1) with `n` = m+1; the
  start is E(0) = E(1) = 1, O(0) = O(1) = 0. This is the
  [A000704](../A000704/) program (which prints E) printing O instead.

**Notes**

- a(n) = A000085(n) − A000704(n), and the e.g.f. is exp(x)·sinh(x²/2).
  Running the involution recurrence and its signed version
  S(n+1) = S(n) − n·S(n−1) side by side and printing (I − S)/2 is
  63 bytes.
- Exact integer arithmetic, O(1) multiplications per term, so the program
  is right for every n; the 4300-digit int-to-str limit stops it at
  a(2835).
- The b-file has 801 terms (n = 0 to 800); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001465), CC BY-SA 4.0.
