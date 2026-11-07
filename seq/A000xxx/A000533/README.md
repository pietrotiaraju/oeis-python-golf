# A000533

> a(0)=1; a(n) = 10^n + 1, n >= 1.
> — [OEIS A000533](https://oeis.org/A000533)

Offset 0: 1, 11, 101, 1001, 10001, 100001, 1000001, 10000001, 100000001, 1000000001, …

### Python 3 — 27 bytes

```python
n=1
while[print(n|1)]:n*=10
```

**How it works**

- `n` runs through 10⁰, 10¹, 10², … For k ≥ 1, 10^k is even, so
  10^k | 1 = 10^k + 1; for k = 0, 1 | 1 = 1. The bitwise OR gives the
  exceptional a(0) = 1 and the general term with no test.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `n+(n>1)` in place of `n|1`:
  31 bytes; `n=0` / `while[print(n+1)]:n=n*10or 10`: 33 bytes; the same
  terms as strings, `s='1'` / `while[print(s[:-1]+'1')]:s+='0'`: 37 bytes,
  with no 4300-digit limit.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s, and it prints at once.
- a(4300) = 10^4300 + 1 has 4301 digits, more than Python's int-to-str
  limit, so printing stops after a(4299), about 1 s in here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |
| 2026-11-07 | Python 3 | 27 | OR with 1 over the powers of ten |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000533), CC BY-SA 4.0.
