# A000547

> Number of steps to reach 1 in sequence A000546.
> — [OEIS A000547](https://oeis.org/A000547)

Offset 1: 0, 9, 18, 37, 25, 120, 36, 47, 42, 59, …

A000546(n) is the smallest start of a run of exactly n consecutive integers
that take the same number of 3x + 1 steps to reach 1, and a(n) is that number
of steps. For example 12 and 13 take 9 steps while 11 and 14 do not, so
a(2) = 9. The runs are maximal on both sides: 98, …, 102 all take 25 steps,
so 99, …, 102 is a run of four that 103 does not extend, yet A000546(4) = 314.

### Python 3 — 132 bytes

```python
f=lambda n:n>1and-~f([n//2,3*n+1][n%2])
D={};k=n=r=1;t=0
while s:=f(n:=n+1):D={r*(s!=t):t}|D;r=r*(s==t)+1;t=s;k+=k in D!=print(D[k])
```

**How it works**

- `f(n)` counts the steps: it is `False` (0) at n = 1 and otherwise one more
  than f of the next term, where `[n//2,3*n+1][n%2]` picks n/2 or 3n + 1.
  `-~x` is x + 1, also for a bool.
- The loop walks n = 2, 3, … and keeps the current run of equal step counts:
  `t` is its step count and `r` its length. When s = f(n) differs from t, the
  run that ends at n − 1 began right after a change too, so it is maximal on
  both sides, and it is stored as D[r] = t unless D already has a run of that
  length. `D={r*(s!=t):t}|D` does both: on equal keys the right operand of `|`
  wins, so the earlier run is kept, and when s = t the key is 0, a length
  that is never asked for. `r=r*(s==t)+1` then extends or restarts the run.
- Runs are disjoint and found in order of their starts, so the first run of
  length k that is stored is the one A000546(k) starts. Lengths turn up out
  of order (length 5 at 98 before length 4 at 314), so `k` is the next length
  to print. In `k+=k in D!=print(D[k])` the chained comparison calls print
  only when `k in D` holds, and then `D!=None` is true, so k moves on. At most
  one term is printed per n, which only delays the output: there are far more
  values of n than terms.
- `while s:=f(n:=n+1):` advances n and computes s in the header, a byte under
  `while 1:n+=1;s=f(n);`. It never stops, since f(n) ≥ 1 for n ≥ 2.

**Notes**

- Other versions: the first entry (an iterative step count in a `def`,
  `setdefault` and an inner `while k in D:` print loop) is 190 bytes;
  `n%2*(3*n+1)or n//2` as the next term is a byte longer; storing the start
  of each run instead of its step count and printing `f(D[k])` is 134 bytes.
- The arithmetic is exact, but the program rests on two open questions: that
  every start reaches 1 (the Collatz conjecture; otherwise f never returns)
  and that a maximal run of every length exists (otherwise the program waits
  forever for the missing length). The b-file shows runs up to length 100.
- `f` recurses once per step, so Python's default limit of 1000 frames needs
  a start with about 1000 steps. None exists below 10⁹: the most there is
  986 steps, for 670617279, far beyond the n this program reaches.
- On Python 3.12, `-~False` prints a DeprecationWarning on stderr, which the
  rules ignore.
- Speed: about 30 terms in 60 s here (the bar is reached in about 12 s); the
  19th term already needs n up to 159116. The b-file has 100 terms; the bar
  is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 190 | first entry |
| 2026-11-07 | Python 3 | 132 | recursive step count, first-wins dict union, print in a chained comparison |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000547), CC BY-SA 4.0.
