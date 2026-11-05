# A000161

> Number of partitions of n into 2 squares.
> — [OEIS A000161](https://oeis.org/A000161)

Offset 0: 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, …

### Python 3 — 63 bytes

```python
s=[n:=0]
while[print(sum(k<=n-k in s for k in s))]:n+=1;s+=n*n,
```

**How it works**

- `s` holds the squares 0, 1, 4, …, n², more than enough: every square up
  to n is in it.
- A partition n = j + k into two squares with k ≤ j is counted once, by
  its smaller part k. The chained comparison `k<=n-k in s` means
  `k <= n-k and n-k in s`, so the sum counts the squares k ≤ n/2 whose
  complement n−k is a square too.
- `s=[n:=0]` sets up the list and the counter in one statement; each step
  appends the next square with `s+=n*n,`.
- A set (`s={n:=0}` … `s|={n*n}`) is a byte longer; it is faster, but the
  list already prints the b-file in time.

**Notes**

- Exact integer arithmetic, correct for every n. The membership test
  scans the list, but the chain only reaches it for k ≤ n/2, so a term
  costs O(n^1.5). The whole b-file (10001 terms) prints in about 32 s on
  the machine that set the bar, which is 8000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000161), CC BY-SA 4.0.
