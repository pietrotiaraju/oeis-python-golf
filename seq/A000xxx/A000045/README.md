# A000045

> Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
> — [OEIS A000045](https://oeis.org/A000045)

Offset 0: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, …

### Python 3 — 33 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,a+b
```

**How it works**

- `a` and `b` hold two consecutive terms, F(n) and F(n+1), starting from
  F(0) = 0 and F(1) = 1.
- `print(a)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true (the
  [A000007](../A000007/) loop).
- `a,b=b,a+b` builds the right-hand tuple before assigning, so both move one
  step at once: (F(n), F(n+1)) becomes (F(n+1), F(n) + F(n+1)).

**Notes**

- `while 1:print(a);a,b=b,a+b` is one byte longer.
- `a=b=1` + `while[print(b-a)]:a,b=b,a+b` is also 33 bytes: it starts one step
  later, at (F(1), F(2)), and prints the difference b − a = F(n). The 2 bytes
  saved on the start are spent on `-a`.
- Growing a list, `f=[0,1]` + `for x in f:print(x);f+=x+f[-1],`, is 39 bytes.
  sympy's `fibonacci(n)` in an `n+=1` loop is 54, so there is no sympy entry.
- Python ints are exact, so the only limit is the 4300-digit int-to-str limit
  of Python 3.11+: the program prints F(0) to F(20577) and then stops with a
  `ValueError` at F(20578), the first term with more than 4300 digits.
- The b-file has 2001 terms (up to F(2000), 418 digits) and all of them print
  in well under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000045), CC BY-SA 4.0.
