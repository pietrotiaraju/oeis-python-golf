# A001087

> Related to S(n), the number of self-dual monotone Boolean functions of n variables (A001206): 2^n-th term is S(n).
> — [OEIS A001087](https://oeis.org/A001087)

Offset 1: 1, 2, 3, 4, 5, 7, 11, 12, 13, 18, 26, 31, 49, 62, 80, 81, 82, 101, 126, 167, …

The OEIS entry gives no definition ("This sequence needs a definition!"),
only the 32 terms and the name. The program uses this one, which gives all
32 terms:

- number every finite set of naturals by its binary code, Σ 2ⁱ over its
  elements, so the codes below 2ⁿ are the subsets of {0, …, n−1};
- a(m) is the number of intersecting families of the sets with codes
  1 … m−1 that are closed upwards inside that range (if A is in the
  family, B ⊇ A and the code of B is below m, then B is in the family).

For m = 2ⁿ these are the intersecting up-sets of the subsets of an n-set,
which match the self-dual monotone Boolean functions of n + 1 variables
(f is fixed by f(x, 0), the indicator of such a family, and
f(x, 1) = ¬f(¬x, 0)). So a(2ⁿ) = [A001206](https://oeis.org/A001206)(n + 1):
1, 2, 4, 12, 81, 2646 at m = 1, 2, 4, 8, 16, 32; the name's "2^n-th term is
S(n)" is off by one in n.

### Python 3 — 96 bytes

```python
f=lambda a=0,*s:a<1or f(*s)+f(*[b for b in s if 0<b&a<a])
m=1
while[print(+f(*range(1,m)))]:m+=1
```

**How it works**

- An up-set is fixed by its minimal sets, and it is intersecting exactly
  when they meet pairwise (any two members contain two minimal sets). So
  a(m) counts the families of codes in 1 … m−1 that pairwise meet and
  where none contains another; the empty family counts too.
- `f(a,*s)` counts them among the codes `a,*s`, given in increasing order:
  without `a` that is `f(*s)`; with `a`, the other sets are codes `b` that
  meet `a` without containing it, `0<b&a<a`. A later code is larger, so
  it is never inside `a`, and the filtered list stays increasing.
- With nothing left, `a` takes its default 0 and `a<1` returns `True`; the
  sums turn it into ints, and `+` does so for m = 1, where nothing else is
  added.

**Notes**

- The definition is a reconstruction from the data: it matches all 32
  terms in the entry and the property in the name, but it is not stated in
  the OEIS. The b-file holds those 32 terms, and the bar is all 32 in 60 s.
- One call per counted family: the program prints the 32 terms at once and
  about 78 in 60 s (a(78) = 12143881), in a few MB.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001087), CC BY-SA 4.0.
