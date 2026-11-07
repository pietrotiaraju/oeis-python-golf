# A000998

> From a differential equation.
> — [OEIS A000998](https://oeis.org/A000998)

Offset 0: 1, 3, 6, 11, 24, 69, 227, 753, 2451, 8004, 27138, 97806, 375313, 1511868, 6292884, 26826701, 116994453, 523646202, 2414394601, 11487130362, …

### Python 3 — 67 bytes

```python
*q,r=1,0,0,[0,0]
for u in q:r=[u:=u+x for x in[0]+r];q+=u,;print(u)
```

**How it works**

- The entry (Alois P. Heinz's Maple) defines b(0..2) = 0, 0, 1,
  b(n+3) = Σ_j C(n,j) b(j) and a(n) = b(n+5): b shifts 3 places left under
  the binomial transform (for its e.g.f. B, B‴ = eˣB).
- The binomial-transform triangle: T(n,0) = b(n) and
  T(n,k) = T(n,k−1) + T(n−1,k−1). By induction T(n,k) = Σ_j C(k,j) b(n−j),
  so the last entry of row n is T(n,n) = Σ_j C(n,j) b(j), the binomial
  transform of the sequence at n. Here that is b(n+3).
- Row n must start with b(n), the end of the pass three rows back, so the
  ends go into a list `q` that the `for` loop reads while it grows: pass n
  reads u = b(n), builds row n as the running sum of `[0]+r` started at u,
  and appends where the sum ends, b(n+3).
- The program starts at pass 2, with q = [b(2), b(3), b(4)] = [1, 0, 0]
  and row 1 = [b(1), b(1)+b(0)] = [0, 0] (`*q,r=1,0,0,[0,0]`), and prints
  the value it appends, so the output starts at b(5) = a(0) with no
  skipping. Printing the read value instead would need the start
  q = [1, 3, 6] with row 4 = [0, 0, 1, 3, 6], 3 bytes longer.
- [A000996](../A000996/) and [A000997](../A000997/) are the same triangle
  with other start values.

**Notes**

- Exact integer additions, about n²/2 of them for n terms.
- The b-file has 696 terms and they print in 0.1 s; the bar is the whole
  b-file in 60 s. After 2333 terms (2 s) the terms pass 4300 digits and
  the interpreter's int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000998), CC BY-SA 4.0.
