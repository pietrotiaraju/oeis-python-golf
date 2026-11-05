# A000007

> The characteristic function of {0}: a(n) = 0^n.
> — [OEIS A000007](https://oeis.org/A000007)

Offset 0: 1, 0, 0, 0, 0, …

Not the same as [A000004](../A000004/): the first term is 1.

### Python 3 — 23 bytes

```python
n=1
while[print(n)]:n=0
```

**How it works**

- `print(n)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true.
- The body sets `n` to 0 after the first term, so 1 is printed once and 0
  forever after.

**Notes**

- `n=1` + `while 1:print(n);n=0` is 24 bytes; `print(1)` followed by the
  A000004 loop is 25.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 23 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000007), CC BY-SA 4.0.
