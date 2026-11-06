# A000107

> Number of rooted trees with n nodes and a single labeled node; pointed rooted trees; vertebrates.
> — [OEIS A000107](https://oeis.org/A000107)

Offset 0: 0, 1, 2, 5, 13, 35, 95, 262, 727, 2033, 5714, 16136, 45733, …

### Python 3 — 120 bytes

```python
v=n=0;r=s=1,
while[print(v)]:v=sum(map(int.__mul__,r,s));s=v,*s;n-=1;r+=sum(d*r[~d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- A vertebrate is a path from the root to the marked node, and each node on
  that path carries the rooted tree that hangs from it. So vertebrates are
  non-empty sequences of rooted trees, and with B(x) the g.f. of the rooted
  trees ([A000081](../A000081/)) the g.f. is **A = B/(1 − B)** (Harary and
  Robinson, on the OEIS page).
- The program works with C = 1 + A = 1/(1 − B) and the rooted forests
  F = B/x, so C = 1 + x·F·C, that is **c(k+1) = Σ_{i=0..k} f(i)·c(k−i)**,
  with c(0) = 1 and a(k) = c(k) for k ≥ 1.
- `r` holds f(0), f(1), …, f(k) in order and `s` holds c(k), …, c(1), c(0)
  backwards, so the convolution is the dot product
  `sum(map(int.__mul__,r,s))`: the two tuples always have the same length.
  The new term goes to the front of `s`.
- `r` grows by the recurrence of the [A000081](../A000081/) program,
  m·f(m) = Σ_{d=1..m} d·f(d−1)·Σ_{j≥1} f(m−jd), with d running over
  −m … −1 and `n` = −m. Since `r` starts at f(0) = b(1) instead of b(0),
  `r[~d]` (index |d| − 1) replaces `r[-d]`; the slices `r[d::d]` count from
  the end and do not change.
- `v` is the term being printed. It starts at a(0) = 0, which is the one
  place where a(k) and c(k) differ, so the 0 costs no `print(0)`. After
  that `v` is each new c(k+1) as it is put on `s`.
- `r=s=1,` starts both states as the same one-item tuple. Each update
  rebinds `s` and `r` independently; `s=v,*s` prepends the new term.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the
  division in the forest recurrence is exact.
- Each term costs O(n log n) big-integer operations. The whole b-file (1001
  terms) prints in under a second, and about 3900 terms print in 60 s. The
  bar is the whole b-file in 60 s.
- a(n) ~ 0.3618 · 2.9558ⁿ / √n ([A340310](https://oeis.org/A340310),
  [A051491](https://oeis.org/A051491)), so from about n = 9140 its decimal
  form passes Python's 4300-digit int-to-str limit.
- Keeping `s` as the a(k), with a(0) = 0, and printing `s[0]` needs a
  `+r[-1]` for the missing f(k)·c(0) term and comes out longer;
  `print(n and s[0])` in place of the `v` variable is 125 bytes.
- `math.sumprod(r,s)` is the same dot product, but `import math` costs more
  than it saves.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 121 | first entry |
| 2026-11-06 | Python 3 | 120 | keep r and s as tuples; prepend without a list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000107), CC BY-SA 4.0.
