# A001576

> a(n) = 1^n + 2^n + 4^n.
> — [OEIS A001576](https://oeis.org/A001576)

Offset 0: 3, 7, 21, 73, 273, 1057, 4161, 16513, 65793, 262657, 1049601, …

### Python 3 — 29 bytes

```python
p=1
while[print(1-p*~p)]:p*=2
```

**How it works**

- With p = 2ⁿ the term is 1 + p + p² (4ⁿ = p², 1ⁿ = 1). The loop keeps p
  itself, starting at 2⁰ = 1 and doubling it, so there is no exponent at all.
- `~p` is −p − 1, so `1-p*~p` is 1 + p(p + 1): 6 characters against 7 for
  `1+p+p*p`. Since p² + p is always even, `p*p+p|1` is also right, at 7.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only doubles p.

**Notes**

- The definition with a counter, `n=0` / `while[print(1+2**n+4**n)]:n+=1`, is
  34 bytes.
- Exact integers, so every term is right; a(7143) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.
- Sums of powers: [A001550](../A001550/) to [A001557](../A001557/),
  [A001579](../A001579/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001576), CC BY-SA 4.0.
