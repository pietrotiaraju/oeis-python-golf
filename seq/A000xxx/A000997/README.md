# A000997

> From a differential equation.
> — [OEIS A000997](https://oeis.org/A000997)

Offset 0: 0, 1, 0, 0, 1, 2, 3, 5, 12, 36, 110, 326, 963, 2964, 9797, 34818, 130585, 506996, 2018454, 8238737, …

### Python 3 — 64 bytes

```python
*q,r=0,1,0,[]
for u in q:print(u);r=[u:=u+x for x in[0]+r];q+=u,
```

**How it works**

- The entry's recurrence (Sean A. Irvine's Maple) is a(0..2) = 0, 1, 0 and
  a(n+3) = Σ_k C(n,k) a(k): the sequence shifts 3 places left under the
  binomial transform (keyword eigen; for the e.g.f. A this is A‴ = eˣA).
- The binomial-transform triangle: T(n,0) = a(n) and
  T(n,k) = T(n,k−1) + T(n−1,k−1). By induction T(n,k) = Σ_j C(k,j) a(n−j),
  so the last entry of row n is T(n,n) = Σ_j C(n,j) a(j), the binomial
  transform of the sequence at n. Here that is a(n+3).
- Row n must start with a(n), the end of the pass three rows back. Rather
  than rotating three variables (`u,v,w=v,w,u`, 3 bytes longer), the ends
  go into a list `q` that the `for` loop reads while it grows: pass n reads
  u = a(n), builds row n as the running sum of `[0]+r` started at u, and
  appends where the sum ends, T(n,n) = a(n+3).
- `*q,r=0,1,0,[]` sets q = [a(0), a(1), a(2)] and the empty row −1 in one
  assignment.
- [A000996](../A000996/) is the same program with the start values 1, 0, 0.

**Notes**

- Exact integer additions, about n²/2 of them for n terms.
- The OEIS has no b-file for this entry; the one here is synthesized from
  the 31 terms of the entry, and they print in under 0.1 s; the bar is the
  whole b-file in 60 s. The program also matches the entry's recurrence
  (computed directly with binomials) for 1000 terms, and stops after 2338
  terms (2 s) at the interpreter's 4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000997), CC BY-SA 4.0.
