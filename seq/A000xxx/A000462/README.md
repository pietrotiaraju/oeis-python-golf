# A000462

> Numbers written in base of triangular numbers.
> — [OEIS A000462](https://oeis.org/A000462)

Offset 1: 1, 2, 10, 11, 12, 100, 101, 102, 110, 1000, …

### Python 3 — 115 bytes

```python
n=1
while 1:
 r=n;s='';t=k=1
 while t<=n:k+=1;t+=k
 while k>1:
  t-=k;k-=1;d,r=divmod(r,t);s+=str(d)
 print(s);n+=1
```

**How it works**

- The place values are T_k=k(k+1)/2, the positive triangular
  numbers 1,3,6,10,… . The notation uses greedy quotients in
  these places, rather than powers of a fixed base.
- The first loop keeps t=T_k and advances it by T_(k+1)−T_k=k+1
  until t>n. The second subtracts k from t before decrementing k,
  keeping t=T_k for the next lower place. Each `divmod` extracts
  that place digit and leaves the remaining value.
- Before a place T_k, the remainder is less than T_(k+1).
  Since T_(k+1)−1<3T_k for k≥1, each digit is at most 2.
  Concatenating the quotient strings therefore produces single
  digits with no need for separators.
- For n=9, the places 6,3,1 give digits 1,1,0, hence 110.
  For n=10, the extra leading place produces 1000. Keeping the
  zero digits records which lower places have been skipped.
- The counter begins at 1, matching the OEIS offset. The largest
  chosen place has a nonzero digit, so no leading zero is printed.

**Notes**

- Exact integer arithmetic. Consecutive differences generate the
  triangular values without recomputing k(k+1)/2. Greedy division specifies a unique output even when other
  unrestricted sums of triangular places could represent the same n.
- The two loops each visit O(√n) place indices per term. The number
  is encoded as text rather than parsed as a new decimal integer,
  keeping the entire place sequence intact.
- [A000433](../A000433/) uses the same construction for cube
  places, where digits can reach 7 and zero needs an explicit case.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 121 | first entry |
| 2026-11-06 | Python 3 | 115 | advance triangular place values by consecutive differences |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000462), CC BY-SA 4.0.
