# A000486

> One half of the number of permutations of [n] such that the differences have 4 runs with the same signs.
> — [OEIS A000486](https://oeis.org/A000486)

Offset 5: 16, 150, 926, 4788, 22548, 100530, 433162, 1825296, 7577120, 31130190, …

### Python 3 — 114 bytes

```python
a=[16,150,926,4788,22548,100530]
while[print(a[0])]:a=a[1:]+[sum(x*y for x,y in zip(a,(-48,172,-244,175,-67,13)))]
```

**How it works**

Multiplying the rational generating function by its denominator
gives the order-six recurrence with coefficients
(-48,172,-244,175,-67,13) on consecutive preceding terms.
The six seeds are a(5) through a(10), obtained from the stated
generating function. Shift the window and append the recurrence
value after each output.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 996 terms in 60 s; the official b-file contains 996 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000486), CC BY-SA 4.0.
