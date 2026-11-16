# A001866

> Number of connected graphs with n nodes and n edges.
> — [OEIS A001866](https://oeis.org/A001866)

Offset 0: 0, 0, 1, 24, 936, 56640, 4968000, 598328640, 94916183040, 19200422062080, …

### Python 3 — 77 bytes

```python
n=0;f=1
while 1:s=i=0;exec('s=(s+n**i//n)*i;i+=1;'*n);print(f*s//2);n+=1;f*=n
```

**How it works**

- **What is counted.** The data counts connected graphs on n labeled nodes
  with n labeled edges, where two edges may join the same pair of nodes:
  in the words of the OEIS comment, n × n 0-1 matrices with two 1s per row
  (an edge per row) and permanent 2. For n = 3 that is the 6 labelings of
  the triangle plus 18 double-edge graphs, 24. A search over all sequences
  of n node pairs gives 0, 1, 24, 936, 56640 for n = 1 to 5, as in the data.
- **The formula.** n nodes and n edges, connected: a spanning tree plus one
  edge, so exactly one cycle, of some length k ≥ 2 (k = 2 is a double
  edge). For k ≥ 3 there are n!/((n − k)!·2k) such cycles, the other nodes
  hang on them as a rooted forest in k·nⁿ⁻ᵏ⁻¹ ways, and the edges take
  their labels in n! ways. For k = 2 there are twice as many cycles as that
  count says (C(n, 2) pairs) but half as many labelings. Both cases give
  n!²·nⁿ⁻ᵏ⁻¹/(2(n − k)!), Vladimir Shevelev's formula on the OEIS page;
  with j = n − k,
  a(n) = (n!/2)·Σⱼ₌₀..ₙ₋₂ (n − 1)!/j!·nʲ.
- **The program.** sᵢ = i·(sᵢ₋₁ + nⁱ⁻¹) from s₀ = 0 gives
  sₘ = Σⱼ₌₀..ₘ₋₁ m!/j!·nʲ, so the sum is sₙ₋₁. `exec` repeats
  `s=(s+n**i//n)*i;i+=1;` n times for i = 0, …, n − 1: the pass i = 0
  multiplies by 0, so whatever `n**i//n` is there does not matter, and
  for i ≥ 1 it is the exact nⁱ⁻¹ (n**i alone with `*-~i`, run n − 1
  times, is 1 byte longer). `f` keeps n!, and `f*s//2` is exact because
  the count is an integer. [A001865](../A001865/), the connected
  functions, is the same sum up to j = n − 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 801.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001866), CC BY-SA 4.0.
