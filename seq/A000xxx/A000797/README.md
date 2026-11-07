# A000797

> Numbers that are not the sum of 4 tetrahedral numbers.
> — [OEIS A000797](https://oeis.org/A000797)

Offset 1: 17, 27, 33, 52, 73, 82, 83, 103, 107, 137, 153, 162, 217, 219, 227, 237, 247, 258, 268, 271, …

### Python 3 — 121 bytes

```python
T=[];S={0};n=t=r=0
while 1:
 T+=t,;S|={t+x for x in T};r+=len(T);t+=r
 while n<t:any(n-s in S for s in S)or print(n);n+=1
```

**How it works**

- `T` lists the tetrahedral numbers k(k+1)(k+2)/6 found so far, built by
  two running sums (`r` is the triangular number, `t` the next tetrahedral
  number), and `S` is the set of all sums of two of them (0 included, so
  "sum of 4" means "of at most 4").
- n is a sum of 4 tetrahedral numbers exactly when n − s ∈ S for some
  s ∈ S. `any(n-s in S for s in S)` stops at the first hit; only the
  rare non-representable n scan all of S, and only those are printed.
- Every n is tested once, in order, after all tetrahedral numbers ≤ n are
  in `T`: the inner loop runs n up to the next tetrahedral number t, and
  adding t to `T` adds t + x to `S` for every x in `T` (t + t included).

**Notes**

- Keyword `fini`: Salzer and Levine conjecture (Pollock's conjecture in a
  sharper form) that there are exactly 241 terms, the last 343867. The
  program does not assume this: it never stops testing, so if a 242nd
  term exists it will print it. If the conjecture is true, it prints
  nothing after 343867 and runs forever, which the rules allow (the
  verifier stops it at the timeout).
- Exact integer arithmetic, no theorem needed.
- All 241 terms of the b-file come out in about 4 s; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000797), CC BY-SA 4.0.
