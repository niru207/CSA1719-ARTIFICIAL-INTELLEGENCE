monkey_box_banana(state(P, P, P, P, P, P)).
monkey_box_banana(state(X1, Y, X2, Y, X3, Y)) :-
    X1 > 0,
    X1_new is X1 - 1,
    monkey_box_banana(state(X1_new, Y, X2, Y, X3, Y)).
monkey_box_banana(state(X1, Y, X2, Y, X3, Y)) :-
    X1 < 4,
    X1_new is X1 + 1,
    monkey_box_banana(state(X1_new, Y, X2, Y, X3, Y)).
monkey_box_banana(state(X, Y1, X, Y2, X, Y3)) :-
    Y1 > 0,
    Y1_new is Y1 - 1,
    monkey_box_banana(state(X, Y1_new, X, Y2, X, Y3)).
monkey_box_banana(state(X, Y1, X, Y2, X, Y3)) :-
    Y1 < 4,
    Y1_new is Y1 + 1,
    monkey_box_banana(state(X, Y1_new, X, Y2, X, Y3)).
monkey_box_banana(state(X1, Y, X1, Y, X2, Y)) :-
    X1 > 0,
    X2 > 0,
    X1_new is X1 - 1,
    X2_new is X2 - 1,
    monkey_box_banana(state(X1_new, Y, X2_new, Y, X2_new, Y)).
monkey_box_banana(state(X1, Y, X1, Y, X2, Y)) :-
    X1 < 4,
    X2 < 4,
    X1_new is X1 + 1,
    X2_new is X2 + 1,
    monkey_box_banana(state(X1_new, Y, X2_new, Y, X2_new, Y)).
monkey_box_banana(state(X, Y1, X, Y1, X, Y2)) :-
    Y1 > 0,
    Y2 > 0,
    Y1_new is Y1 - 1,
    Y2_new is Y2 - 1,
    monkey_box_banana(state(X, Y1_new, X, Y2_new, X, Y2_new)).
monkey_box_banana(state(X, Y1, X, Y1, X, Y2)) :-
    Y1 < 4,
    Y2 < 4,
    Y1_new is Y1 + 1,
    Y2_new is Y2 + 1,
    monkey_box_banana(state(X, Y1_new, X, Y2_new, X, Y2_new)).
