# A000452

> The greedy sequence of integers which avoids 3-term geometric progressions.
> — [OEIS A000452](https://oeis.org/A000452)

Offset 1: 1, 2, 3, 5, 6, 7, 8, 10, 11, 13, …

Each term is the least integer above the previous one that is not the
third term of a geometric progression x, y, n (y² = x·n, x < y, any
rational ratio) with x and y earlier terms.

### Python 3 — 83 bytes

```python
S=[];E={n:=0}
while n:=n+1:
 if{n}-E:print(n);E|={n*n//a*(n*n%a<1)for a in S};S+=n,
```

**How it works**

- **The definition, run directly.** S lists the terms so far and E holds
  every number that is the third term of a progression a, b, b²/a with
  a < b both in S. A new candidate n is the largest number seen, so it
  can only be the last term of a progression with two earlier terms; it
  is a term exactly when n ∉ E.
- **Updating E.** When n is accepted, the progressions with n as the
  middle term are a, n, n²/a for the earlier terms a that divide n²;
  `n*n//a*(n*n%a<1)` is n²/a for those and 0 for the others (0 is
  already in E, and is never a candidate). Every pair a < b of terms is
  handled when b is accepted, and b²/a > b, so E is complete for every
  later candidate.
- `{n}-E` is the empty set, which is false, exactly when n ∈ E (4 bytes
  under `n not in E`). `E={n:=0}` starts E as {0} and n at 0 in one
  statement.

**Notes**

- Other versions that print the same terms:
  - the filter in the comprehension,
    `E|={n*n//a for a in S if n*n%a<1}`: 84 bytes and about twice as fast
    (the bar in 17 s instead of 30 s), since non-divisors add nothing to
    the set;
  - the characterization below with trial division (each prime exponent
    tested digit by digit in base 3): 119 bytes, and the original
    156-byte version of it.
- The terms are the integers whose prime exponents all have only the
  digits 0 and 1 in base 3 (Rankin 1961 showed this set has no 3-term
  geometric progression and has density 0.7197…; Brown and Gordon showed
  it is the greedy sequence; McNew's comment on the entry). The program
  does not use this; it follows the definition.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 10000 terms (up to 13886) take about 30 s here; each new
  term scans all earlier ones. The b-file has 10000 terms (up to
  a(10000)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 156 | first entry |
| 2026-11-07 | Python 3 | 83 | greedy definition with a set of excluded numbers |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000452), CC BY-SA 4.0.
