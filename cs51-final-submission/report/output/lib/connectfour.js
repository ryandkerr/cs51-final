/* start module: connectfour */
$pyjs['loaded_modules']['connectfour'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['connectfour']['__was_initialized__']) return $pyjs['loaded_modules']['connectfour'];
	var $m = $pyjs['loaded_modules']['connectfour'];
	$m['__repr__'] = function() { return '<module: connectfour>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'connectfour';
	$m['__name__'] = __mod_name__;
	var $mul9,$mul8,$mul7,$mul6,$mul5,$mul4,$mul3,$mul2,$mul1,$mul14,$mul13,$mul12,$mul11,$mul10;

	$m['time'] = $p['___import___']('time', null);
	$m['sys'] = $p['___import___']('sys', null);
	$p['__import_all__']('evaluate', null, $m, null, false);
	$p['__import_all__']('prototype', null, $m, null, false);
	$p['__import_all__']('board_functions', null, $m, null, false);
	$m['board'] = $p['list']([(typeof ($mul1=$p['list'](['*']))==typeof ($mul2=6) && typeof $mul1=='number'?
		$mul1*$mul2:
		$p['op_mul']($mul1,$mul2)), (typeof ($mul3=$p['list'](['*']))==typeof ($mul4=6) && typeof $mul3=='number'?
		$mul3*$mul4:
		$p['op_mul']($mul3,$mul4)), (typeof ($mul5=$p['list'](['*']))==typeof ($mul6=6) && typeof $mul5=='number'?
		$mul5*$mul6:
		$p['op_mul']($mul5,$mul6)), (typeof ($mul7=$p['list'](['*']))==typeof ($mul8=6) && typeof $mul7=='number'?
		$mul7*$mul8:
		$p['op_mul']($mul7,$mul8)), (typeof ($mul9=$p['list'](['*']))==typeof ($mul10=6) && typeof $mul9=='number'?
		$mul9*$mul10:
		$p['op_mul']($mul9,$mul10)), (typeof ($mul11=$p['list'](['*']))==typeof ($mul12=6) && typeof $mul11=='number'?
		$mul11*$mul12:
		$p['op_mul']($mul11,$mul12)), (typeof ($mul13=$p['list'](['*']))==typeof ($mul14=6) && typeof $mul13=='number'?
		$mul13*$mul14:
		$p['op_mul']($mul13,$mul14))]);
	$m['init'] = function() {
		var first;
		$p['printFunc'](["\nHello! My name is Rondo. Let's play Connect Four!"], 1);
		first = $m['raw_input']("You'll be yellow (Y). You can enter 'q' at any prompt to quit.\nWould you like to go first? (y/n):\n")['lower']();
		while ($p['bool']((!$p['op_eq'](first, 'y'))&(!$p['op_eq'](first, 'n'))&(!$p['op_eq'](first, 'q')))) {
			first = $m['raw_input']("\nSorry, I don't understand! Please type 'y' or 'n':\n")['lower']();
		}
		if ($p['bool']($p['op_eq'](first, 'q'))) {
			$m['sys']['exit']();
		}
		$p['printFunc'](['\nStarting board:'], 1);
		(typeof printBoard == "undefined"?$m['printBoard']:printBoard)();
		if ($p['bool']($p['op_eq'](first, 'n'))) {
			$m['playersTurn'] = false;
		}
		else {
			$m['playersTurn'] = true;
		}
		(typeof move == "undefined"?$m['move']:move)();
		return null;
	};
	$m['init']['__name__'] = 'init';

	$m['init']['__bind_type__'] = 0;
	$m['init']['__args__'] = [null,null];
	$m['move'] = function() {

		if ($p['bool']((typeof game_won == "undefined"?$m['game_won']:game_won)($m['board'], 'R'))) {
			$p['printFunc'](['\nGame over! I win!'], 1);
			$m['sys']['exit']();
		}
		else if ($p['bool']((typeof game_won == "undefined"?$m['game_won']:game_won)($m['board'], 'Y'))) {
			$p['printFunc'](['\nGame over! You win!'], 1);
			$m['sys']['exit']();
		}
		else if ($p['bool']((typeof full == "undefined"?$m['full']:full)($m['board']))) {
			$p['printFunc'](["\nGame over! It's a tie!"], 1);
			$m['sys']['exit']();
		}
		else if ($p['bool']($m['playersTurn'])) {
			$m['playersTurn'] = false;
			(typeof movePlayer == "undefined"?$m['movePlayer']:movePlayer)();
		}
		else {
			$m['playersTurn'] = true;
			(typeof moveAI == "undefined"?$m['moveAI']:moveAI)();
		}
		return null;
	};
	$m['move']['__name__'] = 'move';

	$m['move']['__bind_type__'] = 0;
	$m['move']['__args__'] = [null,null];
	$m['moveAI'] = function() {

		$p['printFunc'](['\nRondo is thinking....'], 1);
		$m['board'] = (typeof go_next == "undefined"?$m['go_next']:go_next)($m['board'], (typeof minimax == "undefined"?$m['minimax']:minimax)($m['board'], 3), 'R');
		$p['printFunc'](["Rondo's move:"], 1);
		(typeof printBoard == "undefined"?$m['printBoard']:printBoard)();
		$m['move']();
		return null;
	};
	$m['moveAI']['__name__'] = 'moveAI';

	$m['moveAI']['__bind_type__'] = 0;
	$m['moveAI']['__args__'] = [null,null];
	$m['movePlayer'] = function() {
		var $iter1_nextval,$iter1_type,column,$iter1_iter,$iter1_array,row,$iter1_test,$iter1_idx;
		column = $m['raw_input']('\nYour turn! Please choose a column (0-6):\n')['lower']();
		if ($p['bool'](!$p['list'](['q', '0', '1', '2', '3', '4', '5', '6'])['__contains__'](column))) {
			$m['movePlayer']();
		}
		else if ($p['bool']($p['op_eq'](column, 'q'))) {
			$m['sys']['exit']();
		}
		else {
			column = $p['float_int'](column);
			$iter1_iter = $p['range'](6);
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while ($iter1_test = typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
				row = $iter1_nextval['$nextval'];
				if ($p['bool']($p['op_eq']($m['board']['__getitem__'](column)['__getitem__'](row), '*'))) {
					$m['board']['__getitem__'](column)['__setitem__'](row, 'Y');
					$p['printFunc'](['\nYour move:'], 1);
					(typeof printBoard == "undefined"?$m['printBoard']:printBoard)();
					$m['move']();
					break;
				}
			}
			if (!$iter1_test) {
				$m['movePlayer']();
			}
		}
		return null;
	};
	$m['movePlayer']['__name__'] = 'movePlayer';

	$m['movePlayer']['__bind_type__'] = 0;
	$m['movePlayer']['__args__'] = [null,null];
	$m['printBoard'] = function() {
		var $iter2_nextval,$iter2_type,$iter2_iter,column,$iter3_nextval,$iter3_array,$iter2_idx,$iter3_idx,$iter3_iter,$iter3_type,$iter2_array,row;
		$p['printFunc'](['0 1 2 3 4 5 6'], 1);
		$iter2_iter = $p['list']([5, 4, 3, 2, 1, 0]);
		$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
		while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
			row = $iter2_nextval['$nextval'];
			$iter3_iter = $p['range'](6);
			$iter3_nextval=$p['__iter_prepare']($iter3_iter,false);
			while (typeof($p['__wrapped_next']($iter3_nextval)['$nextval']) != 'undefined') {
				column = $iter3_nextval['$nextval'];
				$p['printFunc']([$m['board']['__getitem__'](column)['__getitem__'](row)], 0);
			}
			$p['printFunc']([$m['board']['__getitem__'](6)['__getitem__'](row)], 1);
		}
		return null;
	};
	$m['printBoard']['__name__'] = 'printBoard';

	$m['printBoard']['__bind_type__'] = 0;
	$m['printBoard']['__args__'] = [null,null];
	$m['init']();
	return this;
}; /* end connectfour */


/* end module: connectfour */


/*
PYJS_DEPS: ['time', 'sys', 'evaluate', 'prototype', 'board_functions']
*/
