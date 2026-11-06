# A000237

> Number of mixed Husimi trees with n nodes; or rooted polygonal cacti with bridges.
> — [OEIS A000237](https://oeis.org/A000237)

Offset 0: 0, 1, 1, 3, 8, 26, 84, 297, 1066, 3976, 15093, 58426, 229189, …

### Python 3 — 169 bytes

```python
f=lambda x:sum(map(int.__mul__,L,x))
r=[1,1];L=[1];n=0
while[print(n and r[1])]:n-=1;L+=f(r),;r=[sum(d*(L[-d]+f(r[d-1::2]))*sum(r[~d:-1:-d])for d in range(n,0))//2//n]+r
```

**How it works**

- A rooted cactus is its root plus a multiset of blocks at the root. A block
  is a bridge to a smaller rooted cactus, or a polygon through the root whose
  other k vertices each carry a rooted cactus. Read around the polygon they
  form a sequence of k cacti, and a polygon and its mirror image are the same
  block. So blocks are nonempty sequences of rooted cacti up to reversal
  (k = 1 is the bridge), counted by b = BIK(a), and a(m+1) is the Euler
  transform of b at m: the OEIS formula T(a) = EULER(BIK(a)). As in
  [A000081](../A000081/), that gives
  **m·a(m+1) = Σ_{e=1..m} e·b(e)·Σ_{j≥1} a(m+1−je)**.
- BIK adds the sequences and the palindromes and halves:
  2b(e) = L(e) + S(e), with L = 1/(1−A) (all sequences) and
  S = (1+A(x))/(1−A(x²)) (palindromes: a half, its mirror, and an optional
  middle part). As sums over the list of L values,
  L(e) = Σ_{j<e} L(j)·a(e−j) with L(0) = 1, and
  S(e) = Σ_{j≤e/2} L(j)·a(e−2j) with a(0) read as 1 (no middle part).
- `r` holds a(m), …, a(1), newest first, followed by a 1 that stands for that
  empty middle. `f(x)` is the dot product of `L` with x, and `map` stops at
  the shorter one. `f(r)` is the next L(m): `L` has only m terms, so the 1 at
  the end is never reached. `f(r[d-1::2])` starts at a(e) and steps down by
  two to a(1) or to the 1 at the end, so it is S(e).
- With `n` = −m and d = −e, `L[-d]+f(r[d-1::2])` is 2b(e), and
  `r[~d:-1:-d]` is a(m+1−e), a(m+1−2e), …; the stop `-1` keeps the
  stand-in 1 out of this sum. Every d is negative, so the total is
  −2m·a(m+1), and `//2//n` turns it into a(m+1), which goes in front of `r`.
- The loop condition prints `r[1]`, which is a(−n). On the first pass `n` is
  0 and `r[1]` is the stand-in, so `n and` prints a(0) = 0 instead.

**Notes**

- Exact integer arithmetic, so the program is right for every n: both
  divisions are exact, since the sum is 2m times the integer a(m+1).
- S(e) is recomputed for every e, so a term costs O(m²) big-integer
  operations. The whole b-file (501 terms, n up to 500) still prints in
  about 3 s, and the bar is the whole b-file in 60 s. Keeping 2b(e) in a
  list of its own is about ten times faster but 11 bytes longer (180).
- a(n+1)/a(n) is near 4.49 at n = 500, so the decimal form passes Python's
  4300-digit int-to-str limit near n = 6600, far past the bar.
- The same program with the list in increasing order (the stand-in 1 in
  the a(0) slot) is 172 bytes. Leaving the stand-in out of `r` and adding it
  only in the palindrome slice, `(r+[1])[d-1::2]`, is 171.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 169 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000237), CC BY-SA 4.0.
