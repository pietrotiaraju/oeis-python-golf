# A001178

> Fibonacci frequency of n.
> — [OEIS A001178](https://oeis.org/A001178)

Offset 1: 0, 4, 3, 2, 3, 1, 2, 2, 1, 2, 3, 1, 3, 2, 3, 1, 2, 1, 2, 2, …

### Python 3 — 103 bytes

```python
n=0
while 1:
 k=n=n+1;m=c=0
 while k-m:
  m=k;a=b=k=1;c+=1
  while a%m|~-b%m:a,b=b,a+b;k+=1
 print(c-1)
```

Uses the Pisano period loop of [A001175](../A001175/); the fixed point it
reaches gives [A001179](../A001179/).

**How it works**

- a(n) is the number of times the Pisano period map π has to be applied to n
  before the value stops changing: the least c with π^(c+1)(n) = π^c(n).
- The outer `while k-m:` loop holds the current value `m` and its period `k`.
  Each pass sets m to the last k and computes k = π(m) with the loop of
  [A001175](../A001175/) (exact Fibonacci numbers, step until F_k ≡ 0 and
  F_{k+1} ≡ 1 mod m). It stops when π(m) = m.
- `m=0` makes the first pass run with m = n. `c` counts the periods computed,
  and the last one only confirms the fixed point, so the program prints c − 1.
- `k=n=n+1` advances n and starts the chain in one statement.

**Notes**

- Exact for every n. The chain always ends: Fulton and Morris (Acta Arith. 16,
  1969) showed that iterating π reaches 1 (only from n = 1) or one of its
  other fixed points 24·5^j. The program does not use that; it stops at the
  first value with π(m) = m.
- The values in a chain can be several times n (π(m) ≤ 6m), and every period
  is found by stepping, so the time grows roughly like n² per term: about 4600
  terms in 25 s on the PC it was written on. The b-file has 10000; the bar is
  4000 terms in 60 s.
- Reducing the residues (`b%m`, 105 bytes) is about twice as fast.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001178), CC BY-SA 4.0.
