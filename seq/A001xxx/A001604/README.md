# A001604

> Odd-indexed terms of A124297.
> — [OEIS A001604](https://oeis.org/A001604)

Offset 0: 11, 31, 151, 911, 5951, 40051, 272611, 1863551, 12760031, 87424711, …

### Python 3 — 39 bytes

```python
a=b=1
while[print(-~a*a*5+1)]:a+=b;b+=a
```

**How it works**

- The entry defines the sequence as the odd-indexed terms of [A124297](https://oeis.org/A124297),
  whose terms are [A124297](https://oeis.org/A124297)(m) = 5F(m)² + 5F(m) + 1 with F the Fibonacci
  numbers. So a(n) = 5F(2n+1)² + 5F(2n+1) + 1.
- `a+=b;b+=a` moves (a, b) = (F(2n+1), F(2n+2)) two Fibonacci steps at a
  time, from (F(1), F(2)) = (1, 1). The printed `-~a*a*5+1` is
  5a(a + 1) + 1 (`-~a` is a + 1).

**Notes**

- For odd m these numbers are the Aurifeuillian factors of the Lucas
  numbers, L(5m) = L(m)·(5F(m)² − 5F(m) + 1)·(5F(m)² + 5F(m) + 1)
  (comment in [A124297](https://oeis.org/A124297)); this is the entry's old name, "related to factors
  of Fibonacci numbers".
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1188 terms (a(0) to a(1187)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001604), CC BY-SA 4.0.
