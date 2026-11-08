# A001013

> Jordan-Polya numbers: products of factorial numbers A000142.
> — [OEIS A001013](https://oeis.org/A001013)

Offset 1: 1, 2, 4, 6, 8, 12, 16, 24, 32, 36, 48, 64, 72, 96, 120, 128, 144, 192, …

### Python 3 — 80 bytes

```python
h={(1,2)};p=0
while 1:v,j=e=min(h);h=h-{e}|{(v*j,j+1),(2*v,3)};v>p==print(v);p=v
```

**How it works**

- Every Jordan–Pólya number y > 1 is x·k! with k ≥ 2 and x a smaller
  Jordan–Pólya number (take one factorial off). So the numbers are the
  merge of the increasing chains x·2!, x·3!, x·4!, …, one chain for each
  Jordan–Pólya number x.
- The set `h` holds one pending entry (v, j) per chain: v = x·(j−1)! is
  its next value, and multiplying by j moves to x·j!. The loop takes the
  smallest entry and puts back its successor (v·j, j+1) and the first entry
  (2v, 3) = (v·2!, 3) of the chain of v itself. The root (1, 2) is the
  chain of x = 1: 2, 6, 24, …
- Everything put back is larger than what was taken out, so the values
  come out in nondecreasing order, and by induction every x is taken out
  before its chain is needed: this is a complete, sorted enumeration.
- Different chains can meet (12 = 2·3! = 3!·2!, or 6!·7! = 10!); equal
  values come out one after the other, and `v>p==print(v);p=v` prints only
  the first. The entry (2v, 3) is the same tuple each time, so the set
  keeps a single copy.
- `min` over a set replaces heapq: no import, and `h=h-{e}|{…}` pops and
  pushes in one assignment.

**Notes**

- Exact integer arithmetic.
- `min` and the set copy cost one step per chain, about one per printed
  term: 10 500 terms in 60 s (the whole b-file of 10 000 in about 50 s).
  The bar is 8000 terms in 60 s. In-place `h-={e};h|={…}` is 82 bytes and
  manages 12 900.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001013), CC BY-SA 4.0.
