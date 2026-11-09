# A001212

> a(n) = solution to the postage stamp problem with n denominations and 2 stamps.
> — [OEIS A001212](https://oeis.org/A001212)

Offset 1: 2, 4, 8, 12, 16, 20, 26, 32, 40, 46, 54, 64, 72, 80, 92, 104, …

a(n) is the h-range n(h,k) for k = n stamp values and h = 2 stamps: the
largest N such that some set of stamps 1 = a₁ < a₂ < … < aₙ pays every
amount 1, 2, …, N with at most h stamps. (Lunnon's "solution" is the first
amount that cannot be paid, one more; the OEIS data are the h-range, as
its comment says.)

### Python 3 — 148 bytes

```python
f=lambda L,p,k,y:k and max(f([q:=s|q<<a for s in L],a,k-1,len(bin(q^q+1)))for a in range(p,y-2)if[q:=0])or y-4
n=1
while[print(f([1]*3,0,n,4))]:n+=1
```

**How it works**

- Exhaustive search over the stamp sets. `f(L,p,k,y)` adds k more stamps,
  none smaller than the last one, p. `L[j]` is the bitmask of the amounts
  payable with at most j stamps of the set (bit m set when m is payable),
  j = 0…h, and y is the set's range + 4.
- A new stamp a gives L′[j] = L[j] | L′[j−1] << a (use no a, or one a
  plus at most j−1 stamps), built in one pass by the walrus `q`;
  `if[q:=0]` resets it for each a, so L′[0] = L[0] = 1.
- The range is the lowest 0 bit of L[h] minus 1. After the pass `q` is
  L′[h], and `q^q+1` is 2^(range+2) − 1, so `len(bin(q^q+1))` is the new
  y, passed down with the list; a leaf (k = 0) returns y − 4.
- Only stamps up to range + 1 are tried (`range(p,y-2)`), which loses
  nothing: if, in a set sorted upwards, a stamp is larger than the range
  of the smaller ones plus 1, that amount can never be paid (every stamp
  from there on is too big), so the whole set has the range of the
  smaller stamps; putting range + 1, range + 2, … in place of the larger
  stamps obeys the bound and is no worse. So some optimal set is reached.
- The search starts from the empty set (L = [1]·3, p = 0, y = 4 for range
  0), so the first stamp is 0 or 1. A repeat (a = p, 0 included) is
  allowed: it only gives a set with fewer stamps, whose range is still at
  most n(2,n). So the maximum found is exactly a(n), for every n.

**Notes**

- Exact integer search with no stored terms. No formula is known for a
  growing number of stamp values; the OEIS terms come from long computer
  searches (Challis and others).
- Terms up to a(10) take about 4 s here and a(11) about 27 s more (about
  11 reference seconds); each term costs roughly seven times the one
  before. The b-file has 24 terms. The bar is 11 terms in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 148 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001212), CC BY-SA 4.0.
