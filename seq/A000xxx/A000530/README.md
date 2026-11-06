# A000530

> Let p(n, s, x) be predicate that number of occurrences of s's in x >= 2*n - the length of the longest sequence of s's in x. Then a(n)=#{x in {0,1}* | x ends in 0 and p(n,0,x) and (there is no prefix y of x such that p(n,0,y) or p(n,1,y))}.
> — [OEIS A000530](https://oeis.org/A000530)

Offset 1: 1, 5, 28, 226, 2077, 20770, 222884, 2529541, …

### Python 3 — 240 bytes

```python
from functools import*
n=0
while 1:
 n+=1
 @cache
 def f(a,b,r,s,t,u):
  if a+r>=2*n:return 1
  if b+s>=2*n:return 0
  v=t+1 if u==0 else 1;w=t+1 if u==1 else 1
  return f(a+1,b,max(r,v),s,v,0)+f(a,b+1,r,max(s,w),w,1)
 print(f(0,0,0,0,0,0))
```

**How it works**

- A state records the counts of 0 and 1 (a,b), their longest runs
  (r,s), the current trailing-run length t, and its symbol u.
- Extending by a bit updates its total count, its trailing run, and its
  longest run. A path stops as soon as either predicate count+longest
  run≥2n becomes true.
- A terminal 0-state contributes 1 and a terminal 1-state contributes 0.
  Thus every counted string ends in its first successful 0 step, with
  no earlier prefix satisfying either predicate. Here prefix is proper,
  as required for the definition to have nonzero values.
- Before termination each symbol count is less than 2n, so the search
  tree is finite. Memoization merges prefixes with identical statistics.

**Notes**

- Counts are exact integers. No finite table or assumed upper term is
  encoded; the next value is computed from the same stopping rule.
- The reference file contains 8 terms from the OEIS b-file; the verification
  bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 240 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000530), CC BY-SA 4.0.
