# A000423

> a(n) is smallest number > a(n-1) of form a(i)*a(j), i < j < n.
> — [OEIS A000423](https://oeis.org/A000423)

Offset 1: 2, 3, 6, 12, 18, 24, 36, 48, 54, 72, …

### Python 3 — 79 bytes

```python
a=[];s={2,3}
while s:
 n=min(s);s.remove(n);print(n);s|={n*x for x in a};a+=[n]
```

**How it works**

The set s contains all not-yet-output products of two distinct
previous sequence positions, together with the initial seeds 2 and 3.
Choose the smallest candidate, remove it, and add its products with
every earlier term before appending it to a. All factors are at least
2, so newly added candidates exceed the term just printed. Sets merge
duplicate products, implementing the defining greedy rule exactly.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 49 terms in 60 s; the official b-file contains 49 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000423), CC BY-SA 4.0.
