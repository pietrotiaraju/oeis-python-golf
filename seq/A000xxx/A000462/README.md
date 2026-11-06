# A000462

> Numbers written in base of triangular numbers.
> — [OEIS A000462](https://oeis.org/A000462)

Offset 1: 1, 2, 10, 11, 12, 100, 101, 102, 110, 1000, …

### Python 3 — 121 bytes

```python
n=1
while 1:
 r=n;s='';k=1
 while k*(k+1)//2<=n:k+=1
 while k>1:
  k-=1;d,r=divmod(r,k*(k+1)//2);s+=str(d)
 print(s);n+=1
```

**How it works**

Perform greedy division by the triangular place values k(k+1)/2
in descending order. The initial loop finds the largest place
value not exceeding n. Each divmod yields one digit and the
remainder for the lower places. Quotients never exceed 2,
so concatenating their decimal digits gives the required notation.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000462), CC BY-SA 4.0.
