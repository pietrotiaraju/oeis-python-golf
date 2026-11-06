# A000405

> Number of 6-level labeled rooted trees with n leaves.
> — [OEIS A000405](https://oeis.org/A000405)

Offset 0: 1, 1, 6, 51, 561, 7556, 120196, 2201856, 45592666, 1051951026, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*5
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

This is the exact Stirling-transform antidiagonal algorithm of
[A000307](../A000307/), with two additional transform levels.
The innermost e.g.f. is exp(x); applying five second-kind Stirling
transforms gives the six nested exponentials listed by the OEIS.
Each level obeys T(i+1,k) = k*T(i,k) + T(i,k+1).
The carried value `t` feeds the output of each level into the next.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 151 terms in 60 s; the official b-file contains 151 terms.
- Python 3.11+ eventually reaches its default 4300-digit integer-to-string limit; this interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000405), CC BY-SA 4.0.
