# A000659

> a(n) = 2^a(n-1) + a(n-2).
> — [OEIS A000659](https://oeis.org/A000659)

Offset 0: 0, 0, 1, 2, 5, 34, 17179869189, …

### Python 3 — 37 bytes

```python
a=-1;b=0
while[print(b)]:a,b=b,2**b+a
```

**How it works**

- The pair (a, b) holds (a(n − 1), a(n)): print a(n), then shift to
  (a(n), 2^a(n) + a(n − 1)), which is a(n + 1) by the recurrence.
- Running the recurrence backwards from a(0) = a(1) = 0 gives a(−1) = −1
  (a(1) = 2^a(0) + a(−1)), so the start a = −1, b = 0 prints a(0) first.
- Printing b, the newest term, before computing the next one matters: a(7)
  is out of reach, and the other order would have to compute it before
  printing a(6).

**Notes**

- Exact integer arithmetic. The terms are 0, 0, 1, 2, 5, 34, 17179869189;
  a(7) = 2^17179869189 + 34 has 5171655948 digits (about 2.1 GB in binary).
  After printing a(6) the program starts building it and would use gigabytes
  of memory, and it could never print it because of the 4300-digit
  int-to-str limit of Python 3.11+ (interpreter limits). The verifier stops
  it as soon as the seventh line arrives; don't leave it running on its own.
- The b-file has the 7 terms a(0), …, a(6); the bar is all 7, printed
  instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000659), CC BY-SA 4.0.
