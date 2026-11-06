# A000170

> Number of ways of placing n nonattacking queens on an n X n board.
> — [OEIS A000170](https://oeis.org/A000170)

Offset 0: 1, 1, 0, 0, 2, 10, 4, 40, 92, 352, …

### Python 3 — 122 bytes

```python
f=lambda c,d,e:c+1>>n or sum(f(c|b,(d|b)*2,(e|b)//2)for i in range(n)if(b:=1<<i)&~(c|d|e))
n=0
while[print(f(0,0,0))]:n+=1
```

**How it works**

- Backtracking with bitmasks, one row at a time. `c` holds the occupied
  columns; `d` and `e` hold the squares of the next row attacked along
  the two diagonals, so they shift left and right by one per row.
- A column i is free when bit `b = 1<<i` is clear in `c|d|e`. The walrus
  in the condition names `b` once for the three uses.
- `c+1>>n` is 1 exactly when all n columns are taken (`c = 2^n − 1`) and
  0 before, so the lambda returns the int 1 at a full board, including
  the empty board for n = 0.
- `n` is the global read at call time, so the lambda only carries the
  three masks.

**Notes**

- Exhaustive search, correct for every n. The running time grows about
  six-fold per n: on the machine that set the bar, a(0)…a(13) (14 terms)
  come out in about 19 s and a(14) would take about two minutes more. The
  bar is 13 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000170), CC BY-SA 4.0.
