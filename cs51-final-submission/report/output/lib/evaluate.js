/* start module: evaluate */
$pyjs['loaded_modules']['evaluate'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['evaluate']['__was_initialized__']) return $pyjs['loaded_modules']['evaluate'];
	var $m = $pyjs['loaded_modules']['evaluate'];
	$m['__repr__'] = function() { return '<module: evaluate>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'evaluate';
	$m['__name__'] = __mod_name__;


	$p['__import_all__']('board_functions', null, $m, null, false);
	$m['evaluate'] = function(board) {

		if ($p['bool']((typeof game_won == "undefined"?$m['game_won']:game_won)(board, 'R'))) {
			return $p['float']('inf');
		}
		else if ($p['bool']((typeof game_won == "undefined"?$m['game_won']:game_won)(board, 'Y'))) {
			return $p['float']('-inf');
		}
		else if ($p['bool']((typeof full == "undefined"?$m['full']:full)(board))) {
			return 0;
		}
		else {
			if ($p['bool']((typeof in_row == "undefined"?$m['in_row']:in_row)(board, 'Y', 3))) {
				return (typeof ($usub1=10)=='number'?
					-$usub1:
					$p['op_usub']($usub1));
			}
			else {
				return 5;
			}
		}
		return null;
	};
	$m['evaluate']['__name__'] = 'evaluate';

	$m['evaluate']['__bind_type__'] = 0;
	$m['evaluate']['__args__'] = [null,null,['board']];
	return this;
}; /* end evaluate */


/* end module: evaluate */


/*
PYJS_DEPS: ['board_functions']
*/
