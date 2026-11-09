# A001236

> Differences of reciprocals of unity.
> — [OEIS A001236](https://oeis.org/A001236)

Offset 1: 15, 575, 46760, 6998824, 1744835904, 673781602752, 381495483224064, 303443622431870976, 327643295527342080000, …

### Python 3 — 73 bytes

```python
x=y=z=f=1;N=2
while[print(z:=N**3*z+f*(y:=N*N*y+f*(x:=N*x+f)))]:f*=N;N+=1
```

**How it works**

- With N = n + 1 the term is N!³·h₃(1, 1/2, …, 1/N), the complete
  homogeneous sum of 1/(ijk) over N ≥ i ≥ j ≥ k ≥ 1 (OEIS formula).
- Adding the variable 1/N gives hᵣ(N) = hᵣ(N−1) + hᵣ₋₁(N)/N, so with
  gᵣ = N!ʳ·hᵣ: gᵣ(N) = Nʳ·gᵣ(N−1) + (N−1)!·gᵣ₋₁(N), with g₀ = 1.
- `x`, `y`, `z` are g₁, g₂, g₃ and `f` is (N−1)!; the nested walruses
  update g₁, then g₂, then g₃ for the new N. All start at gᵣ(1) = 1.

**Notes**

- The whole b-file (70 terms) prints at once.
- The same recurrence as a list, `g=[1]*3` with
  `g=[s:=(t:=t*N)*x+f*s for x in g]`, is 81 bytes; it wins for
  [A001237](../A001237/) and [A001238](../A001238/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001236), CC BY-SA 4.0.
