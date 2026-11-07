# A000539

> Sum of 5th powers: 0^5 + 1^5 + 2^5 + ... + n^5.
> — [OEIS A000539](https://oeis.org/A000539)

Offset 0: 0, 1, 33, 276, 1300, 4425, 12201, 29008, 61776, 120825, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**5
```

**How it works**

- a(n) = a(n−1) + n⁵ with a(0) = 0: `a` is the running sum and `n` the
  last summand added.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
  The first pass prints a(0) = 0 before anything is added.
- `n=a=0` starts both with one statement.

**Notes**

- Other versions that print the same terms:
  - the walrus in the print, `a=n=0` / `while[print(a:=a+n**5)]:n+=1`:
    also 34 bytes;
  - `a+=(n:=n+1)**5` as the whole loop body: 36 bytes; `while 1:print(a);…`:
    35;
  - a sum per term, `n=1` / `while[print(sum(k**5for k in range(n)))]:n+=1`:
    49 bytes;
  - with T = n(n+1)/2, Σk⁵ = T²(4T − 1)/3, kept as a running triangular
    number like [A000537](../A000537/):
    `t=n=0` / `while[print(t*t*(4*t-1)//3)]:n+=1;t+=n`, 44 bytes.

  Nothing shorter than 34 was found.
- Exact integer arithmetic, so the program is right for every n.
- About 3.4 million terms in 60 s here. The b-file has 1001 terms
  (up to a(1000)); the bar is the whole b-file in 60 s, and it prints in
  well under a second.
- a(n) < n⁶ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^716: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000539), CC BY-SA 4.0.
