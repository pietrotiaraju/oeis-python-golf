# A000150

> Number of dissections of an n-gon, rooted at an exterior edge, asymmetric with respect to that edge.
> — [OEIS A000150](https://oeis.org/A000150)

Offset 0: 0, 0, 1, 2, 7, 20, 66, 212, 715, 2424, 8398, 29372, 104006, …

### Python 3 — 61 bytes

```python
c=n=1;l=[0]
for d in l:print(c-d>>1);l+=c,0;n+=1;c=4*c-6*c//n
```

**How it works**

- a(n) counts unordered binary trees with n internal nodes whose two subtrees
  differ. There are C(n) ordered ones (Catalan, [A000108](../A000108/)); the
  symmetric ones, with both subtrees equal, exist only for odd n, and there are
  C((n−1)/2) of them. So a(n) = (C(n) − d(n))/2, with d(n) = C((n−1)/2) for odd
  n and 0 for even n (Bodeen's formula on the OEIS page).
- `c` runs through the Catalan numbers with the [A000108](../A000108/) step
  `n+=1;c=4*c-6*c//n`; after the increment `n` is the index of the term just
  printed plus 2.
- `l` is a queue holding d: it starts as `[0]` and every pass appends the pair
  `c,0`, so l is 0, C(0), 0, C(1), 0, C(2), … and its entry number n is
  exactly d(n). The pass
  that prints a(n) has already appended n pairs, so the entry is there in time.
- `for d in l` walks the list while the body keeps extending it. A list
  iterator checks the length on every step, so the loop sees the new entries
  and never ends: the queue grows by two and is read by one per pass.
- `c-d>>1` is `(c-d)>>1`, since `-` binds tighter than `>>`. For n = 0 it
  gives (1 − 0)>>1 = 0, so the first term needs no special case.

**Notes**

- Reading d(n) as `l[n-1]` with `l=[0,1]`, `l+=0,c` and `while[print(...)]`
  is 64 bytes; keeping only the Catalan list and writing
  `n%2*c[n//2]` is 72.
- Python ints are exact; the program prints a(0) to a(7152) and then stops with
  a `ValueError` at the first Catalan number over the 4300-digit int-to-str
  limit of Python 3.11+. Those 7153 terms were checked against
  `(C(n)-n%2*C(n//2))//2`, with C from `math.comb`.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000150), CC BY-SA 4.0.
