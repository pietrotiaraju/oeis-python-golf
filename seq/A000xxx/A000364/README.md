# A000364

> Euler (or secant or "Zig") numbers: e.g.f. (even powers only) sec(x) = 1/cos(x).
> — [OEIS A000364](https://oeis.org/A000364)

Offset 0: 1, 1, 5, 61, 1385, 50521, 2702765, 199360981, 19391512145, …

### Python 3 — 65 bytes

```python
r=[0,t:=1]
while[t%2and print(t)]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- The secant numbers are the even-indexed Euler zigzag numbers,
  a(n) = [A000111](../A000111/)(2n), so the body is the Seidel–Entringer
  step of A000111 and [A000182](../A000182/): each row is the running sums
  of `[0]` followed by the row above reversed, and row m ends with
  A000111(m). `t` runs along the row as a walrus sum, and the `-t` in front
  brings it back to 0 for the leading entry.
- Only the even rows should be printed, and the test is the parity of the
  term instead of the row: the secant numbers A000111(2k) are all odd, and
  the tangent numbers A000111(2k − 1) are even for k ≥ 2 (both proofs are on
  the [A000182](../A000182/) page). `t%2and print(t)` prints exactly the odd
  ones.
- The only odd zigzag number in an odd row is A000111(1) = 1. The program
  starts from row 1, `[0,1]`, instead of row 0, `[1]`: its last entry is
  1 = a(0), so the first `print` gives a(0), and from then on the rows are
  2, 3, 4, … with the odd ones skipped by the parity test.
- `while[…]` loops forever because the list holds one element whatever the
  `and` returns.

**Notes**

- Exact integer arithmetic, correct for every n.
- Alternatives: starting from row 0 with `r=[t:=1]` and running the step
  twice per pass with `exec("…;"*2)` is 67 bytes; testing the row length
  with `len(r)%2and print(t)` from row 0 is 68; two rows per pass with
  `for t in 0,0:r=[t:=t+x for x in[0]+r[::-1]]` is 70.
- Row m has m + 1 entries, so a(n) costs about 2n² big-integer additions.
  The whole b-file (243 terms, n = 0 to 242) prints in well under a second;
  the program stops after a(829), when the next term passes the 4300-digit
  int-to-str limit of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000364), CC BY-SA 4.0.
