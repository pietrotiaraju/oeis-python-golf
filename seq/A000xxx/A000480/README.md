# A000480

> a(n) = floor(cos(n)).
> — [OEIS A000480](https://oeis.org/A000480)

Offset 0: 1, 0, -1, -1, -1, 0, 0, 0, -1, -1, …

### Python 3 — 225 bytes

```python
n=S=1
print(1)
while 1:
 S*=2;K=S.bit_length();E=20*K+20
 p=sum((-1)**k*S*16//((2*k+1)*5**(2*k+1))-(-1)**k*S*4//((2*k+1)*239**(2*k+1))for k in range(K))
 while p>E and(q:=2*n*S//(p+E))==2*n*S//(p-E):print(-(q%4 in(1,2)));n+=1
```

**How it works**

- All angles are in **radians**. The program determines the sector
  containing n using certified bounds on π, then reads off floor(cos(n)).
  It never evaluates a floating-point sine or cosine.
- [Machin's identity](https://mathworld.wolfram.com/Machin-LikeFormulas.html)
  is π=16atan(1/5)−4atan(1/239). With
  atan(1/b)=Σₖ≥₀ (−1)ᵏ/((2k+1)b^(2k+1)), take K terms
  at the integer scale S. The comprehension rounds each of
  the two scaled contributions down before subtracting them.
- Those divisions contribute less than 2K total error. Since
  K=S.bit_length() and S≥2, the two scaled alternating-series
  tails together are less than 1. The generous error allowance
  E=20K+20 therefore proves **p−E<Sπ<p+E**.
- Once `p>E`, both denominators are positive. The two quotients
  ⌊2nS/(p+E)⌋ and ⌊2nS/(p−E)⌋ bracket
  q=⌊2n/π⌋. Print only if they agree, using the first
  quotient stored by the walrus in q.
- If they disagree, double S and recompute tighter bounds.
  Otherwise advance n and reuse the current bounds for as many
  consecutive inputs as they certify. For n>0, 2n/π is
  not an integer, so increasing precision eventually resolves it.
- For positive integer n, cos(n) is strictly between −1 and 1
  and never zero. Its floor is therefore −1 precisely in the
  two negative-cosine quadrants. With q=⌊2n/π⌋, their
  residues are 1 and 2 modulo 4, giving `-(q%4 in(1,2))`.
- The exceptional cos(0)=1 is printed before the loop; all
  later outputs are 0 or −1. This is why n begins at 1.

The sector-to-output mapping is:

| q mod 4 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| floor(cos(n)) | 0 | −1 | −1 | 0 |

**Notes**

- Exact integer arithmetic and a rigorous error interval at every
  precision. Irrationality of π rules out the positive-index
  sector boundaries; the separate handling of n=0 is described above.
- The output uses only −1, 0 and 1, so its conversion never
  reaches Python's 4300-digit integer limit. Time and temporary
  integer sizes grow when a closer approach to a sector boundary
  requires a more accurate π interval.
- [A000484](../A000484/) uses the same π bounds with
  a different sector scale or rounding rule. The lookup is part
  of the mathematical rounding test, not a table of sequence terms.
- The b-file has 80 terms (indices 0 through 79). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 225 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000480), CC BY-SA 4.0.
