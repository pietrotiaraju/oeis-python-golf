# A000405

> Number of 6-level labeled rooted trees with n leaves.
> — [OEIS A000405](https://oeis.org/A000405)

Offset 0: 1, 1, 6, 51, 561, 7556, 120196, 2201856, 45592666, 1051951026, …

### Python 3 — 85 bytes

```python
t=1;Q=[[]]*5
while[print(t)]:t=1;Q=[[t]+[t:=t+len(L)*L.pop(0)for x in L*1]for L in Q]
```

**How it works**

- Start with B₀(x)=exp(x) and put B_(j+1)(x)=B_j(exp(x)−1).
  Substituting exp(x)−1 takes the second-kind Stirling transform:
  if B_j has coefficients b_j(n), then
  b_(j+1)(n)=Σₖ S(n,k)·b_j(k). Five transforms give the six
  nested exponentials in the OEIS generating function.
- One transform can be advanced without storing Stirling numbers.
  For its input c, define T(0,k)=c(k) and
  T(i+1,k)=k·T(i,k)+T(i,k+1). Expanding this recurrence gives
  T(n,0)=Σⱼ S(n,j)·c(j), the desired Stirling transform.
- Each list L holds an antidiagonal, ordered from T(0,n) through
  T(n,0). The next starts with the new input `t`. Its remaining entries
  use the preceding new entry plus the old entry times the descending
  column weight. `len(L)*L.pop(0)` supplies that weight and entry:
  `len(L)` is evaluated before the pop.
- `L*1` is a copy used solely to fix the number of iterations while
  the original L is consumed. The final value of t from one level
  supplies the new input to the next; five lists chain the transforms.
- The innermost exp(x) has every coefficient 1, so the body resets
  `t=1` each round. Printing before the update supplies a(0)=1.

**Notes**

- This is [A000307](../A000307/) with five transform lists instead
  of three. See also [A000406](../A000406/) for the analogous
  first-kind transform, whose triangle has a different weight.
- `Q=[[]]*5` initially shares one empty list. The first pass pops no
  entries and creates five separate `[1]` lists, so later mutations
  do not interfere with each other.
- Exact integer arithmetic; only five antidiagonals are kept. Their
  lengths grow by one per term. The front pops also move list entries,
  so their cost is additional to the integer arithmetic.
- Python 3.11+ eventually reaches its default 4300-digit output
  conversion limit; this interpreter limit is not a correctness failure.
- The b-file has 151 terms (indices 0 through 150). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000405), CC BY-SA 4.0.
