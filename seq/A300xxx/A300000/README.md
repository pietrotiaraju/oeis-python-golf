# A300000

> The sum of the first n terms of the sequence is the concatenation of the
> first n digits of the sequence, with a(1) = 1.
> — [OEIS A300000](https://oeis.org/A300000)

Offset 1: 1, 10, 99, 999, 9990, 99900, 999000, 9990000, 99900000, …

### Python 3 — 65 bytes

```python
q='';c=0
while[print(a:=9*c+int(q[1:2]or 1))]:c+=a;q=q[1:]+str(a)
```

**How it works**

- Let s be the concatenation of the terms and c(n) the sum of the first n
  terms. The definition says c(n) = int(s[:n]), so c(n) = 10·c(n−1) + dₙ,
  where dₙ is the n-th digit of s. Hence **a(n) = 9·c(n−1) + dₙ**, and the
  implicit definition becomes a plain recurrence. `c` holds c(n−1).
- `q` is a queue of digits of s: each step drops one digit from the front and
  appends the new term. From the second step on, `q` holds s from position
  n−1, so `q[1]` is dₙ. The first `q[1:]` cuts an empty string and removes
  nothing, which is what lines the queue up.
- In the first two steps the digit needed is the leading digit of the term
  being computed (a(1) = 1, a(2) = 10), so `q` does not have it yet and
  `or 1` supplies it.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`.

**Notes**

- Python 3.11+ refuses to convert integers over 4300 digits to text, so the
  program stops with `ValueError` after a(4301). `python -X
  int_max_str_digits=0` lifts the limit (tested to 6000 terms).
- Other shapes tried: indexing the whole string with a fallback,
  `(s+'1')[n]` (67 bytes); prefix differences `int(s[:n])` (67); the queue read
  with `q[:1]` (66).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 66 | first entry |
| 2026-11-05 | Python 3 | 65 | `while[print(...)]:` loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A300000), CC BY-SA 4.0.
