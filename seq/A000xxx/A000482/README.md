# A000482

> Unsigned Stirling numbers of first kind s(n,5).
> — [OEIS A000482](https://oeis.org/A000482)

Offset 5: 1, 15, 175, 1960, 22449, 269325, 3416930, 45995730, 657206836, 9957703756, …

### Python 3 — 79 bytes

```python
a=0;b=1;c=e=6;d=11;n=4
while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;d=d*n+e;e*=n;n+=1
```

**How it works**

Apply the unsigned Stirling recurrence s(n+1,k)=n*s(n,k)+s(n,k-1)
to columns k=1 through 5. Initially the row for n=4 is
(s(4,5),s(4,4),s(4,3),s(4,2),s(4,1))=(0,1,6,11,6).
Compute and print the new fifth column, then update lower columns
in descending order so that every expression uses the old row.
The first printed term is s(5,5)=1.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 96 terms in 60 s; the official b-file contains 96 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000482), CC BY-SA 4.0.
