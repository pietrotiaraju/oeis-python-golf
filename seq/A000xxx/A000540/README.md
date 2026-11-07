# A000540

> Sum of 6th powers: 0^6 + 1^6 + 2^6 + ... + n^6.
> — [OEIS A000540](https://oeis.org/A000540)

Offset 0: 0, 1, 65, 794, 4890, 20515, 67171, 184820, 446964, 978405, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**6
```

**How it works**

- a(n) = a(n−1) + n⁶ with a(0) = 0: `a` is the running sum and `n` the
  last summand added.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
  The first pass prints a(0) = 0 before anything is added.
- `n=a=0` starts both with one statement.

**Notes**

- Other versions that print the same terms:
  - the walrus in the print, `a=n=0` / `while[print(a:=a+n**6)]:n+=1`, and
    counting down with `n-=1` (n⁶ = (−n)⁶): also 34 bytes;
  - `a+=(n:=n+1)**6` as the whole loop body: 36 bytes; `while 1:print(a);…`:
    35;
  - a sum per term, `n=1` / `while[print(sum(k**6for k in range(n)))]:n+=1`:
    49 bytes;
  - Faulhaber's polynomial n(n+1)(2n+1)(3n⁴ + 6n³ − 3n + 1)/42 in the same
    loop: 64 bytes.

  Nothing shorter than 34 was found.
- Exact integer arithmetic, so the program is right for every n.
- About 3.1 million terms in 60 s here. The b-file has 1001 terms
  (up to a(1000)); the bar is the whole b-file in 60 s, and it prints in
  well under a second.
- a(n) < n⁷ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^614: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000540), CC BY-SA 4.0.
