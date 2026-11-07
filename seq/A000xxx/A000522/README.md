# A000522

> Total number of ordered k-tuples (k=0..n) of distinct elements from an n-element set: a(n) = Sum_{k=0..n} n!/k!.
> — [OEIS A000522](https://oeis.org/A000522)

Offset 0: 1, 2, 5, 16, 65, 326, 1957, 13700, 109601, 986410, …

### Python 3 — 33 bytes

```python
a=n=0
while[print(a:=a*n+1)]:n+=1
```

**How it works**

- a(n) = Σ_{k=0}^{n} n!/k!. Multiplying a(n−1) by n gives every term of
  this sum except the last one, n!/n! = 1, so a(n) = n·a(n−1) + 1.
- The loop starts one step early: with `a=n=0` the first update gives
  0·0 + 1 = 1 = a(0), so the update sits inside `print` as a walrus and the
  body only counts. That is 3 bytes under `n=0;a=1` /
  `while[print(a)]:n+=1;a=n*a+1`.

**Notes**

- `a=n=1` / `while[print(a)]:a=a*n+1;n+=1`: 34 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The program stops after a(1558):
  a(1559) is the first term with more than 4300 digits, the int-to-str
  limit of Python 3.11+.
- The b-file has 451 terms (up to a(450)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |
| 2026-11-07 | Python 3 | 33 | start one step early, update inside print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000522), CC BY-SA 4.0.
