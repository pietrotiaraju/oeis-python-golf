# A000279

> Card matching: coefficients B[n,1] of t in the reduced hit polynomial `A[n,n,n](t)`.
> — [OEIS A000279](https://oeis.org/A000279)

Offset 1: 3, 24, 216, 1824, 15150, 124416, 1014888, 8241792, 66724398, 538990800, …

### Python 3 — 74 bytes

```python
m=c=1
while 1:m+=1;print(3*sum(j*c*(c:=c*(m-j)//j)**2for j in range(1,m)))
```

**How it works**

- a(n) counts the arrangements of n A's, n B's and n C's with exactly one
  letter in its own block of n places. The OEIS formula is
  a(n) = 3n·Σ_k C(n,k+1)·C(n,k)·C(n−1,k), and n·C(n−1,k) = (k+1)·C(n,k+1),
  so with j = k+1 it becomes
  a(n) = 3·Σ_{j=1..n} j·C(n,j−1)·C(n,j)².
  A direct count of the arrangements matches for n ≤ 8.
- `m` is n+1. Inside the sum, `c` walks along row n of Pascal's triangle:
  it holds C(n,j−1) when the term starts, and the walrus replaces it with
  C(n,j) = C(n,j−1)·(n+1−j)/j, an exact division. Python evaluates
  `j*c` before the walrus, so the term gets the old and the new value.
- The last step is j = n, which leaves `c` = C(n,n) = 1: the walk resets
  itself for the next row, so `c` is set once at the start.
- `while 1:m+=1;print(…)` with `m=c=1` in one assignment is a byte under
  `m=2;c=1` / `while[print(…)]:m+=1`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file (300
  terms) prints in about a second, and about 2900 terms come out in 60 s
  on this PC. The bar is the whole b-file in 60 s.
- With `range(n)` and `-~k` in place of `range(1,m)` and `j` it is 75
  bytes; the same sum with `math.comb` is 93.
- a(n) = ((n+1)·f(n+1) − (5n+2)·f(n))/2 with the Franel numbers
  f = A000172 (from van Hoeij's formula and the Franel recurrence), and
  a(n) has an order-2 recurrence with degree-4 coefficients. Both cost
  more than the sum.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000279), CC BY-SA 4.0.
