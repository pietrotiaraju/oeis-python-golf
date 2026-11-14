# A001690

> Non-Fibonacci numbers.
> — [OEIS A001690](https://oeis.org/A001690)

Offset 1: 4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, …

### Python 3 — 54 bytes

```python
a,b=3,5
while[print(k)for k in range(a+1,b)]:a,b=b,a+b
```

**How it works**

- **The gaps between Fibonacci numbers.** The Fibonacci numbers 0, 1, 1, 2,
  3, 5, 8, … cover 0 to 3, and above that a number is not Fibonacci
  exactly when it lies strictly between two consecutive Fibonacci numbers
  a < b. So the sequence is the gap (3, 5), then (5, 8), (8, 13), …, each
  in increasing order.
- Each pass prints the integers of range(a+1, b) and steps the pair
  a, b → b, a+b. The list of `None`s is never empty (b − a − 1 is the
  Fibonacci number before a, minus 1, which is at least 1 from a = 3 on), so
  the header is true and the loop goes on.

**Notes**

- Exact integers, so the program is right for every n. The 1000 terms of
  the b-file print at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001690), CC BY-SA 4.0.
