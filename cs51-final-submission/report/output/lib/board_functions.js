/* start module: board_functions */
$pyjs['loaded_modules']['board_functions'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['board_functions']['__was_initialized__']) return $pyjs['loaded_modules']['board_functions'];
	var $m = $pyjs['loaded_modules']['board_functions'];
	$m['__repr__'] = function() { return '<module: board_functions>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'board_functions';
	$m['__name__'] = __mod_name__;
	var $iter20_nextval,$iter23_type,$mod4,$mod1,$mod3,$mod2,$iter20_array,$iter23_iter,$iter24_array,$iter24_type,$iter19_iter,$iter19_nextval,$iter20_idx,$iter24_iter,$iter24_nextval,$iter20_iter,$iter19_array,$iter19_idx,$iter23_array,$iter20_type,$iter23_nextval,$iter24_idx,$iter23_idx,$iter19_type;

	$m['COLUMNS'] = 7;
	$m['ROWS'] = 6;
	$m['copy_board'] = function(board) {
		var $iter3_idx,$iter4_nextval,$iter3_nextval,$iter3_type,$iter4_idx,y,$iter4_type,$iter3_array,$iter4_array,x,copy,$iter4_iter,$iter3_iter;
		copy = function(){
			var $iter1_nextval,$iter1_type,$collcomp1,$iter1_iter,$iter1_idx,x,$iter1_array;
	$collcomp1 = $p['list']();
		$iter1_iter = $p['range']($m['COLUMNS']);
		$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
		while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
			x = $iter1_nextval['$nextval'];
			$collcomp1['append'](function(){
				var $iter2_nextval,$iter2_type,$iter2_iter,$collcomp2,$iter2_idx,y,$iter2_array;
	$collcomp2 = $p['list']();
			$iter2_iter = $p['range']($m['ROWS']);
			$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
			while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
				y = $iter2_nextval['$nextval'];
				$collcomp2['append']('*');
			}

	return $collcomp2;}());
		}

	return $collcomp1;}();
		$iter3_iter = $p['range']($m['COLUMNS']);
		$iter3_nextval=$p['__iter_prepare']($iter3_iter,false);
		while (typeof($p['__wrapped_next']($iter3_nextval)['$nextval']) != 'undefined') {
			x = $iter3_nextval['$nextval'];
			$iter4_iter = $p['range']($m['ROWS']);
			$iter4_nextval=$p['__iter_prepare']($iter4_iter,false);
			while (typeof($p['__wrapped_next']($iter4_nextval)['$nextval']) != 'undefined') {
				y = $iter4_nextval['$nextval'];
				copy['__getitem__'](x)['__setitem__'](y, board['__getitem__'](x)['__getitem__'](y));
			}
		}
		return copy;
	};
	$m['copy_board']['__name__'] = 'copy_board';

	$m['copy_board']['__bind_type__'] = 0;
	$m['copy_board']['__args__'] = [null,null,['board']];
	$m['horizontal'] = function(board, state, length) {
		var $iter5_nextval,x,$iter6_array,$iter6_idx,$iter6_type,$iter5_array,$add2,$iter5_iter,$iter5_idx,y,$iter5_type,in_row,$add1,$iter6_iter,$iter6_nextval;
		$iter5_iter = $p['range']($m['ROWS']);
		$iter5_nextval=$p['__iter_prepare']($iter5_iter,false);
		while (typeof($p['__wrapped_next']($iter5_nextval)['$nextval']) != 'undefined') {
			y = $iter5_nextval['$nextval'];
			in_row = 0;
			$iter6_iter = $p['range']($m['COLUMNS']);
			$iter6_nextval=$p['__iter_prepare']($iter6_iter,false);
			while (typeof($p['__wrapped_next']($iter6_nextval)['$nextval']) != 'undefined') {
				x = $iter6_nextval['$nextval'];
				if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__'](y), state))) {
					in_row = $p['__op_add']($add1=in_row,$add2=1);
					if ($p['bool']($p['op_eq'](in_row, length))) {
						return true;
					}
				}
				else {
					in_row = 0;
				}
			}
		}
		return false;
	};
	$m['horizontal']['__name__'] = 'horizontal';

	$m['horizontal']['__bind_type__'] = 0;
	$m['horizontal']['__args__'] = [null,null,['board'],['state'],['length']];
	$m['vertical'] = function(board, state, length) {
		var $iter8_idx,$iter7_nextval,$iter7_iter,$iter8_type,$iter7_array,$iter8_array,$iter8_iter,$add3,$add4,$iter7_idx,y,x,in_row,$iter7_type,$iter8_nextval;
		$iter7_iter = $p['range']($m['COLUMNS']);
		$iter7_nextval=$p['__iter_prepare']($iter7_iter,false);
		while (typeof($p['__wrapped_next']($iter7_nextval)['$nextval']) != 'undefined') {
			x = $iter7_nextval['$nextval'];
			in_row = 0;
			$iter8_iter = $p['range']($m['ROWS']);
			$iter8_nextval=$p['__iter_prepare']($iter8_iter,false);
			while (typeof($p['__wrapped_next']($iter8_nextval)['$nextval']) != 'undefined') {
				y = $iter8_nextval['$nextval'];
				if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__'](y), state))) {
					in_row = $p['__op_add']($add3=in_row,$add4=1);
					if ($p['bool']($p['op_eq'](in_row, length))) {
						return true;
					}
				}
				else {
					in_row = 0;
				}
			}
		}
		return false;
	};
	$m['vertical']['__name__'] = 'vertical';

	$m['vertical']['__bind_type__'] = 0;
	$m['vertical']['__args__'] = [null,null,['board'],['state'],['length']];
	$m['diag_upright'] = function(board, state, x, y, length) {
		var $add11,$and1,$and2,$add13,$add14,$add6,$add12,$add5,in_row,$add9,$add10,$add8,$add7;
		in_row = 0;
		while ($p['bool'](($p['bool']($and1=($p['cmp'](y, $m['ROWS']) == -1))?($p['cmp'](x, $m['COLUMNS']) == -1):$and1))) {
			if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__'](y), state))) {
				in_row = $p['__op_add']($add5=in_row,$add6=1);
				if ($p['bool']($p['op_eq'](in_row, length))) {
					return true;
				}
				x = $p['__op_add']($add7=x,$add8=1);
				y = $p['__op_add']($add9=y,$add10=1);
			}
			else {
				in_row = 0;
				x = $p['__op_add']($add11=x,$add12=1);
				y = $p['__op_add']($add13=y,$add14=1);
			}
		}
		return false;
	};
	$m['diag_upright']['__name__'] = 'diag_upright';

	$m['diag_upright']['__bind_type__'] = 0;
	$m['diag_upright']['__args__'] = [null,null,['board'],['state'],['x'],['y'],['length']];
	$m['diag_downright'] = function(board, state, x, y, length) {
		var $add16,$sub3,$and3,$and4,$sub6,$add15,$add17,$sub2,in_row,$add18,$sub1,$sub5,$sub4;
		in_row = 0;
		while ($p['bool'](($p['bool']($and3=($p['cmp'](x, $m['COLUMNS']) == -1))?((($p['cmp'](y, 0))|1) == 1):$and3))) {
			if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__'](y), state))) {
				in_row = $p['__op_add']($add15=in_row,$add16=1);
				if ($p['bool']($p['op_eq'](in_row, length))) {
					return true;
				}
				x = $p['__op_add']($add17=x,$add18=1);
				y = $p['__op_sub']($sub1=y,$sub2=1);
			}
			else {
				in_row = 0;
				x = $p['__op_sub']($sub3=x,$sub4=1);
				y = $p['__op_sub']($sub5=y,$sub6=1);
			}
		}
		return false;
	};
	$m['diag_downright']['__name__'] = 'diag_downright';

	$m['diag_downright']['__bind_type__'] = 0;
	$m['diag_downright']['__args__'] = [null,null,['board'],['state'],['x'],['y'],['length']];
	$m['diagonal'] = function(board, state, length) {
		var $iter10_nextval,$or1,$iter9_iter,$iter10_idx,$or2,$iter9_nextval,$iter10_array,$iter9_array,$iter10_type,$iter9_idx,y,x,$iter10_iter,$iter9_type;
		$iter9_iter = $p['range']($m['ROWS']);
		$iter9_nextval=$p['__iter_prepare']($iter9_iter,false);
		while (typeof($p['__wrapped_next']($iter9_nextval)['$nextval']) != 'undefined') {
			y = $iter9_nextval['$nextval'];
			$iter10_iter = $p['range']($m['COLUMNS']);
			$iter10_nextval=$p['__iter_prepare']($iter10_iter,false);
			while (typeof($p['__wrapped_next']($iter10_nextval)['$nextval']) != 'undefined') {
				x = $iter10_nextval['$nextval'];
				if ($p['bool'](($p['bool']($or1=$m['diag_upright'](board, state, x, y, length))?$or1:$m['diag_downright'](board, state, x, y, length)))) {
					return true;
				}
			}
		}
		return false;
	};
	$m['diagonal']['__name__'] = 'diagonal';

	$m['diagonal']['__bind_type__'] = 0;
	$m['diagonal']['__args__'] = [null,null,['board'],['state'],['length']];
	$m['full'] = function(board) {
		var $iter11_iter,$iter12_type,$iter11_type,$iter12_array,$iter12_iter,$iter11_array,y,x,$iter11_nextval,$iter11_idx,$iter12_idx,$iter12_nextval;
		$iter11_iter = $p['range']($m['ROWS']);
		$iter11_nextval=$p['__iter_prepare']($iter11_iter,false);
		while (typeof($p['__wrapped_next']($iter11_nextval)['$nextval']) != 'undefined') {
			y = $iter11_nextval['$nextval'];
			$iter12_iter = $p['range']($m['COLUMNS']);
			$iter12_nextval=$p['__iter_prepare']($iter12_iter,false);
			while (typeof($p['__wrapped_next']($iter12_nextval)['$nextval']) != 'undefined') {
				x = $iter12_nextval['$nextval'];
				if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__'](y), '*'))) {
					return false;
				}
			}
		}
		return true;
	};
	$m['full']['__name__'] = 'full';

	$m['full']['__bind_type__'] = 0;
	$m['full']['__args__'] = [null,null,['board']];
	$m['is_terminal'] = function(board, turn) {
		var $or5,$or4,$or6,$or3;
		if ($p['bool'](($p['bool']($or3=$m['horizontal'](board, turn, 4))?$or3:($p['bool']($or4=$m['vertical'](board, turn, 4))?$or4:($p['bool']($or5=$m['diagonal'](board, turn, 4))?$or5:$m['full'](board)))))) {
			return true;
		}
		else {
			return false;
		}
		return null;
	};
	$m['is_terminal']['__name__'] = 'is_terminal';

	$m['is_terminal']['__bind_type__'] = 0;
	$m['is_terminal']['__args__'] = [null,null,['board'],['turn']];
	$m['game_won'] = function(board, turn) {
		var $or7,$or9,$or8;
		if ($p['bool'](($p['bool']($or7=$m['horizontal'](board, turn, 4))?$or7:($p['bool']($or8=$m['vertical'](board, turn, 4))?$or8:$m['diagonal'](board, turn, 4))))) {
			return true;
		}
		else {
			return false;
		}
		return null;
	};
	$m['game_won']['__name__'] = 'game_won';

	$m['game_won']['__bind_type__'] = 0;
	$m['game_won']['__args__'] = [null,null,['board'],['turn']];
	$m['in_row'] = function(board, turn, length) {
		var $or11,$or12,$or10;
		if ($p['bool'](($p['bool']($or10=$m['horizontal'](board, turn, length))?$or10:($p['bool']($or11=$m['vertical'](board, turn, length))?$or11:$m['diagonal'](board, turn, length))))) {
			return true;
		}
		else {
			return false;
		}
		return null;
	};
	$m['in_row']['__name__'] = 'in_row';

	$m['in_row']['__bind_type__'] = 0;
	$m['in_row']['__args__'] = [null,null,['board'],['turn'],['length']];
	$m['possible_moves'] = function(board) {
		var $iter13_nextval,$iter13_iter,$iter13_array,$sub8,x,moves,$sub7,$iter13_type,$iter13_idx;
		moves = $p['list']([]);
		$iter13_iter = $p['range']($m['COLUMNS']);
		$iter13_nextval=$p['__iter_prepare']($iter13_iter,false);
		while (typeof($p['__wrapped_next']($iter13_nextval)['$nextval']) != 'undefined') {
			x = $iter13_nextval['$nextval'];
			if ($p['bool']($p['op_eq'](board['__getitem__'](x)['__getitem__']($p['__op_sub']($sub7=$m['ROWS'],$sub8=1)), '*'))) {
				moves['append'](x);
			}
		}
		return moves;
	};
	$m['possible_moves']['__name__'] = 'possible_moves';

	$m['possible_moves']['__bind_type__'] = 0;
	$m['possible_moves']['__args__'] = [null,null,['board']];
	$m['go_next'] = function(board, move, state) {
		var $iter14_array,$iter14_type,board1,$iter14_iter,y,$iter14_idx,$iter14_nextval;
		board1 = $m['copy_board'](board);
		$iter14_iter = $p['range']($m['ROWS']);
		$iter14_nextval=$p['__iter_prepare']($iter14_iter,false);
		while (typeof($p['__wrapped_next']($iter14_nextval)['$nextval']) != 'undefined') {
			y = $iter14_nextval['$nextval'];
			if ($p['bool']($p['op_eq'](board1['__getitem__'](move)['__getitem__'](y), '*'))) {
				board1['__getitem__'](move)['__setitem__'](y, state);
				return board1;
			}
		}
		return null;
	};
	$m['go_next']['__name__'] = 'go_next';

	$m['go_next']['__bind_type__'] = 0;
	$m['go_next']['__args__'] = [null,null,['board'],['move'],['state']];
	$m['board0'] = function(){
		var $iter15_iter,$iter15_array,$collcomp3,$iter15_idx,$iter15_nextval,$iter15_type;
	$collcomp3 = $p['list']();
	$iter15_iter = $p['range']($m['COLUMNS']);
	$iter15_nextval=$p['__iter_prepare']($iter15_iter,false);
	while (typeof($p['__wrapped_next']($iter15_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter15_nextval['$nextval'];
		$collcomp3['append'](function(){
			var $iter16_array,$iter16_type,$collcomp4,$iter16_idx,$iter16_nextval,$iter16_iter;
	$collcomp4 = $p['list']();
		$iter16_iter = $p['range']($m['ROWS']);
		$iter16_nextval=$p['__iter_prepare']($iter16_iter,false);
		while (typeof($p['__wrapped_next']($iter16_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter16_nextval['$nextval'];
			$collcomp4['append']('*');
		}

	return $collcomp4;}());
	}

	return $collcomp3;}();
	$m['hor_board'] = function(){
		var $iter17_nextval,$iter17_iter,$collcomp5,$iter17_array,$iter17_idx,$iter17_type;
	$collcomp5 = $p['list']();
	$iter17_iter = $p['range']($m['COLUMNS']);
	$iter17_nextval=$p['__iter_prepare']($iter17_iter,false);
	while (typeof($p['__wrapped_next']($iter17_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter17_nextval['$nextval'];
		$collcomp5['append'](function(){
			var $iter18_type,$iter18_iter,$iter18_array,$collcomp6,$iter18_idx,$iter18_nextval;
	$collcomp6 = $p['list']();
		$iter18_iter = $p['range']($m['ROWS']);
		$iter18_nextval=$p['__iter_prepare']($iter18_iter,false);
		while (typeof($p['__wrapped_next']($iter18_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter18_nextval['$nextval'];
			$collcomp6['append']('*');
		}

	return $collcomp6;}());
	}

	return $collcomp5;}();
	$iter19_iter = $p['range']($m['ROWS']);
	$iter19_nextval=$p['__iter_prepare']($iter19_iter,false);
	while (typeof($p['__wrapped_next']($iter19_nextval)['$nextval']) != 'undefined') {
		$m['y'] = $iter19_nextval['$nextval'];
		$iter20_iter = $p['range']($m['COLUMNS']);
		$iter20_nextval=$p['__iter_prepare']($iter20_iter,false);
		while (typeof($p['__wrapped_next']($iter20_nextval)['$nextval']) != 'undefined') {
			$m['x'] = $iter20_nextval['$nextval'];
			if ($p['bool']($p['op_eq']((typeof ($mod1=$m['y'])==typeof ($mod2=2) && typeof $mod1=='number'?
				(($mod1=$mod1%$mod2)<0&&$mod2>0?$mod1+$mod2:$mod1):
				$p['op_mod']($mod1,$mod2)), 0))) {
				$m['hor_board']['__getitem__']($m['x'])['__setitem__']($m['y'], 'R');
			}
			else {
				$m['hor_board']['__getitem__']($m['x'])['__setitem__']($m['y'], 'Y');
			}
		}
	}
	$m['vert_board'] = function(){
		var $iter21_idx,$collcomp7,$iter21_nextval,$iter21_type,$iter21_iter,$iter21_array;
	$collcomp7 = $p['list']();
	$iter21_iter = $p['range']($m['COLUMNS']);
	$iter21_nextval=$p['__iter_prepare']($iter21_iter,false);
	while (typeof($p['__wrapped_next']($iter21_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter21_nextval['$nextval'];
		$collcomp7['append'](function(){
			var $iter22_array,$collcomp8,$iter22_nextval,$iter22_idx,$iter22_type,$iter22_iter;
	$collcomp8 = $p['list']();
		$iter22_iter = $p['range']($m['ROWS']);
		$iter22_nextval=$p['__iter_prepare']($iter22_iter,false);
		while (typeof($p['__wrapped_next']($iter22_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter22_nextval['$nextval'];
			$collcomp8['append']('*');
		}

	return $collcomp8;}());
	}

	return $collcomp7;}();
	$iter23_iter = $p['range']($m['COLUMNS']);
	$iter23_nextval=$p['__iter_prepare']($iter23_iter,false);
	while (typeof($p['__wrapped_next']($iter23_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter23_nextval['$nextval'];
		$iter24_iter = $p['range']($m['ROWS']);
		$iter24_nextval=$p['__iter_prepare']($iter24_iter,false);
		while (typeof($p['__wrapped_next']($iter24_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter24_nextval['$nextval'];
			if ($p['bool']($p['op_eq']((typeof ($mod3=$m['x'])==typeof ($mod4=2) && typeof $mod3=='number'?
				(($mod3=$mod3%$mod4)<0&&$mod4>0?$mod3+$mod4:$mod3):
				$p['op_mod']($mod3,$mod4)), 0))) {
				$m['vert_board']['__getitem__']($m['x'])['__setitem__']($m['y'], 'R');
			}
			else {
				$m['vert_board']['__getitem__']($m['x'])['__setitem__']($m['y'], 'Y');
			}
		}
	}
	$m['diag1_board'] = function(){
		var $collcomp9,$iter25_nextval,$iter25_array,$iter25_iter,$iter25_idx,$iter25_type;
	$collcomp9 = $p['list']();
	$iter25_iter = $p['range']($m['COLUMNS']);
	$iter25_nextval=$p['__iter_prepare']($iter25_iter,false);
	while (typeof($p['__wrapped_next']($iter25_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter25_nextval['$nextval'];
		$collcomp9['append'](function(){
			var $iter26_idx,$iter26_nextval,$iter26_type,$collcomp10,$iter26_array,$iter26_iter;
	$collcomp10 = $p['list']();
		$iter26_iter = $p['range']($m['ROWS']);
		$iter26_nextval=$p['__iter_prepare']($iter26_iter,false);
		while (typeof($p['__wrapped_next']($iter26_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter26_nextval['$nextval'];
			$collcomp10['append']('*');
		}

	return $collcomp10;}());
	}

	return $collcomp9;}();
	$m['diag1_board']['__getitem__'](2)['__setitem__'](2, 'R');
	$m['diag1_board']['__getitem__'](3)['__setitem__'](3, 'R');
	$m['diag1_board']['__getitem__'](4)['__setitem__'](4, 'R');
	$m['diag1_board']['__getitem__'](5)['__setitem__'](5, 'R');
	$m['diag2_board'] = function(){
		var $iter27_nextval,$iter27_array,$iter27_idx,$iter27_iter,$collcomp11,$iter27_type;
	$collcomp11 = $p['list']();
	$iter27_iter = $p['range']($m['COLUMNS']);
	$iter27_nextval=$p['__iter_prepare']($iter27_iter,false);
	while (typeof($p['__wrapped_next']($iter27_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter27_nextval['$nextval'];
		$collcomp11['append'](function(){
			var $iter28_array,$iter28_nextval,$iter28_idx,$collcomp12,$iter28_iter,$iter28_type;
	$collcomp12 = $p['list']();
		$iter28_iter = $p['range']($m['ROWS']);
		$iter28_nextval=$p['__iter_prepare']($iter28_iter,false);
		while (typeof($p['__wrapped_next']($iter28_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter28_nextval['$nextval'];
			$collcomp12['append']('*');
		}

	return $collcomp12;}());
	}

	return $collcomp11;}();
	$m['diag2_board']['__getitem__'](2)['__setitem__'](5, 'R');
	$m['diag2_board']['__getitem__'](3)['__setitem__'](4, 'R');
	$m['diag2_board']['__getitem__'](4)['__setitem__'](3, 'R');
	$m['diag2_board']['__getitem__'](5)['__setitem__'](2, 'R');
	$m['insert_board'] = function(){
		var $iter29_type,$iter29_iter,$iter29_nextval,$collcomp13,$iter29_idx,$iter29_array;
	$collcomp13 = $p['list']();
	$iter29_iter = $p['range']($m['COLUMNS']);
	$iter29_nextval=$p['__iter_prepare']($iter29_iter,false);
	while (typeof($p['__wrapped_next']($iter29_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter29_nextval['$nextval'];
		$collcomp13['append'](function(){
			var $iter30_type,$iter30_nextval,$iter30_iter,$collcomp14,$iter30_idx,$iter30_array;
	$collcomp14 = $p['list']();
		$iter30_iter = $p['range']($m['ROWS']);
		$iter30_nextval=$p['__iter_prepare']($iter30_iter,false);
		while (typeof($p['__wrapped_next']($iter30_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter30_nextval['$nextval'];
			$collcomp14['append']('*');
		}

	return $collcomp14;}());
	}

	return $collcomp13;}();
	$m['insert_board']['__getitem__'](0)['__setitem__'](0, 'R');
	$m['insert_board']['__getitem__'](1)['__setitem__'](0, 'R');
	$m['insert_board']['__getitem__'](2)['__setitem__'](0, 'R');
	if ($p['bool'](!$p['op_eq']($m['is_terminal']($m['board0'], 'R'), false))) {
		$p['printFunc'](['failure0'], 1);
	}
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['hor_board'], 'R'), false))) {
		$p['printFunc'](['failure0.5'], 1);
	}
	if ($p['bool']($m['horizontal']($m['vert_board'], 'R', 4))) {
		$p['printFunc'](['failure1'], 1);
	}
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['vert_board'], 'R'), false))) {
		$p['printFunc'](['failure1.5'], 1);
	}
	if ($p['bool']($m['vertical']($m['hor_board'], 'R', 4))) {
		$p['printFunc'](['failure2'], 1);
	}
	if ($p['bool']($m['diagonal']($m['vert_board'], 'R', 4))) {
		$p['printFunc'](['failure3'], 1);
	}
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['diag1_board'], 'R'), false))) {
		$p['printFunc'](['failure3.5'], 1);
	}
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['diag2_board'], 'R'), false))) {
		$p['printFunc'](['failure4'], 1);
	}
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['hor_board'], 'R'), false))) {
		$p['printFunc'](['failure5'], 1);
	}
	$m['moves1'] = $m['possible_moves']($m['board0']);
	$m['moves2'] = $m['possible_moves']($m['hor_board']);
	$m['go_board'] = $m['go_next']($m['insert_board'], 3, 'R');
	if ($p['bool']($p['op_eq']($m['is_terminal']($m['go_board'], 'R'), false))) {
		$p['printFunc'](['failure6'], 1);
	}
	$m['dummy'] = function() {

		$p['printFunc'](['hey!'], 1);
		return null;
	};
	$m['dummy']['__name__'] = 'dummy';

	$m['dummy']['__bind_type__'] = 0;
	$m['dummy']['__args__'] = [null,null];
	$m['empty'] = function(){
		var $iter31_array,$iter31_nextval,$iter31_idx,$collcomp15,$iter31_type,$iter31_iter;
	$collcomp15 = $p['list']();
	$iter31_iter = $p['range']($m['COLUMNS']);
	$iter31_nextval=$p['__iter_prepare']($iter31_iter,false);
	while (typeof($p['__wrapped_next']($iter31_nextval)['$nextval']) != 'undefined') {
		$m['x'] = $iter31_nextval['$nextval'];
		$collcomp15['append'](function(){
			var $iter32_idx,$iter32_nextval,$iter32_type,$collcomp16,$iter32_iter,$iter32_array;
	$collcomp16 = $p['list']();
		$iter32_iter = $p['range']($m['ROWS']);
		$iter32_nextval=$p['__iter_prepare']($iter32_iter,false);
		while (typeof($p['__wrapped_next']($iter32_nextval)['$nextval']) != 'undefined') {
			$m['y'] = $iter32_nextval['$nextval'];
			$collcomp16['append']('*');
		}

	return $collcomp16;}());
	}

	return $collcomp15;}();
	$m['moved'] = $m['go_next']($m['empty'], 1, 'R');
	return this;
}; /* end board_functions */


/* end module: board_functions */


