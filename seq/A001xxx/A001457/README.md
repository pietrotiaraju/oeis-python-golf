# A001457

> Number of permutations of length n with longest increasing subsequence of length 6.
> — [OEIS A001457](https://oeis.org/A001457)

Offset 6: 1, 36, 841, 16465, 296326, 5122877, 87116283, 1477363967, …

### Python 3 — 131 bytes

```python
D={63:1}
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
  λ₁ = 6, where f_λ counts the standard tableaux of shape λ. Transposing
  a tableau gives f_λ = f_λ′, so the sum may run over the λ with exactly
  6 parts instead.
- The cell holding n in a standard tableau is a corner, so f_λ is the sum
  of f_μ over the shapes μ that lose one corner of λ, with f_∅ = 1. The
  program builds f_λ for all λ ⊢ n with at most 6 parts, one n at a time.
  Nothing else goes in, no formula and no recurrence, so it is right for
  every n.

**How it works**

- A shape λ₁ ≥ … ≥ λ_6 ≥ 0 is the bitmask `l` of its β-set
  {λᵢ + 6 − i}, 6 distinct numbers. A cell can be added to row i when
  λᵢ + 6 − i + 1 is not in the set, and adding it raises that number by 1:
  in the mask, a set bit with a clear bit above it, which `l+b` moves up.
  `c=l&~l>>1` holds all those bits and `b=c&-c` is the lowest.
- The empty shape is {0, …, 5}, the mask 2^6 − 1 = 63. A shape has
  exactly 6 parts when λ_6 ≥ 1, that is when 0 is not in the set: `l` is
  even, `~l%2`.
- `D` maps the masks of the current n to f. `for l in[*D]` walks a copy of
  its keys, `D.pop(l)` takes f out, and the new masks go into the same dict:
  their β-sum is one larger, so they never meet a mask still waiting.
- `while[s:=0]:` resets s for each n (a list holding 0 is true), and s
  collects f² over the even masks. a(n) is 0 for n < 6 and positive from
  n = 6 on, so `s and print(s)` starts the output at the offset.

**Notes**

- There are about n^5/(6!·5!) shapes with at most 6 parts, and
  each costs 6 or fewer big-int additions, so the terms slow down
  steadily: about 112 terms in 60 s here.
- The same program with `D={7:1}`, `{15:1}`, `{31:1}`, `{63:1}` and
  `{127:1}` gives k = 3 to 7:
  [A001454](../A001454/), [A001455](../A001455/), [A001456](../A001456/), [A001458](../A001458/);
  for k = 3 a recurrence from Gessel's formula is shorter.
- The b-file has 170 terms (n = 6 to 175); the bar is the first
  88 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001457), CC BY-SA 4.0.
