# A000232

> Construct a triangle as in A036262. Sequence is one less than the position of the first number larger than 2 in the n-th row (n-th difference).
> — [OEIS A000232](https://oeis.org/A000232)

Offset 1: 3, 8, 14, 14, 25, 24, 23, 22, 25, 59, 98, 97, 98, 97, 174, 176, …

### Python 3 — 110 bytes

```python
P=k=d=1;L=[]
while 1:
 P*=k*k;k+=1
 if P%k:L=[s:=-k]+[s:=abs(s-x)for x in L];d-=1
 while L[d]>2:print(~d);d+=1
```

**How it works**

- The triangle is Gilbreath's: row 0 is the primes, row j + 1 is the
  absolute differences of row j, and a(n) is the 0-based column of the
  first entry > 2 in row n.
- Primes come from Wilson's theorem: P = ((k − 1)!)², so `P%k` is 1 when
  k is prime and 0 otherwise.
- L is the newest antidiagonal: L[j] = T(j, m − j) after the primes
  p₀, …, p_m. A new prime p gives the next antidiagonal in one pass,
  T(0, m+1) = p and T(j, m+1−j) = |T(j−1, m+2−j) − T(j−1, m+1−j)|, which is
  the running `s:=abs(s-x)` over the old L. Every entry is exact as soon
  as it exists, so no prime bound has to be guessed.
- Rows finish in order. If row n has its first entry > 2 at column a(n),
  its earlier entries are all in {0, 1, 2}, so the first a(n) − 1 entries of
  row n + 1 are too: a(n+1) ≥ a(n) − 1, i.e. row n + 1 cannot finish on an
  earlier antidiagonal than row n. So it is enough to watch one row, the
  first one not yet printed, and when it finishes, check the next row on
  the same antidiagonal (`while`, since several rows can finish together:
  a(5..8) = 25, 24, 23, 22 all end on antidiagonal m = 30).
- d is that row's index counted from the end of L (row n = `L[d]` with
  d = n − len(L)): it drops by one with each new antidiagonal and rises by
  one with each printed row, and the column is m − n = −d − 1 = `~d`.
- Row 0 is stored negated (`-k`): the differences don't change, and if
  some row n ever had a(n) = 0 (an entry > 2 in column 0, which Gilbreath's
  conjecture says never happens), d would reach 0 while row n + 1 does not
  exist yet, and `L[0]` = −p can't be mistaken for a finished row. So the
  program does not assume the conjecture.

**Notes**

- Correctness needs no conjecture for any term that exists; a term
  exists when row n has some entry > 2 (the OEIS definition takes that
  for granted, and the program would wait forever on a row that never
  has one).
- Wilson's product is the bottleneck: P has about 1.7 million bits by
  the 64th term, and the b-file's last terms are near 10⁸, far out of
  reach. The program prints 64 terms in 60 s here, so the bar is 50.
- Keeping the row index n and printing `len(L)+~n` is 114 bytes once it
  is made safe for short rows (`while[3]<=L[n:]`).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 110 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000232), CC BY-SA 4.0.
