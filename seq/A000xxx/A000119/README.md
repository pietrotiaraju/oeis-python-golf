# A000119

> Number of representations of n as a sum of distinct Fibonacci numbers.
> — [OEIS A000119](https://oeis.org/A000119)

Offset 0: 1, 1, 1, 2, 1, 2, 2, 1, 3, 2, 2, 3, 1, 3, 3, 2, 4, 2, 3, 3, 1, 4, 3, 3, 5, …

### Python 3 — 75 bytes

```python
M=0,1;a=b=m=1
while[print(M[m])]:
 m+=1
 if m>b:a,b=b,a+b
 M+=M[-a]+M[b-m],
```

**How it works**

The Fibonacci numbers here are 1, 2, 3, 5, 8, …, with 1 used at most once.
Take F ≤ n < G for consecutive Fibonacci numbers F < G, and let
E = G − F ≤ F be the one before F. A representation of n either uses F or
it does not:

- With F, the rest adds up to n − F < E, which only numbers below F can
  make, so every representation of n − F works: a(n − F) ways.
- Without F, it cannot use G or anything larger either, so it is a subset
  of the Fibonacci numbers below F, which add up to G − 2. Swapping a
  subset for its complement in that set turns sum n into sum G − 2 − n,
  and that number is below E, so all of its representations lie in the
  set: a(G − 2 − n) ways, where a(−1) = 0 covers n = G − 1.

So a(n) = a(n − F) + a(G − 2 − n), and both arguments are below n.

- `M[i]` holds a(i − 1), so `M[0]` is the 0 that stands for a(−1).
  `while[print(M[m])]:` prints a(m − 1) in the loop condition (`[None]`
  is true), then the body appends `M[m]`.
- `a`, `b` are F and G for n = m − 1, that is a < m ≤ b. When `m` passes
  `b` the pair moves up one step: `a,b=b,a+b`.
- With the shift, the recurrence becomes `M[m]=M[m-a]+M[b-m]`. The tuple
  has exactly `m` items when the new one is computed, so `M[m-a]` is
  `M[-a]`.
- Starting from `a=b=1` (1 and 1 are two consecutive Fibonacci numbers)
  is 2 bytes shorter than `a=m=1;b=2`: the first step has m = 2 > b, so it
  moves the pair to 1, 2 before computing anything.
- `M+=x,` concatenates a one-item tuple.

**Notes**

- One addition per term: the whole b-file (n ≤ 6765) takes well under a
  second, and the bar is all 6766 terms in 60 s. The terms stay small,
  since a(n) ≤ √(n + 1) (Stockmeyer), and the tuple holds one int per term.
- A consequence of the recurrence: a(n) = 1 exactly when n + 1 is a
  Fibonacci number ([A000071](https://oeis.org/A000071)). Shifting on
  `M[m]<2` instead of `m>b` is longer, because the list index still needs
  `m` and `b`.
- Zumkeller's recursion from the OEIS entry,
  `f=lambda x,y=1,z=1:x>=y and f(x-y,y+z,y)+f(x,y+z,y)or 0**x` with the same
  print loop, is 86 bytes and walks every subset, about n^1.44 calls for
  term n: it gets to about n = 4150 in a minute.
- Keeping the multiset of all subset sums of the Fibonacci numbers seen so
  far and printing `s.count(n)` is 88 bytes.
- Popping the second terms off a copy `R=M[:a]` of the prefix, with
  `a=len(M)-1` at each new block, is 84 bytes. Writing the body on the
  `while` line with `a,b=(a,b,b,a+b)[m>b::2]`, or dropping `m` for
  `len(M)`, is 80.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 77 | first entry |
| 2026-11-06 | Python 3 | 75 | use a tuple for the initial M state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000119), CC BY-SA 4.0.
