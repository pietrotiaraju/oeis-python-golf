# A000538

> Sum of fourth powers: 0^4 + 1^4 + ... + n^4.
> — [OEIS A000538](https://oeis.org/A000538)

Offset 0: 0, 1, 17, 98, 354, 979, 2275, 4676, 8772, 15333, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**4
```

**How it works**

- a(n) = a(n−1) + n⁴ with a(0) = 0: `a` is the running sum and `n` the
  last summand added.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
  The first pass prints a(0) = 0 before anything is added.
- `n=a=0` starts both with one statement.

**Notes**

- Other versions that print the same terms:
  - the walrus in the print, `a=n=0` / `while[print(a:=a+n**4)]:n+=1`, and
    counting down with `n-=1` (n⁴ = (−n)⁴): also 34 bytes;
  - `a+=(n:=n+1)**4` as the whole loop body: 36 bytes; `while 1:print(a);…`:
    35;
  - a sum per term, `n=1` / `while[print(sum(k**4for k in range(n)))]:n+=1`:
    49 bytes;
  - Faulhaber's polynomial n(n+1)(2n+1)(3n² + 3n − 1)/30 in the same loop:
    56 bytes.

  The cube page [A000537](../A000537/) gets to 33 bytes by squaring a
  triangular number; for fourth powers nothing shorter than 34 was found.
- Exact integer arithmetic, so the program is right for every n.
- About 3.5 million terms in 60 s here. The b-file has 1001 terms
  (up to a(1000)); the bar is the whole b-file in 60 s, and it prints in
  well under a second.
- a(n) < n⁵ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n ≥ 10^860: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000538), CC BY-SA 4.0.
