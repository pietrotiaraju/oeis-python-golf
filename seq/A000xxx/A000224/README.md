# A000224

> Number of squares mod n.
> — [OEIS A000224](https://oeis.org/A000224)

Offset 1: 1, 2, 2, 2, 3, 4, 4, 3, 4, 6, 6, …

### Python 3 — 53 bytes

```python
n=1
while[print(len({k*k%n for k in range(n)}))]:n+=1
```

**How it works**

- k² mod n depends only on k mod n, so the squares mod n (0 included)
  are exactly the residues k² mod n for 0 ≤ k < n, and a(n) is the size
  of that set: `len({k*k%n for k in range(n)})`.
- `while[print(…)]:n+=1` loops forever, because the one-element list
  `[None]` is truthy. It is one byte under `while 1:print(…);n+=1`.

**Notes**

- Term n costs n set insertions. On this PC the whole b-file
  (10000 terms) prints in about 13 s and about 22700 terms fit in
  60 s. The bar is the whole b-file in 60 s.
- Same idea, longer loops: `n=0` / `while n:=n+1:print(…)` is 54 bytes.
  The growing queue `r=[1]` / `for n in r:r+=n+1,;print(len({k*k%n for k in r}))`
  is 55 (r holds 1..n+1, which covers every residue). A running list of
  squares `s+=n*n,` with `{k%n for k in s}` is 58. A walrus in the
  comprehension's iterable (`range(n:=n+1)`) is a SyntaxError.
- a(n) is multiplicative (Chinese remainder theorem). The prime-power
  formulas in the entry need a factorization and come out much longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000224), CC BY-SA 4.0.
