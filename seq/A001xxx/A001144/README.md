# A001144

> An exponential function on partitions (next term is 2^512).
> — [OEIS A001144](https://oeis.org/A001144)

Offset 1: 1, 2, 3, 4, 9, 27, 512, 134217728, …

### Python 3 — 50 bytes

```python
a=0;b=c=1
while[print(c)]:a,b,c=b,c,max(2**b,3**a)
```

**How it works**

- The definition (Adams-Watters's comment on the entry, and Golomb and
  Richman's Monthly problem E2118): a(n) is the largest value of a tower
  a₁^a₂^…^a_k = a₁^(a₂^(…^a_k)) of positive integers with
  a₁ + a₂ + … + a_k = n.
- **Recursion.** Put f(0) = 1 (the empty tower). A tower whose first part
  is k is k^T, where T is a tower of the remaining n − k (T = 1 when k = n).
  For k = 1 that is 1, and for k ≥ 2 the map T ↦ k^T is increasing, so the
  best T is the largest. Hence f(n) = max over 1 ≤ k ≤ n of k^f(n−k).
  By induction f is non-decreasing: f(0) = f(1) = 1, and if f is
  non-decreasing up to n then k^f(n+1−k) ≥ k^f(n−k) for each k ≤ n, so
  f(n+1) ≥ f(n).
- **Only k = 2 and k = 3 matter.** The term k = 2 gives
  f(m+2) ≥ 2^f(m) ≥ 2·f(m) (2^x ≥ 2x for every integer x ≥ 1), so
  f(m+2j) ≥ 2^j·f(m) and, f being non-decreasing, f(m+i) ≥ 2^⌊i/2⌋·f(m).
  With m = n − k:
  - k = 4: 4^f(m) = 2^(2·f(m)) ≤ 2^f(m+2) = 2^f(n−2);
  - k ≥ 5: f(n−3) = f(m+k−3) ≥ 2^⌊(k−3)/2⌋·f(m) ≥ log₃(k)·f(m) (2 ≥ log₃ 5,
    log₃ 6; 4 ≥ log₃ 7, log₃ 8; and from there the left side doubles while
    log₃ k grows by less than 1), so k^f(m) ≤ 3^f(n−3);
  - k = 1 gives 1, never more than the others.

  So f(n) = max(2^f(n−2), 3^f(n−3)) for n ≥ 3, and with f(−1) = f(−2) = 0
  the same formula also gives f(1) = max(1, 1) = 1 and f(2) = max(2, 1) = 2.
- The program keeps (a, b, c) = (f(n−2), f(n−1), f(n)), starting from
  (f(−1), f(0), f(1)) = (0, 1, 1): it prints c, then shifts in
  max(2^b, 3^a). From n = 7 on the 2-term always wins, which is the
  entry's formula a(n) = 2^a(n−2), n ≥ 7; the 3-term gives 3, 9 and 27.
- Each term is computed just before it is printed, so nothing larger than
  the next term is ever built.

**Notes**

- a(9) = 2^512 (155 digits, the "next term" of the name) still prints.
  a(10) = 2^134217728 is computed in a moment (16 MB), but it has
  40,403,563 digits, and printing it stops the program with the 4300-digit
  int-to-str limit of Python 3.12: an interpreter limit. a(11) = 2^(2^512)
  could not be stored anywhere.
- The bar is the b-file, the 8 terms of the OEIS data, in 60 s; all 9
  printable terms come out at once.
- A brute force over all towers (compositions of n) agrees for n ≤ 9.
- The entry's second comment restates the maximum as the largest number
  made from n copies of the constant 1 with + and ^; the program follows
  the tower definition above.
- Following the recursion over every k instead
  (`b=1,` / `while[print(x:=max(k**y for k,y in enumerate(b,1)))]:b=x,*b`,
  64 bytes) needs no lemma; the lemma saves 14 bytes. Hard-coding
  1, 2, 3, 4, 9, 27 and then a(n) = 2^a(n−2) is shorter as a list loop
  (`a=[1,2,3,4,9,27]` / `for x in a:print(x);a+=2**a[-2],`, 49 bytes),
  but it appends six terms ahead: right after printing a(5) = 9 it would
  start building a(11) = 2^(2^512) and never print a(6).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001144), CC BY-SA 4.0.
