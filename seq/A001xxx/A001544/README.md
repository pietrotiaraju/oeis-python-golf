# A001544

> A nonlinear recurrence: a(n) = a(n-1)^2 - 6*a(n-1) + 6, with a(0) = 1, a(1) = 7.
> — [OEIS A001544](https://oeis.org/A001544)

Offset 0: 1, 7, 13, 97, 8833, 77968897, 6079148431583233, …

### Python 3 — 32 bytes

```python
p=a=1
while[print(a)]:a=p+6;p*=a
```

**How it works**

- The title's recurrence a(n) = a(n−1)² − 6·a(n−1) + 6 starts at n = 2
  (a(0) = 1 is a fixed point of it). For n ≥ 1, a(n) = 6 + a(0)·…·a(n−1):
  true for a(1) = 7, and if it holds for n then
  a(0)·…·a(n) = (a(n) − 6)·a(n), so 6 + a(0)·…·a(n) =
  a(n)² − 6·a(n) + 6 = a(n+1).
- `p` holds the product: `a=p+6` is a(n), and `p*=a` adds it to the product
  for the next term. Since a(0) = 1, the start `p=a=1` serves both as a(0)
  and as the product a(0) = 1 that a(1) needs.

**Notes**

- The recurrence itself needs a(0) apart: `print(1);a=7` /
  `while[print(a)]:a=a*(a-6)+6` is 40 bytes.
- The same program with 5 in place of 6 is [A001543](../A001543/).
- Exact integer arithmetic, so the program is right for every n. a(n)
  grows doubly exponentially (the number of digits doubles at each step):
  a(14) has 4041 digits and a(15) 8082, so Python's 4300-digit
  int-to-str limit stops the program after a(14).
- The b-file has 12 terms (a(0) to a(11), up to 506 digits); the bar is
  the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001544), CC BY-SA 4.0.
