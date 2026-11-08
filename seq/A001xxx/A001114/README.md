# A001114

> Increasing blocks of digits of e.
> — [OEIS A001114](https://oeis.org/A001114)

Offset 1: 2, 7, 18, 28, 182, 845, 904, 5235, 36028, 74713, 526624, …

### Python 3 — 117 bytes

```python
N=2;F=Q=m=1;b=p=0
while-N%F<=Q or[c:=N//F,N:=N%F*10,Q:=Q*10,c*(b>p)and[print(p:=b),b:=0],b:=b*10+c]:m+=1;N=N*m+Q;F*=m
```

**How it works**

- The digits of e come from the spigot of [A001113](../A001113/): the first
  three items of the list in the `while` condition and the body are that
  program, with the digit kept in `c`.
- The rule, as in the OEIS Python program and checked on all 1000 terms of
  the b-file: the next block is the shortest run of following digits whose
  value is larger than the previous block, extended over any zeros that
  follow it, so that no block starts with 0.
- The program keeps the current block `b` and the previous one `p` as
  integers. A digit `c` closes `b` exactly when c ≠ 0 and b > p
  (`c*(b>p)`): then `b` is printed, becomes `p`, and the new block starts
  from 0; in every case `b:=b*10+c` appends the digit. Since no block starts
  with 0, b > p as numbers means "more digits than p, or as many and larger",
  which is the OEIS program's test (take len(p) digits if they beat p, else
  len(p) + 1), and waiting for a nonzero digit is its extension over zeros.
- `b = p = 0` at the start: the first digit 2 does not close the empty block
  (0 > 0 is false), so the first block is 2.

**Notes**

- The blocks keep growing: the 1000 terms of the b-file use 291507 digits
  of e, and each digit costs work proportional to the size of N and F. The
  program prints about 580 terms in 60 s here; the bar is 430 terms in 60 s
  (about 19 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001114), CC BY-SA 4.0.
