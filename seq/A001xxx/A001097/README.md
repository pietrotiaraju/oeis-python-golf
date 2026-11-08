# A001097

> Twin primes.
> — [OEIS A001097](https://oeis.org/A001097)

Offset 1: 3, 5, 7, 11, 13, 17, 19, 29, 31, 41, 43, 59, 61, 71, 73, 101, 103, 107, 109, 137, …

### Python 3 — 61 bytes

```python
s=0;P=k=1
while 1:s+=s+P%k;s&4>0<s&17!=print(k-2);P*=k*k;k+=1
```

**How it works**

- Wilson's theorem in its squared form: with P = ((k − 1)!)², P mod k is
  1 when k is prime and 0 otherwise, and `P*=k*k;k+=1` keeps it up to
  date.
- s is a shift register of those bits (`s+=s+P%k`), bit i standing for
  k − i. A prime k − 2 is a twin prime when k or k − 4 is prime too, that
  is when bit 2 is set together with bit 0 or bit 4.
- `s&4>0<s&17!=print(k-2)` is the chain (s&4) > 0 < (s&17) ≠ None: print
  runs only when the first two comparisons hold, and its `None` is
  always ≠ an int. 3 and 5 are printed (each pairs with the other), 2 is
  not (0 and 4 are not prime), and each twin prime is printed once, in
  order.

**Notes**

- Exact integer arithmetic; the only theorem used is Wilson's.
- P has about 2k log₂ k bits, so the cost grows like k² in all. About 2300
  terms print in 60 s; the b-file has 10 000 and the bar is 1700.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001097), CC BY-SA 4.0.
