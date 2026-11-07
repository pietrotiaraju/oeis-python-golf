# A000542

> Sum of 8th powers: 1^8 + 2^8 + ... + n^8.
> — [OEIS A000542](https://oeis.org/A000542)

Offset 0: 0, 1, 257, 6818, 72354, 462979, 2142595, 7907396, 24684612, 67731333, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**8
```

**How it works**

- a(n) = a(n−1) + n⁸ with a(0) = 0: `a` is the running sum and `n` the
  last summand added.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
  The first pass prints a(0) = 0 before anything is added.
- `n=a=0` starts both with one statement.

**Notes**

- Other versions that print the same terms:
  - the walrus in the print, `a=n=0` / `while[print(a:=a+n**8)]:n+=1`, and
    counting down with `n-=1` (n⁸ = (−n)⁸): also 34 bytes;
  - `a+=(n:=n+1)**8` as the whole loop body: 36 bytes; `while 1:print(a);…`:
    35;
  - a sum per term, `n=1` / `while[print(sum(k**8for k in range(n)))]:n+=1`:
    49 bytes;
  - Faulhaber's polynomial
    n(n+1)(2n+1)(5n⁶ + 15n⁵ + 5n⁴ − 15n³ − n² + 9n − 3)/90 in the same loop:
    84 bytes.

  Nothing shorter than 34 was found.
- Exact integer arithmetic, so the program is right for every n.
- About 3.4 million terms in 60 s here. The b-file has 24 terms
  (up to a(23), the terms of the OEIS entry); the bar is the whole b-file in
  60 s, and it prints at once.
- a(n) < n⁹ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^477: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000542), CC BY-SA 4.0.
