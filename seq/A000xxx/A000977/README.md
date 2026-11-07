# A000977

> Numbers that are divisible by at least three different primes.
> — [OEIS A000977](https://oeis.org/A000977)

Offset 1: 30, 42, 60, 66, 70, 78, 84, 90, 102, 105, 110, 114, 120, 126, 130, 132, 138, 140, 150, 154, …

### Python 3 — 69 bytes

```python
P=[];n=1
while 1:n+=1;c=sum(n%p<1for p in P);c>2!=print(n);P+=[n][c:]
```

**How it works**

- `P` lists the primes below n. c counts the primes in it that divide n:
  n is printed when c > 2 (`c>2!=print(n)` calls print only then).
- c = 0 exactly when n is prime, and `[n][c:]` is `[n]` then and `[]`
  otherwise, so `P+=[n][c:]` keeps the prime list up to date.

**Notes**

- The whole b-file (10000 terms) in about 3 s; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000977), CC BY-SA 4.0.
