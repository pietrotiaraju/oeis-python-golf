# A000560

> Number of symmetric ways of folding a strip of n labeled stamps.
> — [OEIS A000560](https://oeis.org/A000560)

Offset 2: 1, 2, 5, 12, 33, 87, 252, 703, 2105, 6099, …

### Python 3 — 172 bytes

```python
L=[[0]],
n=1
while 1:
 if n>2:print(len(L)//(2*n))
 L=[(x+[-len(q)],*q)for q in L for x in([],*q)if all((x<c)^(x<d)==(q[0]<c)^(q[0]<d)for c,d in zip(q[1::2],q[2::2]))];n+=1
```

**How it works**

- OEIS gives a(n)=A000136(n+1)/(2n+2). Generate the foldings of an
  m-stamp strip and divide their count by 2m, starting at m=3.
- A folding is represented by stamp heights, newest stamp first.
  On either edge of the pile, two creases must not interleave. Inserting
  the next stamp creates one crease, so only the old creases on that
  edge need to be checked: the pairs in `zip(q[1::2],q[2::2])`.
- Lexicographically ordered list heights encode insertion gaps without
  renumbering. The choices `[]` and each old height give all m+1 gaps;
  appending the new negative depth puts the new height just above that
  choice. The XOR equality is exactly the noninterleaving condition.
- This is the folding generator used for A000136, with the OEIS relation
  applied at the required offset. The first count is 6/(2·3)=1.

**Notes**

- The divisor relation is stated in [OEIS A000560](https://oeis.org/A000560).
  Each folding is generated once by removing or reinserting its last stamp.
- The complete folding list grows rapidly and can eventually exhaust
  memory; the verification bar is the first eight requested counts.
- The reference file contains 43 published OEIS terms; the verification
  bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000560), CC BY-SA 4.0.
