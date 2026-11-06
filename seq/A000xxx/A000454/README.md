# A000454

> Unsigned Stirling numbers of first kind s(n,4).
> — [OEIS A000454](https://oeis.org/A000454)

Offset 4: 1, 10, 85, 735, 6769, 67284, 723680, 8409500, 105258076, 1414014888, …

### Python 3 — 68 bytes

```python
a=0;b=1;c=3;d=2;n=3
while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;d*=n;n+=1
```

**How it works**

Use the unsigned Stirling recurrence s(n+1,k)=n*s(n,k)+s(n,k-1).
Initially (a,b,c,d)=(s(3,4),s(3,3),s(3,2),s(3,1))=(0,1,3,2).
The walrus computes s(n+1,4) before printing; update lower columns
in descending order so each expression still sees the previous row.
The first printed value is therefore s(4,4)=1.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 97 terms in 60 s; the official b-file contains 97 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000454), CC BY-SA 4.0.
