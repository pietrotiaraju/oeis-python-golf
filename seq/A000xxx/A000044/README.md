# A000044

> Dying rabbits: a(0) = 1; for 1 <= n <= 12, a(n) = Fibonacci(n); for n >= 13,
> a(n) = a(n-1) + a(n-2) - a(n-13).
> — [OEIS A000044](https://oeis.org/A000044)

Offset 0: 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 232, 375, 606, 979, …

### Python 3 — 42 bytes

```python
a=1,
while[print(a[0])]:a=sum(a[:11:2]),*a
```

**How it works**

- a(n) is also the number of compositions of n into odd parts 1, 3, …, 11,
  with generating function 1/(1 − z − z³ − z⁵ − z⁷ − z⁹ − z¹¹), so
  **a(n) = a(n−1) + a(n−3) + … + a(n−11)** with a(0) = 1 and a(n) = 0 for
  n < 0.
- That matches the definition for every n: (1 − z²)(1 − z − z³ − … − z¹¹)
  = 1 − z − z² + z¹³, so the compositions obey the defining recurrence
  a(n) = a(n−1) + a(n−2) − a(n−13) for n ≥ 3, and for n ≤ 12 no part can be
  13 or more, so they are the compositions into any odd parts, counted by
  Fibonacci(n).
- `a` is a tuple with the newest term first, so `a[:11:2]` is
  a(n−1), a(n−3), …, a(n−11). While the tuple is shorter than 11 the slice
  just stops early, which is exactly the zeros for n < 0, so `a=1,` is the
  only start-up needed.
- `a=sum(…),*a` puts the new term in front. `while[print(a[0])]:` prints
  in the loop condition: `[None]` is a non-empty list, so it is true.

**Notes**

- The tuple keeps every term and is copied each step, which is nothing for
  the whole b-file (1001 terms, the bar is all of them in 60 s).
- The defining recurrence needs 13 starting values. Appending to a list
  instead, `a=[1]` with `a+=sum(a[:-12:-2]),` (reading backwards from the
  end), is 45 bytes, both with `while[print(a[-1])]:` and with
  `for x in a:print(x);`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000044), CC BY-SA 4.0.
