# A001113

> Decimal expansion of e.
> — [OEIS A001113](https://oeis.org/A001113)

Offset 1: 2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, …

### Python 3 — 76 bytes

```python
N=2;F=Q=m=1
while-N%F<=Q or[print(N//F),N:=N%F*10,Q:=Q*10]:m+=1;N=N*m+Q;F*=m
```

**How it works**

- e = Σ 1/j!. After the terms up to 1/m!, the partial sum is N/F with
  F = m!, and the tail Σ_{j>m} 1/j! is below 1/(m·m!) ≤ 1/F. With Q = 10^d
  after d printed digits, the part still to print, 10^d·e minus the digits
  so far, lies strictly between N/F and (N + Q)/F.
- `-N%F<=Q` asks whether those two ends may have different integer parts
  (−N%F is the distance from N up to the next multiple of F). If so, the
  body takes in the next term: m → m + 1, N → N·m + Q (the new term is
  Q/m! = Q/F after `F*=m`).
- Otherwise the integer part N//F is certain: it is printed, the remainder
  is scaled by 10 (`N:=N%F*10`), and so is Q. That list is non-empty, so the
  condition is true either way and the body takes in a term every round, as
  in Gibbons' π spigot on [A000796](../../A000xxx/A000796/).
- The start N = 2, F = Q = m = 1 is 1/0! + 1/1! with tail e − 2 < 1.
  Exact integers throughout. The program never stalls: each term divides
  the width Q/F by m + 1, each digit multiplies it by 10, and the value is
  never an integer because e is irrational.

**Notes**

- `-N%F<=Q` is 1 byte under `N%F+Q>=F`. When N%F = 0 it takes another term
  instead of printing, which is only cautious.
- The whole b-file (50000 digits) takes about 13 s here; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001113), CC BY-SA 4.0.
