/* start module: index */
$pyjs['loaded_modules']['index'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['index']['__was_initialized__']) return $pyjs['loaded_modules']['index'];
	var $m = $pyjs['loaded_modules']['index'];
	$m['__repr__'] = function() { return '<module: index>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'index';
	$m['__name__'] = __mod_name__;


	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['HTML'] = $p['___import___']('pyjamas.ui.HTML.HTML', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['Window'] = $p['___import___']('pyjamas.Window', null, null, false);
	$m['greet'] = function(fred) {

		fred['setText']('No, really click me!');
		$m['Window']['alert']('Hello, AJAX!');
		return null;
	};
	$m['greet']['__name__'] = 'greet';

	$m['greet']['__bind_type__'] = 0;
	$m['greet']['__args__'] = [null,null,['fred']];
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m['__name__']:__name__), '__main__'))) {
		$m['pyjd']['setup']('public/Hello.html?fred=foo#me');
		$m['b'] = $pyjs_kwargs_call(null, $m['Button'], null, null, [{'StyleName':'teststyle'}, 'Click me', $m['greet']]);
		$m['h'] = $pyjs_kwargs_call(null, $m['HTML'], null, null, [{'StyleName':'teststyle'}, '<b>Hello World</b> (html)']);
		$m['l'] = $pyjs_kwargs_call(null, $m['Label'], null, null, [{'StyleName':'teststyle'}, 'Hello World (label)']);
		$m['base'] = $pyjs_kwargs_call(null, $m['HTML'], null, null, [{'StyleName':'teststyle'}, $p['sprintf']('Hello from %s', $m['pygwt']['getModuleBaseURL']())]);
		$m['RootPanel']()['add']($m['b']);
		$m['RootPanel']()['add']($m['h']);
		$m['RootPanel']()['add']($m['l']);
		$m['RootPanel']()['add']($m['base']);
		$m['pyjd']['run']();
	}
	return this;
}; /* end index */


/* end module: index */


/*
PYJS_DEPS: ['pyjd', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.HTML.HTML', 'pyjamas.ui.HTML', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.Window']
*/
