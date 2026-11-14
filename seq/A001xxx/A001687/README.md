# A001687

> a(n) = a(n-2) + a(n-5).
> — [OEIS A001687](https://oeis.org/A001687)

Offset 0: 0, 1, 0, 1, 0, 1, 1, 1, 2, 1, 3, 2, 4, 4, 5, 7, 7, 11, 11, 16, 18, 23, …

### Python 3 — 45 bytes

```python
l=[0,1,0,1,0]
for x in l:print(x);l+=l[-2]+x,
```

**How it works**

- The generating function is x/(1 − x² − x⁵), so for n ≥ 1 a(n) counts the
  compositions of n − 1 into parts 2 and 5; the program just runs the
  recurrence a(n) = a(n − 2) + a(n − 5) from a(0), …, a(4) = 0, 1, 0, 1, 0.
- `for x in l` keeps reading a list that grows while it is read. On the pass
  that reads x = a(i) the list holds a(0), …, a(i + 4), so `l[-2]` is
  a(i + 3) and `l+=l[-2]+x,` appends a(i + 5) = a(i + 3) + a(i). The list
  stays five terms ahead of the loop, so the loop never ends.

**Notes**

- Six seeds, `l=[0,1]*3` with `l+=l[-2]+l[-5],`, tie at 45 bytes; the
  shifting-tuple form `l=0,1,0,1,0` / `while 1:a,*l=*l,l[0]+l[3];print(a)` is
  46.
- Exact integers, so every term is right; a(n) grows like 1.2365ⁿ (the real
  root of x⁵ = x³ + 1), far from the 4300-digit int-to-str limit within any
  run.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001687), CC BY-SA 4.0.
