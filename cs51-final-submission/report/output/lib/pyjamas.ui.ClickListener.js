/* start module: pyjamas.ui.ClickListener */
$pyjs['loaded_modules']['pyjamas.ui.ClickListener'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['pyjamas.ui.ClickListener']['__was_initialized__']) return $pyjs['loaded_modules']['pyjamas.ui.ClickListener'];
	if(typeof $pyjs['loaded_modules']['pyjamas.ui'] == 'undefined' || !$pyjs['loaded_modules']['pyjamas.ui']['__was_initialized__']) $p['___import___']('pyjamas.ui', null);
	var $m = $pyjs['loaded_modules']['pyjamas.ui.ClickListener'];
	$m['__repr__'] = function() { return '<module: pyjamas.ui.ClickListener>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'pyjamas.ui.ClickListener';
	$m['__name__'] = __mod_name__;
	$pyjs['loaded_modules']['pyjamas.ui']['ClickListener'] = $pyjs['loaded_modules']['pyjamas.ui.ClickListener'];


	$m['DOM'] = $p['___import___']('pyjamas.DOM', 'pyjamas.ui', null, false);
	$m['Event'] = $p['___import___']('pyjamas.ui.Event', 'pyjamas.ui', null, false);
	$m['ClickHandler'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'pyjamas.ui.ClickListener';
		$method = $pyjs__bind_method2('__init__', function(preventDefault) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				preventDefault = arguments[1];
			}
			if (typeof preventDefault == 'undefined') preventDefault=arguments['callee']['__args__'][3][1];

			self['_clickListeners'] = $p['list']([]);
			self['_doubleclickListeners'] = $p['list']([]);
			self['_clickPreventDefault'] = preventDefault;
			self['sinkEvents']($p['getattr']($m['Event'], 'ONCLICK'));
			self['sinkEvents']($p['getattr']($m['Event'], 'ONDBLCLICK'));
			return null;
		}
	, 1, [null,null,['self'],['preventDefault', false]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onClick', function(sender) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}
			if (typeof sender == 'undefined') sender=arguments['callee']['__args__'][3][1];

 			return null;
		}
	, 1, [null,null,['self'],['sender', null]]);
		$cls_definition['onClick'] = $method;
		$method = $pyjs__bind_method2('onDoubleClick', function(sender) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}
			if (typeof sender == 'undefined') sender=arguments['callee']['__args__'][3][1];

 			return null;
		}
	, 1, [null,null,['self'],['sender', null]]);
		$cls_definition['onDoubleClick'] = $method;
		$method = $pyjs__bind_method2('addDoubleClickListener', function(listener) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				listener = arguments[1];
			}

			self['_doubleclickListeners']['append'](listener);
			return null;
		}
	, 1, [null,null,['self'],['listener']]);
		$cls_definition['addDoubleClickListener'] = $method;
		$method = $pyjs__bind_method2('addClickListener', function(listener) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				listener = arguments[1];
			}
			var stylename;
			stylename = self['getStyleName']();
			if ($p['bool'](stylename)) {
				self['addStyleName']($p['sprintf']('%s-clickable', stylename['$$split']()['__getitem__'](0)));
			}
			self['_clickListeners']['append'](listener);
			return null;
		}
	, 1, [null,null,['self'],['listener']]);
		$cls_definition['addClickListener'] = $method;
		$method = $pyjs__bind_method2('onBrowserEvent', function(event) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}
			var $iter2_nextval,$iter1_nextval,$iter1_type,$iter2_iter,$iter1_iter,listener,$iter2_idx,$iter1_array,$iter2_type,type,$iter2_array,$iter1_idx;
			type = $m['DOM']['eventGetType'](event);
			if ($p['bool']($p['op_eq'](type, 'click'))) {
				if ($p['bool']($p['getattr'](self, '_clickPreventDefault'))) {
					$m['DOM']['eventPreventDefault'](event);
				}
				$iter1_iter = $p['getattr'](self, '_clickListeners');
				$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
				while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
					listener = $iter1_nextval['$nextval'];
					if ($p['bool']($p['hasattr'](listener, 'onClick'))) {
						listener['onClick'](self);
					}
					else {
						listener(self);
					}
				}
			}
			else if ($p['bool']($p['op_eq'](type, 'dblclick'))) {
				if ($p['bool']($p['getattr'](self, '_clickPreventDefault'))) {
					$m['DOM']['eventPreventDefault'](event);
				}
				$iter2_iter = $p['getattr'](self, '_doubleclickListeners');
				$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
				while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
					listener = $iter2_nextval['$nextval'];
					if ($p['bool']($p['hasattr'](listener, 'onDoubleClick'))) {
						listener['onDoubleClick'](self);
					}
					else {
						listener(self);
					}
				}
			}
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['onBrowserEvent'] = $method;
		$method = $pyjs__bind_method2('removeClickListener', function(listener) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				listener = arguments[1];
			}

			self['_clickListeners']['remove'](listener);
			return null;
		}
	, 1, [null,null,['self'],['listener']]);
		$cls_definition['removeClickListener'] = $method;
		$method = $pyjs__bind_method2('removeDoubleClickListener', function(listener) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				listener = arguments[1];
			}

			self['_doubleclickListeners']['remove'](listener);
			return null;
		}
	, 1, [null,null,['self'],['listener']]);
		$cls_definition['removeDoubleClickListener'] = $method;
		$method = $pyjs__bind_method2('clearClickListener', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['__setslice']($p['getattr'](self, '_clickListeners'), 0, null, $p['list']([]));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clearClickListener'] = $method;
		$method = $pyjs__bind_method2('clearDoubleClickListener', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['__setslice'](self['_doubleclickListeners']['remove']((typeof listener == "undefined"?$m['listener']:listener)), 0, null, $p['list']([]));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clearDoubleClickListener'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('ClickHandler', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end pyjamas.ui.ClickListener */


/* end module: pyjamas.ui.ClickListener */


/*
PYJS_DEPS: ['pyjamas.DOM', 'pyjamas', 'pyjamas.ui.Event', 'pyjamas.ui']
*/
