# A001468

> There are a(n) 2's between successive 1's.
> — [OEIS A001468](https://oeis.org/A001468)

Offset 0: 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, …

### Python 3 — 38 bytes

```python
a=[1]
for x in a:print(x);a+=[2]*x+[1]
```

**How it works**

- **The title as a rule.** The sequence starts with a 1 and is made of 1's
  and 2's; cut it before each 1 and the n-th piece (n = 0, 1, …) is a 1
  followed by a(n) 2's. Read the other way round, the sequence is a 1, then
  a(0) 2's and a 1, then a(1) 2's and a 1, and so on:
  a = 1 · τ(a(0)) τ(a(1)) τ(a(2)) …, with τ(x) = 2…2 1 (x twos). Every
  block only depends on an earlier term, so this fixes the whole sequence.
- **A queue that feeds itself.** `a` starts as [1]; the `for` loop walks
  the list while it grows (a Python list iterator sees appended items), and
  for each term x it prints x and appends τ(x) = `[2]*x+[1]`. Each block
  has at least two entries, so the list always runs ahead of the loop, and
  the list becomes exactly 1 τ(a(0)) τ(a(1)) ….
- This is the Fibonacci word on {2, 1} with an extra 1 in front, so a(n) =
  ⌊(n + 1)τ⌋ − ⌊nτ⌋ with τ the golden ratio (formula in the entry); the
  program does not need it.

**Notes**

- Integers only; the list holds about 1.6 times as many entries as terms
  printed. The b-file (1001 terms) prints instantly; the bar is the whole
  b-file in 60 s.
- With the slice trick of [A000201](../../A000xxx/A000201/),
  `a+=(2,2,1)[~x:print(x)]` is 2 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001468), CC BY-SA 4.0.
