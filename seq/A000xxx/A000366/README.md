# A000366

> Genocchi numbers of second kind (A005439) divided by 2^(n-1).
> — [OEIS A000366](https://oeis.org/A000366)

Offset 1: 1, 1, 2, 7, 38, 295, 3098, 42271, 726734, 15366679, …

### Python 3 — 81 bytes

```python
r=[t:=1]
while[print(t>>len(r)-1)]:s=sum(r);t=0;r=[t:=t+(s:=s-x)+x for x in[0]+r]
```

**How it works**

- Seidel's 1877 algorithm for the median Genocchi numbers H(n) =
  A005439(n), as in Luschny's Sage program in the OEIS entry: a row D of
  length n is replaced by the suffix sums of the prefix sums of D + [0], and
  H(n) is the first entry of row n. Rows: [1], [2, 1], [8, 6, 3],
  [56, 48, 34, 17], …; then a(n) = H(n)/2^(n−1).
- The program keeps r = D reversed. Reversing turns prefix sums into suffix
  sums and back, so the step becomes r ← prefix sums of the suffix sums of
  [0] + r, and H(n) is the last entry, which the walrus `t` holds when the
  comprehension ends. Rows: [1], [1, 2], [3, 6, 8], [17, 34, 48, 56], ….
- The suffix sums need no second pass: with s = sum(r), the suffix sum at
  position j of w = [0] + r is s minus the entries before j. In
  `(s:=s-x)+x` the walrus takes the current entry off s, and adding it back
  gives the value of s before it, which is exactly that suffix sum. `t`
  adds them up, so the comprehension builds the new row in one pass; `t=0`
  restarts the prefix sum.
- Row n has n entries, so `t>>len(r)-1` divides H(n) by 2^(n−1). The
  division is exact because that is how this sequence is defined:
  A005439(n) is 2^(n−1) times an integer, a(n).

**Notes**

- Exact integer arithmetic, correct for every n.
- The four steps of Luschny's loop written as two comprehensions, one per
  direction, with the shift: about 100 bytes.
- The rows of the related triangle [A014784](https://oeis.org/A014784)
  (first column = this sequence) seem to follow a simpler rule: the second
  differences of row n are minus the sums of adjacent entries of row n − 1,
  which gives a 77-byte program
  (`r=[1]` / `while[print(r[0])]:d=sum(r);t=y=0;r=[t:=t+(d:=d-y-(y:=x))for x in[0]+r]`)
  that agrees with this one for the first 972 terms. The rule was read off
  the data and is not proved, so it is not the record.
- Row n has n entries and is built in one pass, so the first N terms take
  about 3N²/2 big-integer additions. The whole b-file (100 terms) prints in
  about 0.1 s;
  the program stops after a(972), when the next term passes the 4300-digit
  int-to-str limit of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000366), CC BY-SA 4.0.
