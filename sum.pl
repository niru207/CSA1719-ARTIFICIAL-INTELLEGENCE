sum(0, 0).
sum(N, Sum) :-
    N > 0,
    Prev is N - 1,
    sum(Prev, PrevSum),
    Sum is N + PrevSum.
