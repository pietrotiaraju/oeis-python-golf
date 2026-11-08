# A001060

> a(n) = a(n-1) + a(n-2) with a(0)=2, a(1)=5. Sometimes called the Evangelist Sequence.
> — [OEIS A001060](https://oeis.org/A001060)

Offset 0: 2, 5, 7, 12, 19, 31, 50, 81, 131, 212, 343, 555, 898, 1453, 2351, …

### Python 3 — 33 bytes

```python
a,b=2,5
while[print(a)]:a,b=b,a+b
```

**How it works**

- `a` and `b` hold two consecutive terms, a(n) and a(n+1), starting from
  a(0) = 2 and a(1) = 5.
- `print(a)` runs in the loop condition: it returns `None`, and `[None]` is
  a non-empty list, so the loop never ends.
- `a,b=b,a+b` moves one step along the recurrence. This is the
  [Lucas](../../A000xxx/A000032/) program with another start; integers are
  exact, so every term is right.

**Notes**

- The [Fibonacci](../../A000xxx/A000045/) trick (keep a(n−1) and a(n+1),
  print the difference) ties: `a,b=3,5` / `while[print(a:=b-a)]:b+=a` is 33
  bytes. The loop is as long as the tuple one; for F the gain came from the
  start `a=b=1`, and here the start (a(−1), a(1)) = (3, 5) is still two
  numbers. `a,b=2,3` /
  `while[print(a)]:a,b=a+b,a` (`b` keeps the previous term, a(−1) = 3) is
  33 as well.
- A search over loops with two in-place statements or a tuple update
  (coefficients up to 20, a walrus or a small combination in the print,
  start values solved exactly) found nothing shorter.
- Python's 4300-digit int-to-str limit stops the program at a(20574), the
  first term with 4301 digits, after printing a(0) to a(20573).
- The b-file has 1001 terms (a(0) to a(1000), 210 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001060), CC BY-SA 4.0.
