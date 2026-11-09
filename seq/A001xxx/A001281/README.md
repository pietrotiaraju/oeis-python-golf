# A001281

> Image of n under the map n->n/2 if n even, n->3n-1 if n odd.
> — [OEIS A001281](https://oeis.org/A001281)

Offset 0: 0, 2, 1, 8, 2, 14, 3, 20, 4, 26, 5, 32, 6, 38, …

### Python 3 — 36 bytes

```python
a=2
while[print(a//6),print(a)]:a+=6
```

**How it works**

- The terms come in pairs: n = 2j gives n/2 = j, and n = 2j + 1 gives
  3(2j + 1) − 1 = 6j + 2. So the sequence is j, 6j + 2 for j = 0, 1, 2, …
- `a` runs through 6j + 2 = 2, 8, 14, …; `a//6` is j because the
  remainder 2 is less than 6. Each pass prints j and then 6j + 2, which are
  a(2j) and a(2j+1).
- The list `[None, None]` from the two `print` calls is non-empty, so the
  loop never ends. Exact integers, so every term is right.

**Notes**

- One term per pass is longer: `[n//2,3*n-1][n%2]` in a counting loop is
  40 bytes and `n%2*(3*n-1)or n//2` is 41. Printing `a//6` in the loop
  condition and `a` in the body (`while[print(a//6)]:print(a);a+=6`) is
  also 36 bytes.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001281), CC BY-SA 4.0.
