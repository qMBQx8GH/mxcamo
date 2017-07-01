package 
{
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;
	import lesta.api.ModBase;

	public class HelpMe extends ModBase 
	{
		private static const SHOW_FLAG_HINT_CV:String = "HelpMe.showFlagHintCV";
		private static const SHOW_FLAG_HINT_BB:String = "HelpMe.showFlagHintBB";
		private static const SHOW_FLAG_HINT_CA:String = "HelpMe.showFlagHintCA";
		private static const SHOW_FLAG_HINT_DD:String = "HelpMe.showFlagHintDD";
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

		private function addIcons(s: Sprite):void
		{
			s.addChild(MyIcon.produceIcon(gameAPI, Res.getCredits(), 0));
			s.addChild(MyIcon.produceIcon(gameAPI, Res.getCredits(), 1));
			s.addChild(MyIcon.produceIcon(gameAPI, Res.getExp(), 2));
			s.addChild(MyIcon.produceIcon(gameAPI, Res.getCrew(), 3));
			s.addChild(MyIcon.produceIcon(gameAPI, Res.getFreeExp(), 4));
		}

		private function createWindow():void
		{
			var _flagHintCV:Sprite = new Sprite;
			_flagHintCV.mouseChildren = _flagHintCV.mouseEnabled = false;
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 0, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 2, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 3, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 4, 0));
			this.addIcons(_flagHintCV);
			this._states[SHOW_FLAG_HINT_CV] = _flagHintCV;

			var _flagHintBB:Sprite = new Sprite;
			_flagHintBB.mouseChildren = _flagHintBB.mouseEnabled = false;
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 1, 0));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 2, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 3, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 4, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this.addIcons(_flagHintBB);
			this._states[SHOW_FLAG_HINT_BB] = _flagHintBB;

			var _flagHintCA:Sprite = new Sprite;
			_flagHintCA.mouseChildren = _flagHintCA.mouseEnabled = false;
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 0, 0));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 1, 1));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this.addIcons(_flagHintCA);
			this._states[SHOW_FLAG_HINT_CA] = _flagHintCA;

			var _flagHintDD:Sprite = new Sprite;
			_flagHintDD.mouseChildren = _flagHintDD.mouseEnabled = false;
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 2, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 3, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 4, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 1, 1));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this.addIcons(_flagHintDD);
			this._states[SHOW_FLAG_HINT_DD] = _flagHintDD;

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
	}
}