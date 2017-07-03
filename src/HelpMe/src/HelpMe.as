package 
{
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;
	import lesta.api.ModBase;

	public class HelpMe extends ModBase 
	{
		private static const SHOW_PERK_MENU:String = "HelpMe.showPerkMenu";
		private var _states:Object = {};

		override public function init():void 
		{
			super.init();
			createWindow();
		}
		
		override public function fini():void 
		{
			gameAPI.data.removeCallBack();
			super.fini();
		}

		private function createWindow():void
		{
			var perks:Object = {
				CV: {
					JP: [
						[3, 0, "1"],
						[3, 1, "2"],
						[2, 2, "3"],
						[3, 3, "4"]
					],
					US: [
						[3, 0, "1"],
						[3, 1, "2"],
						[2, 2, "3"],
						[3, 3, "4"]
					]
				},
				BB: {
					JP: [
						[0, 0, "1"], [4, 0, "1(есть ястреб)"],
						[2, 1, "2"],
						[5, 2, "3"], [4, 2, "4"],
						[0, 3, "6(ПМК)"], [1, 3, "5"], [4, 3, "5(ПМК)"], [5, 3, "6(ПВО)"]
					],
					US: [
						[0, 0, "1"], [4, 0, "1(есть ястреб)"],
						[2, 1, "2"],
						[5, 2, "3"], [4, 2, "4"],
						[1, 3, "6"], [4, 3, "6(ПВО)"], [5, 3, "5(ПВО)"]
					],
					DE: [
						[0, 0, "1"], [4, 0, "1(есть ястреб)"],
						[2, 1, "2"],
						[5, 2, "3"], [6, 2, "4"],
						[0, 3, "5,6"], [4, 3, "5,6"]
					]
				},
				CA: {
					JP: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[2, 1, "2"], [7, 1, "3"],
						[4, 2, "5"], [5, 2, "7(>=IX)"], [6, 2, "4"],
						[7, 3, "6"]
					],
					US: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[7, 1, "3?"], [7, 1, "2"],
						[4, 2, "3"], [5, 2, "6,5"],
						[4, 3, "4"], [5, 3, "5,6"]
					],
					RU: [
						[0, 0, "1"], [6, 0, "1"],
						[2, 1, "2(=X)"], [7, 1, "2"],
						[4, 2, "5"], [5, 2, "3(есть хилка)"], [6, 2, "3,5"],
						[5, 3, "4"],
					],
					DE: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[2, 1, "2(=VII)"], [7, 1, "2"],
						[4, 2, "5"], [5, 2, "3(есть хилка)"], [6, 2, "3,5"],
						[5, 3, "4"]
					],
					GB: [
						[0, 0, "1"], [6, 0, "1"],
						[7, 1, "2"],
						[4, 2, "4"], [5, 2, "3"],
						[4, 3, "5"], [5, 3, "6"]
					]
				},
				DD: {
					JP: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[7, 1, "2"],
						[2, 2, "3"],
						[7, 3, "4"]
					],
					US: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[7, 1, "2"],
						[4, 2, "3"], [1, 2, "3,5(>=VII)"], [2, 2, "6"], [6, 2, "6"],
						[7, 3, "4"]
					],
					RU: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[7, 1, "2"],
						[4, 2, "3"], [6, 2, "5"],
						[4, 3, "4"], [7, 3, "6"]
					],
					DE: [
						[0, 0, "1"], [1, 0, "1"], [6, 0, "1"],
						[7, 1, "2"],
						[1, 2, "6(>=VII)"], [2, 2, "3,4"], [4, 2, "3,4"], [4, 2, "5"], [5, 2, "6"],
						[7, 3, "6"]
					]
				}
			};
			for (var shipType:String in perks) {
				for (var nation:String in perks[shipType]) {
					var _perkHint:Sprite = new Sprite;
					for (var i:uint = 0; i < perks[shipType][nation].length; i++) {
						_perkHint.addChild(MyPerkHint.produceHint(
							gameAPI,
							perks[shipType][nation][i][0],
							perks[shipType][nation][i][1],
							perks[shipType][nation][i][2]
						));
					}
					this._states[SHOW_PERK_MENU + shipType + nation] = _perkHint;
				}
			}
			
			gameAPI.data.addCallBack("HelpMe.SHOW_MENU", this.onShowMenu);
			gameAPI.data.addCallBack("HelpMe.CREATE_MENU", this.onCreateMenu);
			gameAPI.data.addCallBack("HelpMe.ADD_MENU_ITEM", this.onAddMenuItem);
			gameAPI.data.addCallBack("HelpMe.CREATE_FLAG_SET", this.onCreateFlagSet);
			gameAPI.data.addCallBack("HelpMe.ADD_FLAG_HINT", this.onAddFlagHint);
			log("[HelpMe] createWindow");
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
			if (!this._states[menuId])
			{
				var _menu:MyMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
				_menu.addMenuItem(this.repl(title));
				this._states[menuId] = _menu;
			}
		}

		private function onAddMenuItem(menuId:String, title:String):void
		{
			if (this._states[menuId])
			{
				this._states[menuId].addMenuItem(this.repl(title));
			}
		}

		private function onShowMenu(menuId:String, show:Boolean):void
		{
			if (this._states[menuId])
			{
				if (show) {
					gameAPI.stage.addChild(this._states[menuId]);
				} else {
					gameAPI.stage.removeChild(this._states[menuId]);
				}
			}
		}

		private function onCreateFlagSet(setId:String):void
		{
			if (!this._states[setId])
			{
				var _set:Sprite = new Sprite();
				_set.mouseChildren = _set.mouseEnabled = false;
				this._states[setId] = _set;
			}
		}

		private function onAddFlagHint(setId:String, hintType:String, col:int, row:int):void
		{
			if (this._states[setId])
			{
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
	}
}