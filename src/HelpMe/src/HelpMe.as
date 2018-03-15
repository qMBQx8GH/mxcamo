package 
{
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;
	import lesta.api.ModBase;

	public class HelpMe extends ModBase 
	{
		private var _states:Object = {};

		override public function init():void 
		{
			super.init();
			gameAPI.data.addCallBack("HelpMe.SHOW_MENU", this.onShowMenu);
			gameAPI.data.addCallBack("HelpMe.CREATE_MENU", this.onCreateMenu);
			gameAPI.data.addCallBack("HelpMe.ADD_MENU_ITEM", this.onAddMenuItem);
			gameAPI.data.addCallBack("HelpMe.CREATE_FLAG_SET", this.onCreateFlagSet);
			gameAPI.data.addCallBack("HelpMe.ADD_FLAG_HINT", this.onAddFlagHint);
			gameAPI.data.addCallBack("HelpMe.CREATE_PERK_SET", this.onCreatePerkSet);
			gameAPI.data.addCallBack("HelpMe.ADD_PERK", this.onAddPerk);
			gameAPI.data.addCallBack("HelpMe.ADD_QR_CODE", this.onAddQrCode);
			gameAPI.data.addCallBack("HelpMe.CREATE_QR_CODE", this.onCreateQrCode);
		}
		
		override public function fini():void 
		{
			gameAPI.data.removeCallBack();
			super.fini();
		}

		private var _search:RegExp = /\&(.)/g;
		private var _replace:String = "<u>\\1</u>";
		//Instead of str.replace(/\&(.)/g, "<u>$1</u>"
		private function repl(str:String):String
		{
			var p:int;
			do {
				p = str.search("&");
				if (p >= 0) {
					str = str.substr(0, p) + "<u>" + str.substr(p + 1, 1) + "</u>" + str.substr(p + 2);
				}
			} while (p >= 0);
			return str;
		}

		private function onCreateMenu(menuId:String, title:String):void
		{
			var _menu:MyMenu = new MyMenu(gameAPI);
			_menu.addMenuItem(this.repl(title), '');
			this._states[menuId] = _menu;
		}

		private function onAddMenuItem(menuId:String, title:String, id:String):void
		{
			if (this._states[menuId]) {
				this._states[menuId].addMenuItem(this.repl(title), id);
			}
		}

		private function onShowMenu(menuId:String, show:Boolean):void
		{
			if (this._states[menuId]) {
				if (show) {
					gameAPI.stage.addChild(this._states[menuId]);
				} else {
					gameAPI.stage.removeChild(this._states[menuId]);
				}
			}
		}

		private function onCreateFlagSet(setId:String):void
		{
			var _set:Sprite = new Sprite();
			_set.mouseChildren = _set.mouseEnabled = false;
			this._states[setId] = _set;
		}

		private function onAddFlagHint(setId:String, hintType:String, col:int, row:int):void
		{
			if (this._states[setId]) {
				if (hintType == "credits") {
					this._states[setId].addChild(MyIcon.produceIcon(gameAPI, Res.getCredits(), col, row));
				} else if (hintType == "exp") {
					this._states[setId].addChild(MyIcon.produceIcon(gameAPI, Res.getExp(), col, row));
				} else if (hintType == "crew") {
					this._states[setId].addChild(MyIcon.produceIcon(gameAPI, Res.getCrew(), col, row));
				} else if (hintType == "free_exp") {
					this._states[setId].addChild(MyIcon.produceIcon(gameAPI, Res.getFreeExp(), col, row));
				} else {
					this._states[setId].addChild(MyHint.produceHint(gameAPI, col, row));
				}
			}
		}

		private function onCreatePerkSet(setId:String):void
		{
			var _set:Sprite = new Sprite();
			_set.mouseChildren = _set.mouseEnabled = false;
			this._states[setId] = _set;
		}

		private function onAddPerk(setId:String, col:int, row:int, label:String):void
		{
			if (this._states[setId]) {
				this._states[setId].addChild(
					MyPerkHint.produceHint(gameAPI, col, row, label)
				);
			}
		}

		private function onAddQrCode(setId:String, x:int, y:int, label:String):void
		{
			if (this._states[setId]) {
				this._states[setId].addChild(
					MyQrCode.produceQrCode(gameAPI, x, y, label)
				);
			}
		}

		private function onCreateQrCode(setId:String, x:int, y:int, label:String):void
		{
			var _set:Sprite = new Sprite();
			_set.mouseChildren = _set.mouseEnabled = false;
			this._states[setId] = _set;
			this._states[setId].addChild(
				MyQrCode.produceQrCode(gameAPI, x, y, label)
			);
		}
	}
}