# A001694

> Powerful numbers, definition (1): if a prime p divides n then p^2 must also divide n (also called squareful, square full, square-full or 2-powerful numbers).
> — [OEIS A001694](https://oeis.org/A001694)

Offset 1: 1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100, 108, 121, 125, …

### Python 3 — 102 bytes

```python
m=2
while[x<m*m<=4*x==print(x)for x in sorted({a*a*b**3for b in range(1,m)for a in range(m//b)})]:m*=2
```

**How it works**

- **Powerful numbers are a²b³.** If every prime of x divides it at least
  twice, write each exponent e ≥ 2 as 2i + 3j (j = 0 or 1) and collect
  x = a²b³; conversely a²b³ is powerful. The representation is not unique
  (64 = 8²·1³ = 1²·4³), so the values go into a set.
- **Blocks.** m runs over 2, 4, 8, …, and pass m prints the powerful x with
  m²/4 ≤ x < m², in increasing order: `sorted` orders the set and the
  chained comparison `x<m*m<=4*x==print(x)` calls print only inside the
  block (print returns None, so the last link is just false). The blocks
  tile [1, ∞), so every term comes once and in order.
- **The ranges are enough.** Let x = a²b³ < m² with a, b ≥ 1. Then
  b³ < m², so b < m; and a < m//b, i.e. (a+1)·b ≤ m. For b = 1 that is
  a < m. Otherwise a·b^(3/2) < m, and (a+1)·b ≤ a·b^(3/2) as soon as
  √b ≥ 1 + 1/a, which holds for all b ≥ 4, and for b = 2, 3 when a ≥ 3.
  The four pairs left, (a, b) = (1, 2), (2, 2), (1, 3), (2, 3), give
  x = 8, 32, 27, 108, which first fall below m² at m = 4, 8, 8, 16, where
  (a+1)·b = 4, 6, 6, 9 ≤ m. The set may also hold a = 0 (x = 0) and values
  of m² or more; the comparison drops them.
- Each block has a term, (m/2)², so the list of `None`s is never empty, the
  header is true and the body doubles m.

**Notes**

- Exact integers, so the program is right for every n. Pass m forms about
  m·ln m products; the 10000 terms of the b-file (up to 23002083) need
  m = 8192 and print in under a second. The bar is the whole b-file in
  60 s.
- `range(m//b+1)` would cover the pairs with no case check; the shorter
  `range(m//b)` needs the four small cases above. Testing each number by
  trial division is much slower: it spends time growing with n on every n,
  while the blocks spend about log m per term.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001694), CC BY-SA 4.0.
