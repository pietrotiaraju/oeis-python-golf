# A001581

> Winning moves in Fibonacci nim.
> — [OEIS A001581](https://oeis.org/A001581)

Offset 1: 4, 10, 14, 20, 24, 30, 36, 40, 46, 50, 56, 60, 66, 72, 76, 82, 86, 92, 96, 102, …

The game (as the OEIS entry explains): a pile of stones, each move removes a
Fibonacci number 1, 2, 3, 5, 8, … of them, and whoever makes the last move
wins. The terms are the positive losing positions for the player to move,
the positions a winning move leaves behind. Equivalently, with 0 in front,
the lexicographically least set of non-negative integers with no two
differing by a Fibonacci number.

### Python 3 — 87 bytes

```python
P={m:=0}
while 1:
 m+=1;a=b=1
 while(m-b in P)<(b<=m):a,b=b,a+b
 if b>m:P|={m};print(m)
```

**How it works**

- `P` holds the losing positions found so far, starting with 0 (no move
  left). A pile m is losing exactly when no move m → m − f, with f a
  Fibonacci number at most m, reaches a losing position.
- For each m, b runs through 1, 2, 3, 5, … (`a=b=1`, then `a,b=b,a+b`) while
  m − b is not in P and b ≤ m: `(m-b in P)<(b<=m)` is `False < True`.
- The loop ends either at a move into P (m is a winning position, b ≤ m) or
  with b > m (no such move). In the second case m joins P and is printed.

**Notes**

- Exact for every n, straight from the definition.
- About 30 set lookups per m: the whole b-file (165109 terms, up to
  999998) in about 7 s on the PC it was written on; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001581), CC BY-SA 4.0.
