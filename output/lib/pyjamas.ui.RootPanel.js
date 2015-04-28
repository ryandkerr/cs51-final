/* start module: pyjamas.ui.RootPanel */
$pyjs['loaded_modules']['pyjamas.ui.RootPanel'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['pyjamas.ui.RootPanel']['__was_initialized__']) return $pyjs['loaded_modules']['pyjamas.ui.RootPanel'];
	if(typeof $pyjs['loaded_modules']['pyjamas.ui'] == 'undefined' || !$pyjs['loaded_modules']['pyjamas.ui']['__was_initialized__']) $p['___import___']('pyjamas.ui', null);
	var $m = $pyjs['loaded_modules']['pyjamas.ui.RootPanel'];
	$m['__repr__'] = function() { return '<module: pyjamas.ui.RootPanel>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'pyjamas.ui.RootPanel';
	$m['__name__'] = __mod_name__;
	$pyjs['loaded_modules']['pyjamas.ui']['RootPanel'] = $pyjs['loaded_modules']['pyjamas.ui.RootPanel'];


	$m['sys'] = $p['___import___']('sys', 'pyjamas.ui');
	$m['Factory'] = $p['___import___']('pyjamas.Factory', 'pyjamas.ui', null, false);
	$m['DOM'] = $p['___import___']('pyjamas.DOM', 'pyjamas.ui', null, false);
	$m['Window'] = $p['___import___']('pyjamas.Window', 'pyjamas.ui', null, false);
	$m['AbsolutePanel'] = $p['___import___']('pyjamas.ui.AbsolutePanel.AbsolutePanel', 'pyjamas.ui', null, false);
	$m['rootPanels'] = $p['dict']([]);
	$m['RootPanelManager'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'pyjamas.ui.RootPanel';
		$method = $pyjs__bind_method2('onWindowClosed', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $iter1_nextval,$iter1_type,$iter1_idx,$iter1_iter,$iter1_array,panel;
			$iter1_iter = $m['rootPanels']['itervalues']();
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
				panel = $iter1_nextval['$nextval'];
				panel['onDetach']();
			}
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onWindowClosed'] = $method;
		$method = $pyjs__bind_method2('onWindowClosing', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onWindowClosing'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('RootPanelManager', $p['tuple']($bases), $data);
	})();
	$m['get'] = function(id) {
		if (typeof id == 'undefined') id=arguments['callee']['__args__'][2][1];
		var element;
		if ($p['bool']($m['rootPanels']['has_key'](id))) {
			return $m['rootPanels']['__getitem__'](id);
		}
		element = null;
		if ($p['bool']((id !== null))) {
			element = $m['DOM']['getElementById'](id);
			if ($p['bool']((element === null))) {
				return null;
			}
		}
		return (typeof manageRootPanel == "undefined"?$m['manageRootPanel']:manageRootPanel)((typeof RootPanelCls == "undefined"?$m['RootPanelCls']:RootPanelCls)(element), id);
	};
	$m['get']['__name__'] = 'get';

	$m['get']['__bind_type__'] = 0;
	$m['get']['__args__'] = [null,null,['id', null]];
	$m['manageRootPanel'] = function(panel, id) {
		if (typeof id == 'undefined') id=arguments['callee']['__args__'][3][1];
		var panelManager;
		if ($p['bool'](($p['cmp']($p['len']($m['rootPanels']), 1) == -1))) {
			panelManager = $m['RootPanelManager']();
			$m['Window']['addWindowCloseListener'](panelManager);
		}
		$m['rootPanels']['__setitem__'](id, panel);
		return panel;
	};
	$m['manageRootPanel']['__name__'] = 'manageRootPanel';

	$m['manageRootPanel']['__bind_type__'] = 0;
	$m['manageRootPanel']['__args__'] = [null,null,['panel'],['id', null]];
	$m['RootPanelCls'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'pyjamas.ui.RootPanel';
		$method = $pyjs__bind_method2('__init__', function(Element) {
			if (this['__is_instance__'] === true) {
				var self = this;
				var kwargs = arguments['length'] >= 2 ? arguments[arguments['length']-1] : arguments[arguments['length']];
				if (kwargs === null || typeof kwargs != 'object' || kwargs['__name__'] != 'dict' || typeof kwargs['$pyjs_is_kwarg'] == 'undefined') {
					var kwargs = arguments[arguments['length']+1];
				} else {
					delete kwargs['$pyjs_is_kwarg'];
				}
			} else {
				var self = arguments[0];
				Element = arguments[1];
				var kwargs = arguments['length'] >= 3 ? arguments[arguments['length']-1] : arguments[arguments['length']];
				if (kwargs === null || typeof kwargs != 'object' || kwargs['__name__'] != 'dict' || typeof kwargs['$pyjs_is_kwarg'] == 'undefined') {
					kwargs = arguments[arguments['length']+1];
				} else {
					delete kwargs['$pyjs_is_kwarg'];
				}
			}
			if (typeof kwargs == 'undefined') {
				kwargs = $p['__empty_dict']();
				if (typeof Element != 'undefined') {
					if (Element !== null && typeof Element['$pyjs_is_kwarg'] != 'undefined') {
						kwargs = Element;
						Element = arguments[2];
					}
				} else 				if (typeof self != 'undefined') {
					if (self !== null && typeof self['$pyjs_is_kwarg'] != 'undefined') {
						kwargs = self;
						self = arguments[2];
					}
				} else {
				}
			}
			if (typeof Element == 'undefined') Element=arguments['callee']['__args__'][3][1];

			if ($p['bool']((Element !== null))) {
				kwargs['__setitem__']('Element', Element);
			}
			$pyjs_kwargs_call($m['AbsolutePanel'], '__init__', null, kwargs, [{}, self]);
			if ($p['bool']((Element === null))) {
				Element = self['getBodyElement']();
				self['setElement'](Element);
			}
			self['onAttach']();
			return null;
		}
	, 1, [null,['kwargs'],['self'],['Element', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getBodyElement', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return $p['getattr']($doc, 'body');
		}
	, 1, [null,null,['self']]);
		$cls_definition['getBodyElement'] = $method;
		var $bases = new Array($m['AbsolutePanel']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('RootPanelCls', $p['tuple']($bases), $data);
	})();
	$m['Factory']['registerClass']('pyjamas.ui.RootPanel', 'RootPanelCls', $m['RootPanelCls']);
	$m['RootPanel'] = function(id) {
		if (typeof id == 'undefined') id=arguments['callee']['__args__'][2][1];

		return $m['get'](id);
	};
	$m['RootPanel']['__name__'] = 'RootPanel';

	$m['RootPanel']['__bind_type__'] = 0;
	$m['RootPanel']['__args__'] = [null,null,['id', null]];
	return this;
}; /* end pyjamas.ui.RootPanel */


/* end module: pyjamas.ui.RootPanel */


/*
PYJS_DEPS: ['sys', 'pyjamas.Factory', 'pyjamas', 'pyjamas.DOM', 'pyjamas.Window', 'pyjamas.ui.AbsolutePanel.AbsolutePanel', 'pyjamas.ui', 'pyjamas.ui.AbsolutePanel']
*/
