# A001455

> Number of permutations of length n with longest increasing subsequence of length 4.
> — [OEIS A001455](https://oeis.org/A001455)

Offset 4: 1, 16, 181, 1821, 17557, 167449, 1604098, 15555398, 153315999, …

### Python 3 — 131 bytes

```python
D={15:1}
while[s:=0]:
 for l in[*D]:
  f=D.pop(l);s+=~l%2*f*f;c=l&~l>>1
  while c:b=c&-c;D[l+b]=D.get(l+b,0)+f;c-=b
 s and print(s)
```

**Why it works**

- By the Robinson–Schensted correspondence, the permutations of n are in
  bijection with the pairs (P, Q) of standard Young tableaux of one shape
  λ ⊢ n, and by Schensted's theorem (1961) the longest increasing
  subsequence has length λ₁. So a(n) = Σ f_λ² over the λ ⊢ n with
  λ₁ = 4, where f_λ counts the standard tableaux of shape λ. Transposing
  a tableau gives f_λ = f_λ′, so the sum may run over the λ with exactly
  4 parts instead.
- The cell holding n in a standard tableau is a corner, so f_λ is the sum
  of f_μ over the shapes μ that lose one corner of λ, with f_∅ = 1. The
  program builds f_λ for all λ ⊢ n with at most 4 parts, one n at a time.
  Nothing else goes in, no formula and no recurrence, so it is right for
  every n.

**How it works**

- A shape λ₁ ≥ … ≥ λ_4 ≥ 0 is the bitmask `l` of its β-set
  {λᵢ + 4 − i}, 4 distinct numbers. A cell can be added to row i when
  λᵢ + 4 − i + 1 is not in the set, and adding it raises that number by 1:
  in the mask, a set bit with a clear bit above it, which `l+b` moves up.
  `c=l&~l>>1` holds all those bits and `b=c&-c` is the lowest.
- The empty shape is {0, …, 3}, the mask 2^4 − 1 = 15. A shape has
  exactly 4 parts when λ_4 ≥ 1, that is when 0 is not in the set: `l` is
  even, `~l%2`.
- `D` maps the masks of the current n to f. `for l in[*D]` walks a copy of
  its keys, `D.pop(l)` takes f out, and the new masks go into the same dict:
  their β-sum is one larger, so they never meet a mask still waiting.
- `while[s:=0]:` resets s for each n (a list holding 0 is true), and s
  collects f² over the even masks. a(n) is 0 for n < 4 and positive from
  n = 4 on, so `s and print(s)` starts the output at the offset.

**Notes**

- There are about n^3/(4!·3!) shapes with at most 4 parts, and
  each costs 4 or fewer big-int additions, so the terms slow down
  steadily: about 244 terms in 60 s here.
- The recurrence in the entry (Kotesovec, 2014) comes with no proof, so
  it is not used.
- The same program with `D={7:1}`, `{15:1}`, `{31:1}`, `{63:1}` and
  `{127:1}` gives k = 3 to 7:
  [A001454](../A001454/), [A001456](../A001456/), [A001457](../A001457/), [A001458](../A001458/);
  for k = 3 a recurrence from Gessel's formula is shorter.
- The b-file has 297 terms (n = 4 to 300); the bar is the first
  190 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001455), CC BY-SA 4.0.
