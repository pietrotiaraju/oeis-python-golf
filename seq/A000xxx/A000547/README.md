# A000547

> Number of steps to reach 1 in sequence A000546.
> — [OEIS A000547](https://oeis.org/A000547)

Offset 1: 0, 9, 18, 37, 25, 120, 36, 47, 42, 59, …

### Python 3 — 190 bytes

```python
def f(n):
 t=0
 while n>1:t+=1;n=3*n+1 if n%2 else n//2
 return t
D={};n=k=r=1;t=0
while 1:
 n+=1;s=f(n)
 if s==t:r+=1
 else:D.setdefault(r,(n-r,t));r=1;t=s
 while k in D:print(D[k][1]);k+=1
```

**How it works**

- Compute the ordinary Collatz stopping time by iterating until 1,
  counting each halving or 3n+1 step individually.
- Scan positive starting numbers in increasing order. `r` is the length
  of the current run of equal stopping times, and `t` is its value.
  Record a run only when the following stopping time changes: the OEIS
  condition requires a maximal run of exactly that length.
- `setdefault` keeps the first run of each length. Later occurrences
  cannot start earlier because the scan is ordered. The next required
  length `k` is printed as soon as its record exists, even when longer
  runs have already been discovered.
- The stored pair contains the run's starting integer and its stopping
  time. This entry prints the stopping time.

**Notes**

- Stopping times use exact integer operations and no recursion or large
  memoization table. The dictionary stores only one record per run length.
- Continued production depends on Collatz trajectories terminating and
  on runs of the required lengths existing; these are mathematical
  assumptions of extending this search, not inferred from a finite table.
- The reference file contains 100 published OEIS terms; the verification
  bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 190 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000547), CC BY-SA 4.0.
