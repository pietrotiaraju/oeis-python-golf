# A000966

> n! never ends in this many 0's.
> — [OEIS A000966](https://oeis.org/A000966)

Offset 1: 5, 11, 17, 23, 29, 30, 36, 42, 48, 54, 60, 61, 67, 73, 79, 85, 91, 92, 98, 104, …

### Python 3 — 48 bytes

```python
A=[5]
for x in A:print(x);A+=x+6-5*(len(A)in A),
```

**How it works**

- The sequence generates itself: a(1) = 5, and a(n+1) − a(n) is 1 when n
  is itself a term and 6 otherwise (Paul C Abbott's comment in the OEIS
  entry). So the program keeps the terms in a list `A`, prints them one by
  one and appends the next: `x+6-5*(len(A)in A)`.
- Why it holds. Let z(m) be the number of trailing zeros of m!. It only
  moves at multiples of 5, and from 5j−5 to 5j it jumps by 1 + v₅(j), so
  the v₅(j) numbers in between are never reached. These gaps sit at
  j = 5, 10, 15, …, and inside a gap the terms are 1 apart. The last
  number skipped before z(5j) is z(5j) − 1; the next four steps jump by 1
  each, so the next gap starts at z(5j) + 5, 6 further on.
- The gaps up to j hold Σ_{i≤j} v₅(i) = z(j) terms, so the last term of
  the gap at j is term number z(j), and the others have the numbers
  strictly between z(j−5) and z(j). Since z(j−5) and z(j) are consecutive
  values of z, those are exactly the numbers z never takes: the terms. So a(n+1) − a(n) = 1 (n not last in its gap)
  exactly when n is a term.
- Appending to the list a `for` loop is walking makes the loop infinite.
  When `x` = a(i) is printed the list holds a(1), …, a(i), so `len(A)` is
  i; and since a(k) > k, if i is a term it is already in the list.

**Notes**

- Exact integer arithmetic. The `in` test scans the list, so n terms cost
  about n²/2 comparisons: the 10000-term b-file takes under a second,
  about 59000 terms in 20 s.
- The direct loop over multiples of 5 that prints the skipped values
  (`y=m=0`, `while k%5<1:k//=5;print(m+y);y+=1`) is 58 bytes.
- The bar is the whole b-file (10000 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000966), CC BY-SA 4.0.
