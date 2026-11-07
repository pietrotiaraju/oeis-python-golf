# A000994

> Shifts 2 places left under binomial transform.
> — [OEIS A000994](https://oeis.org/A000994)

Offset 0: 1, 0, 1, 1, 2, 5, 13, 36, 109, 359, 1266, 4731, 18657, 77464, 337681, 1540381, 7330418, 36301105, 186688845, 995293580, …

### Python 3 — 59 bytes

```python
u,t,*r=1,0
while[print(u)]:r=[u:=u+x for x in[0]+r];u,t=t,u
```

**How it works**

- The binomial-transform triangle: T(n,0) = a(n) and
  T(n,k) = T(n,k−1) + T(n−1,k−1). By induction T(n,k) = Σ_j C(k,j) a(n−j),
  so the last entry of row n is T(n,n) = Σ_j C(n,j) a(j), the binomial
  transform of the sequence at n. Here that is a(n+2).
- `r` is row n−1; row n is the running sum of `[0]+r` started at a(n),
  `[u:=u+x for x in[0]+r]`, and the running sum ends at T(n,n) = a(n+2).
- Row n+1 must start with a(n+1), the end of the previous pass, kept in
  `t`: the swap `u,t=t,u` makes u = a(n+1) (printed next) and t = a(n+2).
  The start `u,t,*r=1,0` is a(0), a(1) and an empty row −1.
- [A000995](../A000995/) is the same program with the start values 0, 1;
  the shift-3 relatives are [A000996](../A000996/), [A000997](../A000997/)
  and [A000998](../A000998/).

**Notes**

- Exact integer additions, about n²/2 of them for n terms; only the current
  row is kept.
- The b-file has 651 terms and they print in 0.1 s; the bar is the whole
  b-file in 60 s. After 2195 terms (2 s) the terms pass 4300 digits and
  the interpreter's int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000994), CC BY-SA 4.0.
