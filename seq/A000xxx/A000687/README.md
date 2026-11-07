# A000687

> Boustrophedon transform (first version) of Fibonacci numbers 0,1,1,2,3,5,...
> — [OEIS A000687](https://oeis.org/A000687)

Offset 0: 1, 1, 2, 6, 17, 59, 229, 1029, 5242, 30040, 191201, 1338897, 10228097, 84647981, 754437958, …

### Python 3 — 71 bytes

```python
r=[t:=1];f=-1
while[print(t)]:r=[t:=t+(f:=x)for x in[r[0]+f-t]+r[::-1]]
```

**How it works**

- The OEIS terms are the transform of u = 1, 0, 1, 1, 2, 3, 5, …, that is
  u(n) = F(n−1) with F(−1) = 1: Hadjicostas's e.g.f. in the entry is
  (sec x + tan x)·(1 + ∫₀ˣ Σ F(m)tᵐ/m! dt), and the integral shifts the
  Fibonacci numbers one place. ("First version": the transform of
  0, 1, 1, 2, … itself would start with 0.) With this u,
  the boustrophedon transform of u is b(n) = T(n,n) in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young).
  Row n is the running sums of u(n) followed by row n−1 read backwards,
  exactly the triangle of [A000111](../A000111/), which is the transform of
  1, 0, 0, 0, …
- u(n+1) = u(n) + u(n−1) for every n ≥ 0, with u(−1) = F(−2) = −1. The
  program gets u(n) for free as `r[0]`, the first entry of the old row, and
  keeps u(n−1) in `f`: the walrus `(f:=x)` stores every x the row reads,
  and the last x read is the first entry of the row before, u(n−1). So
  `r[0]+f` is the next row's first entry; `f=-1` starts it at u(−1).
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `r[0]+f-t` brings it to u(n+1), the row's first entry; then it adds the
  old row reversed. When the comprehension ends, `t` is the new row's last
  entry, the next term, which the `while` header prints.

**Notes**

- A separate pair `f,g=0,1` … `f-t` … `;f,g=g,f+g` is 4 bytes longer, and
  `f+(f:=r[0])` inside the list is not allowed (no walrus in a
  comprehension's iterable). Reading u(n−1) from the old row as
  `r[-1]-r[-2]` would need a row 0 with two entries.
- The values were checked against the e.g.f. above for every printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 483 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000687), CC BY-SA 4.0.
