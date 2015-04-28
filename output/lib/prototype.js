/* start module: prototype */
$pyjs['loaded_modules']['prototype'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['prototype']['__was_initialized__']) return $pyjs['loaded_modules']['prototype'];
	var $m = $pyjs['loaded_modules']['prototype'];
	$m['__repr__'] = function() { return '<module: prototype>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'prototype';
	$m['__name__'] = __mod_name__;


	$p['__import_all__']('board_functions', null, $m, null, false);
	$p['__import_all__']('evaluate', null, $m, null, false);
	$m['minimax'] = function(board, depth) {
		var $iter1_nextval,$iter1_type,$iter1_idx,board_score,new_board,move,$mod2,next_moves,$iter1_iter,$add2,$add1,$mod1,best_move,$sub2,$sub1,best_score,$iter1_array;
		next_moves = (typeof possible_moves == "undefined"?$m['possible_moves']:possible_moves)(board);
		best_move = next_moves['__getitem__'](3);
		best_score = $p['float']('-inf');
		$iter1_iter = next_moves;
		$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
		while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
			move = $iter1_nextval['$nextval'];
			new_board = (typeof go_next == "undefined"?$m['go_next']:go_next)(board, move, 'R');
			board_score = $p['__op_add']($add1=(typeof min_player == "undefined"?$m['min_player']:min_player)(new_board, $p['__op_sub']($sub1=depth,$sub2=1)),$add2=(typeof ($mod1=move)==typeof ($mod2=4) && typeof $mod1=='number'?
				(($mod1=$mod1%$mod2)<0&&$mod2>0?$mod1+$mod2:$mod1):
				$p['op_mod']($mod1,$mod2)));
			if ($p['bool'](($p['cmp'](board_score, best_score) == 1))) {
				best_score = board_score;
				best_move = move;
			}
		}
		return best_move;
	};
	$m['minimax']['__name__'] = 'minimax';

	$m['minimax']['__bind_type__'] = 0;
	$m['minimax']['__args__'] = [null,null,['board'],['depth']];
	$m['min_player'] = function(board, depth) {
		var min_score,$iter2_nextval,$iter2_type,$iter2_iter,new_board,move,$iter2_idx,next_moves,board_score,$sub3,$iter2_array,$sub4;
		if ($p['bool']((typeof is_terminal == "undefined"?$m['is_terminal']:is_terminal)(board, 'R'))) {
			return $m['evaluate'](board);
		}
		else {
			next_moves = (typeof possible_moves == "undefined"?$m['possible_moves']:possible_moves)(board);
			min_score = $p['float']('inf');
			$iter2_iter = next_moves;
			$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
			while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
				move = $iter2_nextval['$nextval'];
				new_board = (typeof go_next == "undefined"?$m['go_next']:go_next)(board, move, 'Y');
				board_score = 0;
				if ($p['bool']($p['op_eq'](depth, 0))) {
					board_score = $m['evaluate'](new_board);
				}
				else {
					board_score = (typeof max_player == "undefined"?$m['max_player']:max_player)(new_board, $p['__op_sub']($sub3=depth,$sub4=1));
				}
				if ($p['bool'](($p['cmp'](board_score, min_score) == -1))) {
					min_score = board_score;
				}
			}
			return min_score;
		}
		return null;
	};
	$m['min_player']['__name__'] = 'min_player';

	$m['min_player']['__bind_type__'] = 0;
	$m['min_player']['__args__'] = [null,null,['board'],['depth']];
	$m['max_player'] = function(board, depth) {
		var move,$iter3_idx,$iter3_nextval,$iter3_array,next_moves,$sub6,board_score,$iter3_type,max_score,new_board,$sub5,$iter3_iter;
		if ($p['bool']((typeof is_terminal == "undefined"?$m['is_terminal']:is_terminal)(board, 'Y'))) {
			return $m['evaluate'](board);
		}
		else {
			next_moves = (typeof possible_moves == "undefined"?$m['possible_moves']:possible_moves)(board);
			max_score = $p['float']('-inf');
			$iter3_iter = next_moves;
			$iter3_nextval=$p['__iter_prepare']($iter3_iter,false);
			while (typeof($p['__wrapped_next']($iter3_nextval)['$nextval']) != 'undefined') {
				move = $iter3_nextval['$nextval'];
				new_board = (typeof go_next == "undefined"?$m['go_next']:go_next)(board, move, 'R');
				board_score = 0;
				if ($p['bool']($p['op_eq'](depth, 0))) {
					board_score = $m['evaluate'](new_board);
				}
				else {
					board_score = $m['min_player'](new_board, $p['__op_sub']($sub5=depth,$sub6=1));
				}
				if ($p['bool'](($p['cmp'](board_score, max_score) == 1))) {
					max_score = board_score;
				}
			}
			return max_score;
		}
		return null;
	};
	$m['max_player']['__name__'] = 'max_player';

	$m['max_player']['__bind_type__'] = 0;
	$m['max_player']['__args__'] = [null,null,['board'],['depth']];
	return this;
}; /* end prototype */


/* end module: prototype */


/*
PYJS_DEPS: ['board_functions', 'evaluate']
*/
