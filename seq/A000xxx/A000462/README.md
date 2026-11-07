# A000462

> Numbers written in base of triangular numbers.
> — [OEIS A000462](https://oeis.org/A000462)

Offset 1: 1, 2, 10, 11, 12, 100, 101, 102, 110, 1000, …

a(n) writes n greedily with the place values 1, 3, 6, 10, 15, … (the
triangular numbers T_k = k(k+1)/2, lowest place on the right): 20 =
1·15 + 0·10 + 0·6 + 1·3 + 2·1 gives a(20) = 10012.

### Python 3 — 65 bytes

```python
L=[i:=0];K=1
while[print(x:=10**~-K+L[i])]:L+=x,;i=-~i%-~K;K+=i<1
```

**How it works**

- **Blocks.** Let T_K ≤ n < T_{K+1}, so n = T_K + j with 0 ≤ j ≤ K (the
  gap T_{K+1} − T_K is K + 1). For K ≥ 2 the top digit is 1, because
  T_{K+1} ≤ 2T_K, and the rest j is below T_K, so the lower places hold
  the greedy representation of j itself (greedy on n continues exactly as
  greedy on j would). For K = 1 the same reading works with
  a(2) = 1 + a(1) = 2. Hence, with a(0) = 0,

  a(T_K + j) = 10^(K−1) + a(j),  0 ≤ j ≤ K,

  and block K (K + 1 terms) is 10^(K−1) added to a(0), a(1), …, a(K).
  The digits are 0, 1 and 2, so the result is the decimal integer of the
  digit string.
- **The loop.** `L` holds a(0), a(1), … and grows by each new term; `i` is
  the offset j inside block K. `i=-~i%-~K` steps i through 0, …, K and
  wraps to 0, and `K+=i<1` then opens the next block. In block 1 the
  entry L[1] = a(1) is appended just before it is read, so the list is
  always long enough.
- `L=[i:=0]` makes the list [a(0)] and sets i = 0 in one statement.

**Notes**

- Other versions that print the same terms: greedy division per n,
  scanning all places k = n, …, 1 from the top (leading zeros vanish
  in `s=s*10+r//t`):
  `n=0` / `while n:=n+1:` / ` r=k=n;s=0;t=n*-~n//2` /
  ` while k:s=s*10+r//t;r%=t;t-=k;k-=1` / ` print(s)`: 85 bytes and
  O(n) per term (7849 terms in 30 s); finding
  the top place first and building a string, the first version: 115
  bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 10000 terms print in 0.4 s here, about 390000 terms in
  20 s. The list keeps every term, but at 10000 terms it is small. The
  b-file has 10000 terms (up to a(10000)); the bar is the whole b-file in
  60 s.
- a(n) has K digits for T_K ≤ n < T_{K+1}, so the first term with more
  than 4300 digits is a(T₄₃₀₁) = a(9251451), where printing stops.
- [A000433](../A000433/) is the same construction with the cubes as
  place values.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 121 | first entry |
| 2026-11-06 | Python 3 | 115 | advance triangular place values by consecutive differences |
| 2026-11-07 | Python 3 | 65 | a(T_K + j) = 10^(K−1) + a(j) from a list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000462), CC BY-SA 4.0.
