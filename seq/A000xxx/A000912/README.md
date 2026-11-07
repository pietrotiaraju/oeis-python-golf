# A000912

> Expansion of (sqrt(1-4x^2) - sqrt(1-4x))/(2x).
> — [OEIS A000912](https://oeis.org/A000912)

Offset 0: 1, 0, 2, 4, 14, 40, 132, 424, 1430, 4848, 16796, 58744, 208012, …

### Python 3 — 58 bytes

```python
c=n=1;l=[0]
for d in l:print(c-d);l+=c,0;n+=1;c=4*c-6*c//n
```

**How it works**

- The g.f. splits as (1−√(1−4x))/(2x) − x·(1−√(1−4x²))/(2x²) =
  c(x) − x·c(x²), with c the Catalan g.f., so a(n) = C(n) − d(n) with
  d(n) = C((n−1)/2) for odd n and 0 for even n (Deutsch's formula on the
  OEIS page).
- This is the [A000150](../A000150/) program without the final halving
  (A000912 = 2·A000150 for n > 0). `c` runs through the Catalan numbers
  with the [A000108](../A000108/) step `n+=1;c=4*c-6*c//n`.
- `l` is a queue for d: it starts as `[0]` and each pass appends `c,0`, so
  it reads 0, C(0), 0, C(1), 0, C(2), …, and its entry n is d(n).
  `for d in l` walks the list while the body extends it, two entries
  appended per entry read, so the loop never ends.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. The program prints 7153 terms in about a second (the first 2000
  checked against `C(n)-n%2*C(n//2)` with `math.comb`) and then stops with
  a `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000912), CC BY-SA 4.0.
