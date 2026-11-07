# A000570

> Number of tournaments on n nodes determined by their score vectors.
> — [OEIS A000570](https://oeis.org/A000570)

Offset 1: 1, 1, 2, 4, 7, 11, 18, 31, 53, 89, …

a(n) counts the score sequences of n-vertex tournaments that belong to only
one tournament up to isomorphism.

### Python 3 — 48 bytes

```python
A=1,1,2,4,7
while 1:x,*A=*A,sum(A)-A[3];print(x)
```

**How it works**

- **The recurrence.** The strong components of a tournament are linearly
  ordered (every arc between two of them points the same way), and the score
  sequence determines the components' score sequences: they are cut where
  Landau's inequality Σ_{i≤k} s_i ≥ C(k, 2) is tight. Tetali (1998,
  *A characterization of unique tournaments*, J. Combin. Theory B 72)
  showed that a tournament is unique exactly when each strong component is,
  and that the unique strong tournaments are one each on 1, 3, 4 and 5
  vertices. So a(n) counts the compositions of n into parts 1, 3, 4, 5:
  a(n) = a(n−1) + a(n−3) + a(n−4) + a(n−5) with a(0) = 1 and a(k) = 0 for
  k < 0 (the entry's formula line, Jon E. Schoenfield). A brute force over
  all labelled tournaments on up to 6 vertices gives 1, 1, 2, 4, 7, 11 unique
  score sequences, as it should.
- **The window.** `A` holds the last five terms a(n−5), …, a(n−1), and the
  next one is their sum minus a(n−2), which is `A[3]`.
- **The shift.** `x,*A=*A,new` appends the new term and drops the oldest
  into `x` in one starred assignment, so the program prints the term that
  leaves the window. The first pass starts from the tuple a(1), …, a(5),
  prints a(1) and appends a(6); from then on `A` is a list.

**Notes**

- Other versions that print the same terms: printing `A[0]` in the loop
  head, `while[print(A[0])]:x,*A=*A,sum(A)-A[3]`: 50 bytes; slicing,
  `A=[1,1,2,4,7]` / `while[print(A[0])]:A=A[1:]+[sum(A)-A[3]]`: 54 bytes;
  five variables, `a=b=c=0;d=e=1` /
  `while[print(e)]:a,b,c,d,e=b,c,d,e,a+b+c+e`: 55 bytes.
- Exact integer arithmetic; correctness for every n rests on Tetali's
  characterization.
- The b-file has 500 terms (up to a(500)); the bar is the whole b-file in
  60 s, and the program prints it at once.
- a(n) grows like 1.685ⁿ, and a(18975) is the first term with more than 4300
  digits, so Python's int-to-str limit stops the printing after a(18974),
  about 5 s into the run here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 54 | first entry |
| 2026-11-07 | Python 3 | 48 | starred-assignment shift `x,*A=*A,…`, print the dropped term |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000570), CC BY-SA 4.0.
