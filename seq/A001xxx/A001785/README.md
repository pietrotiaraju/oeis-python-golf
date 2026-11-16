# A001785

> Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+4, n]]. The number of n-orbit permutations of a (2n+4)-set with at least 2 elements in each orbit. Also known as associated Stirling numbers of the first kind (e.g., Comtet).
> — [OEIS A001785](https://oeis.org/A001785)

Offset 0: 1, 120, 7308, 303660, 11098780, 389449060, 13642629000, 486591585480, 17856935296200, 678103775949600, …

### Python 3 — 76 bytes

```python
E=[s:=1,i:=0,0,0,0]
while[print(s)]:s=0;E=[s:=(i:=i+1)*(s+e)for e in E];i-=3
```

**How it works**

- [[m, k]] counts permutations of m points with k cycles, all of length
  ≥ 2. Take the largest point: either its cycle stays of length ≥ 2 when it
  is removed (it sat after one of the other m − 1 points) or it was in a
  transposition with one of them, so
  [[m, k]] = (m−1)·([[m−1, k]] + [[m−2, k−1]]).
- Let e_k(n) = [[2n+k, n]] for k = 0, …, 4; a(n) = e₄(n). The recurrence
  reads e_k(n) = (2n+k−1)·(e_{k−1}(n) + e_k(n−1)), with e₋₁(n) =
  [[2n−1, n]] = 0 for n ≥ 1, and row 0 is [1, 0, 0, 0, 0] ([[0, 0]] = 1).
- `E` holds row n − 1. One pass resets `s=0` (that is e₋₁) and runs
  `s:=(i:=i+1)*(s+e)` along the row, with multipliers 2n − 1, …, 2n + 3:
  each new entry uses the one just made and the old entry below it. The last
  one is a(n); `i-=3` moves the start from 2n + 3 back to 2n for the next
  row. `E=[s:=1,i:=0,0,0,0]` builds row 0 and sets `s` and `i` at once.
- For n = 0 the definition gives [[4, 0]] = 0, but the entry lists a(0) = 1
  (all its programs special-case it). The program follows the data: the
  first print is the starting `s=1`; every later one comes from a pass.

**Notes**

- Exact integer arithmetic, correct for every n. a(1417) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- The closed form by cycle types (as in [A001784](../A001784/)): with
  j = 2n + 3 and d = j!!, a(n) = d(j−3)(j²−1)(20j³ + 120j² + 187j + 45)/38880,
  and `d=j=3` / `while[print(d*(j-3)*(j*j-1)*(((20*j+120)*j+187)*j+45)//38880or 1)]:j+=2;d*=j`
  is 82 bytes; it agrees with Kotesovec's formula in the entry.
- The b-file has 15 terms (a(0) to a(14)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001785), CC BY-SA 4.0.
