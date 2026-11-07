# A000996

> Shifts 3 places left under binomial transform.
> — [OEIS A000996](https://oeis.org/A000996)

Offset 0: 1, 0, 0, 1, 1, 1, 2, 6, 17, 44, 112, 304, 918, 3040, 10623, 38161, 140074, 528594, 2068751, 8436893, …

### Python 3 — 64 bytes

```python
*q,r=1,0,0,[]
for u in q:print(u);r=[u:=u+x for x in[0]+r];q+=u,
```

**How it works**

- The binomial-transform triangle: T(n,0) = a(n) and
  T(n,k) = T(n,k−1) + T(n−1,k−1). By induction T(n,k) = Σ_j C(k,j) a(n−j),
  so the last entry of row n is T(n,n) = Σ_j C(n,j) a(j), the binomial
  transform of the sequence at n. Here that is a(n+3).
- Row n must start with a(n), the end of the pass three rows back. Rather
  than rotating three variables (`u,v,w=v,w,u`, 3 bytes longer), the ends
  go into a list `q` that the `for` loop reads while it grows: pass n reads
  u = a(n), builds row n as the running sum of `[0]+r` started at u, and
  appends where the sum ends, T(n,n) = a(n+3).
- `*q,r=1,0,0,[]` sets q = [a(0), a(1), a(2)] and the empty row −1 in one
  assignment, a byte under `q=[1,0,0];r=[]`.
- [A000997](../A000997/) is the same program with the start values 0, 1, 0;
  the shift-2 relatives are [A000994](../A000994/) and [A000995](../A000995/).

**Notes**

- Exact integer additions, about n²/2 of them for n terms.
- The b-file has 301 terms and they print in under 0.1 s; the bar is the
  whole b-file in 60 s. After 2338 terms (2 s) the terms pass 4300 digits
  and the interpreter's int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000996), CC BY-SA 4.0.
