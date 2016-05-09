tree(root, left, right) :-
	Tree = tree(root, [left, right]),
	Left = tree(left, [_,_]),
	Right = tree(right, [_,_]),
	is_father(father, left),
	is_father(father, right),
	is_left_son(left, father),
	is_right_son(right, father).

a := tree([1,1], [2,1], [1,2]).


