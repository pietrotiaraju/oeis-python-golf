# A001453

> Catalan numbers - 1.
> — [OEIS A001453](https://oeis.org/A001453)

Offset 2: 1, 4, 13, 41, 131, 428, 1429, 4861, 16795, 58785, 208011, …

### Python 3 — 43 bytes

```python
c=2;n=3
while[print(c-1)]:n+=1;c=4*c-6*c//n
```

**How it works**

- a(m) = C(m) − 1 for m ≥ 2, where C(m) = C(2m, m)/(m + 1) is the m-th
  Catalan number; the offset 2 starts at C(2) − 1 = 1.
- The Catalan numbers satisfy C(m) = C(m − 1)·(4m − 2)/(m + 1). The loop
  keeps c = C(n − 1): it starts with C(2) = 2 and n = 3, prints c − 1, and
  after `n+=1` turns C(n − 2) into C(n − 1) = C(n − 2)·(4n − 6)/n
  = 4·C(n − 2) − 6·C(n − 2)/n.
- 6·C(n − 2)/n is an integer, being 4·C(n − 2) − C(n − 1), so `//` is exact
  and the program is right for every n. It is the update of
  [A000108](../../A000xxx/A000108/) with the start moved to C(2).
- `print(…)` runs in the loop condition: `[None]` is a non-empty list, so the
  condition is always true.

**Notes**

- Keeping c = C(n) instead, `c=n=2` + `while[print(c-1)]:n+=1;c=4*c-6*c//-~n`,
  is also 43 bytes; `math.comb(2*n,n)//-~n-1` with its import is 58.
- The b-file has 499 terms (n = 2 to 500); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001453), CC BY-SA 4.0.
