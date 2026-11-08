# A000975

> a(2n) = 2*a(2n-1), a(2n+1) = 2*a(2n)+1 (also a(n) is the n-th number without consecutive equal binary digits).
> — [OEIS A000975](https://oeis.org/A000975)

Offset 0: 0, 1, 2, 5, 10, 21, 42, 85, 170, 341, 682, 1365, 2730, 5461, 10922, …

### Python 3 — 27 bytes

```python
n=2
while[print(n//3)]:n*=2
```

**How it works**

- a(n) = ⌊2ⁿ⁺¹/3⌋ (a formula in the entry). Proof: 2ⁿ⁺¹ mod 3 is 2 for
  even n and 1 for odd n, so b(n) = ⌊2ⁿ⁺¹/3⌋ satisfies b(n+1) = 2b(n) + 1
  after an even n and b(n+1) = 2b(n) after an odd n, with b(0) = 0: the
  defining recurrence.
- In binary this is 1010…, the leading bits of 2/3 = 0.101010…₂, which is
  the "no two equal adjacent binary digits" description in the name.
- `n` runs over 2, 4, 8, …, and `n//3` is the term.

**Notes**

- Exact integer arithmetic. `n=1` with `n-=~n` (2ᵏ − 1) is another
  27-byte form; the recurrence `a-=~a+a%2` (a ← 2a + 1 − a mod 2) is
  29 bytes.
- The program stops at Python's 4300-digit `int`-to-`str` limit near
  n = 14284; the b-file has 3301 terms (n ≤ 3300) and the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000975), CC BY-SA 4.0.
