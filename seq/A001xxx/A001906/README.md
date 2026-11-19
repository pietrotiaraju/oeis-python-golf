# A001906

> F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2).
> — [OEIS A001906](https://oeis.org/A001906)

Offset 0: 0, 1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811, …

### Python 3 — 32 bytes

```python
a=b=-1
while[print(a:=a-b)]:b-=a
```

**How it works**

- a(n) = F(2n). Before term n is computed, `a` = F(2n − 2) and
  `b` = −F(2n − 1). Then `a:=a-b` makes a = F(2n − 2) + F(2n − 1) = F(2n),
  which is printed, and `b-=a` makes b = −F(2n − 1) − F(2n) = −F(2n + 1):
  two Fibonacci steps per term, with the odd-indexed numbers kept negated.
- The start is n = 0: F(−2) = −1 and −F(−1) = −1, so `a=b=-1`.
- Two steps of F(k + 1) = F(k) + F(k − 1) give F(m + 2) = 3F(m) − F(m − 2),
  the recurrence in the name.

**Notes**

- The sister program [A001519](../A001519/) (F(2n − 1), 31 bytes) prints
  F(2n) as `a-b` in 33 bytes; `a=0;b=1` / `a+=b;b+=a` is 33 too. The walrus
  in the print removes the separate print variable.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 10290.
- The b-file has 2389 terms (n = 0 to 2388); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001906), CC BY-SA 4.0.
