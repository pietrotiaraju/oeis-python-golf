# A001386

> Coordination sequence for 4-dimensional I-centered tetragonal orthogonal lattice.
> — [OEIS A001386](https://oeis.org/A001386)

Offset 0: 1, 12, 56, 164, 368, 700, 1192, 1876, 2784, 3948, 5400, 7172, 9296, …

### Python 3 — 41 bytes

```python
k=0
while[print(k*(k*k+20)//12or 1)]:k+=4
```

**How it works**

- The entry gives a(n) = 4·A004006(2n) for n > 0, with
  A004006(m) = m(m² + 5)/6, so a(n) = 4n(4n² + 5)/3 for n ≥ 1 and
  a(0) = 1 (the origin itself). This is O'Keeffe's coordination formula for
  the lattice (Zeit. f. Krist. 210, 1995).
- With k = 4n the formula is k(k² + 20)/12, an exact integer: the loop
  steps `k` by 4 and prints `k*(k*k+20)//12`.
- At k = 0 the formula gives 0, and `or 1` turns that one value into
  a(0) = 1; every later term is positive. `12or` is tokenized as `12`
  followed by `or` (Python warns on stderr, which is ignored).

**Notes**

- Keeping the previous term instead, `a=1;k=0` /
  `while[print(a)]:k+=4;a=k*(k*k+20)//12`, is 45 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (a(0) to a(1000)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001386), CC BY-SA 4.0.
