# A001042

> a(n) = a(n-1)^2 - a(n-2)^2.
> — [OEIS A001042](https://oeis.org/A001042)

Offset 0: 1, 2, 3, 5, 16, 231, 53105, 2820087664, 7952894429824835871, …

### Python 3 — 37 bytes

```python
a=1;b=2
while[print(a)]:a,b=b,b*b-a*a
```

**How it works**

- `a` and `b` hold two consecutive terms, a(n) and a(n+1), starting from
  a(0) = 1 and a(1) = 2 (the OEIS data: a(2) = 2² − 1² = 3,
  a(3) = 3² − 2² = 5, …).
- `print(a)` runs in the loop condition: it returns `None`, and `[None]` is
  a non-empty list, so the loop never ends.
- `a,b=b,b*b-a*a` moves one step: the new pair is a(n+1) and
  a(n+1)² − a(n)² = a(n+2). Exact integer arithmetic.

**Notes**

- There is no earlier start: a(1) = a(0)² − a(−1)² would need
  a(−1)² = −1. Keeping the square instead (`b` = a(n−1)², as in
  [A000283](../../A000xxx/A000283/)) allows the start b = −1:
  `a=1;b=-1` / `while[print(a)]:a=-b+(b:=a*a)` is correct but 39 bytes, and
  `(b-a)*(b+a)` is longer than `b*b-a*a`.
- The terms roughly double in length each step (a(n) ~ c^(2ⁿ),
  c ≈ 1.1853): a(13) has 605 digits, a(15) 2420 and a(16) 4839. The program
  prints a(0) to a(15) and then stops on Python's 4300-digit int-to-str
  limit (a `ValueError` on stderr), an interpreter limit, not a failure.
- The b-file has 14 terms (a(0) to a(13)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001042), CC BY-SA 4.0.
