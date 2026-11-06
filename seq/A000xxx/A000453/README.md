# A000453

> Stirling numbers of the second kind, S(n,4).
> — [OEIS A000453](https://oeis.org/A000453)

Offset 4: 1, 10, 65, 350, 1701, 7770, 34105, 145750, 611501, 2532530, …

### Python 3 — 50 bytes

```python
n=4
while 1:print((4**n-4*3**n+6*2**n-4)//24);n+=1
```

**How it works**

Inclusion-exclusion counts onto maps from an n-set to four labeled
boxes: 4^n - 4*3^n + 6*2^n - 4. Divide by 4! to forget box labels,
giving the Stirling number S(n,4). Start at n=4.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 197 terms in 60 s; the official b-file contains 197 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000453), CC BY-SA 4.0.
