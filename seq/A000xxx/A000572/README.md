# A000572

> A Beatty sequence: [ n(e+1) ].
> — [OEIS A000572](https://oeis.org/A000572)

Offset 1: 3, 7, 11, 14, 18, 22, 26, 29, 33, 37, …

### Python 3 — 81 bytes

```python
n=1
while 1:
 N=F=1;k=0
 while -n*N%F<2*n:k+=1;N=N*k+1;F*=k
 print(n+n*N//F);n+=1
```

**How it works**

- `N/F` is the Taylor sum Σⱼ₌₀ᵏ 1/j!, with F=k!. Advancing k
  multiplies the old numerator by k and adds 1, so every partial sum
  is represented exactly.
- For k≥1 the remaining tail is smaller than 2/F: after multiplication
  by F it is bounded by Σᵣ₌₁∞(k+1)^(−r)=1/k≤1. Thus n·e lies in
  [nN/F,(nN+2n)/F).
- `-n*N%F` is the distance to the next integer in units of 1/F when
  the lower bound is nonintegral. The loop stops only when that
  distance is at least 2n, proving that the interval has one floor.
  A zero remainder forces further refinement. Since F=1 at k=0 and
  k=1, the loop always reaches the range where the tail bound applies.
- Irrationality of e ensures that refinement eventually succeeds for
  every positive n. Adding n then gives floor(n(e+1)).

**Notes**

- All precision decisions use exact integers and a proven Taylor tail
  bound. No fixed decimal approximation to e is embedded.
- The reference file contains 59 terms from the published OEIS entry; the verification
  bar is 59 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000572), CC BY-SA 4.0.
