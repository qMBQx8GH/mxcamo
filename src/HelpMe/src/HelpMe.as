package 
{
	import flash.display.SimpleButton;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;
	import lesta.api.ModBase;
	import flash.utils.getDefinitionByName;
	import scaleform.clik.controls.Window;
    import scaleform.clik.controls.*;
	import flash.text.TextField;
    import flash.text.TextFormat;

	public class HelpMe extends ModBase 
	{
        private static const CHANGE_STATE:String = "HelpMe.changeState";
        private static const SHOW_MAIN_MENU:String = "HelpMe.showMainMenu";
        private static const SHOW_FLAG_MENU:String = "HelpMe.showFlagMenu";
        private static const SHOW_FLAG_HINT_CV:String = "HelpMe.showFlagHintCV";
        private static const SHOW_FLAG_HINT_BB:String = "HelpMe.showFlagHintBB";
        private static const SHOW_FLAG_HINT_CA:String = "HelpMe.showFlagHintCA";
        private static const SHOW_FLAG_HINT_DD:String = "HelpMe.showFlagHintDD";
        private static const SHOW_PERK_MENU:String = "HelpMe.showPerkMenu";
        private static const SHOW_PERK_MENU_CV:String = "HelpMe.showPerkMenuCV";
        private static const SHOW_PERK_MENU_BB:String = "HelpMe.showPerkMenuBB";
        private static const SHOW_PERK_MENU_CA:String = "HelpMe.showPerkMenuCA";
        private static const SHOW_PERK_MENU_DD:String = "HelpMe.showPerkMenuDD";
        private static const SHOW_PERK_HINT_TEST:String = "HelpMe.showPerkHintTest";
		private var _states:Object = {};
		
		public function HelpMe() 
		{
			super();
			log("[HelpMe] Constructor");
		}
		
		override public function init():void 
		{
			super.init();
			log("[HelpMe] init");
			createWindow();
		}
		
		override public function fini():void 
		{
            gameAPI.data.removeCallBack();
			super.fini();
		}
		
		private function createWindow():void
		{
			var _mainMenu:MyMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_mainMenu.addMenuItem("Help Me!");
			_mainMenu.addMenuItem("1. Сигнальные флаги");
			_mainMenu.addMenuItem("2. Навыки капитана");
			this._states[SHOW_MAIN_MENU] = _mainMenu;
			/*
			_mainMenu.graphics.lineStyle(2, 0xFF0000);
			var mainBarHeight:int = 90;
			var stageHeight:int = gameAPI.stage.height - mainBarHeight;
			var marginTop:int = (17 + (stageHeight - 720) / 6);
			_mainMenu.graphics.drawRect(0, mainBarHeight + marginTop, gameAPI.stage.width, 2);
			var iconVerticalPadding:int = 15 + (stageHeight - 720) / 18;
			var height:int = (26 + iconVerticalPadding);
			_mainMenu.graphics.drawRect(0, mainBarHeight + marginTop + height, gameAPI.stage.width, 2);
			*/
			var _flagMenu:MyMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_flagMenu.addMenuItem("Сигнальные флаги");
			_flagMenu.addMenuItem("1. Авианосец");
			_flagMenu.addMenuItem("2. Линкор");
			_flagMenu.addMenuItem("3. Крейсер");
			_flagMenu.addMenuItem("4. Эсминец");
			this._states[SHOW_FLAG_MENU] = _flagMenu;

			var _flagHintCV:Sprite = new Sprite;
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 0, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 2, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 3, 0));
			_flagHintCV.addChild(MyHint.produceHint(gameAPI, 4, 0));
			this._states[SHOW_FLAG_HINT_CV] = _flagHintCV;

			var _flagHintBB:Sprite = new Sprite;
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 1, 0));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 2, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 3, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 4, 1));
			_flagHintBB.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this._states[SHOW_FLAG_HINT_BB] = _flagHintBB;

			var _flagHintCA:Sprite = new Sprite;
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 0, 0));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 1, 1));
			_flagHintCA.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this._states[SHOW_FLAG_HINT_CA] = _flagHintCA;

			var _flagHintDD:Sprite = new Sprite;
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 2, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 3, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 4, 0));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 0, 1));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 1, 1));
			_flagHintDD.addChild(MyHint.produceHint(gameAPI, 5, 1));
			this._states[SHOW_FLAG_HINT_DD] = _flagHintDD;

			var _perkMenu:MyMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_perkMenu.addMenuItem("Навыки капитана");
			_perkMenu.addMenuItem("1. Авианосец");
			_perkMenu.addMenuItem("2. Линкор");
			_perkMenu.addMenuItem("3. Крейсер");
			_perkMenu.addMenuItem("4. Эсминец");
			this._states[SHOW_PERK_MENU] = _perkMenu;

			_perkMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_perkMenu.addMenuItem("Навыки капитана (Авианосец)");
			_perkMenu.addMenuItem("1. Япония");
			_perkMenu.addMenuItem("2. США");
			this._states[SHOW_PERK_MENU_CV] = _perkMenu;

			_perkMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_perkMenu.addMenuItem("Навыки капитана (Линкор)");
			_perkMenu.addMenuItem("1. Япония");
			_perkMenu.addMenuItem("2. США");
			//_perkMenu.addMenuItem("3. Советы");
			_perkMenu.addMenuItem("4. Немцы");
			this._states[SHOW_PERK_MENU_BB] = _perkMenu;

			_perkMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_perkMenu.addMenuItem("Навыки капитана (Крейсер)");
			_perkMenu.addMenuItem("1. Япония");
			_perkMenu.addMenuItem("2. США");
			_perkMenu.addMenuItem("3. Советы");
			_perkMenu.addMenuItem("4. Немцы");
			_perkMenu.addMenuItem("5. Бриты");
			this._states[SHOW_PERK_MENU_CA] = _perkMenu;

			_perkMenu = new MyMenu(gameAPI.stage.width, gameAPI.stage.height);
			_perkMenu.addMenuItem("Навыки капитана (Эсминец)");
			_perkMenu.addMenuItem("1. Япония");
			_perkMenu.addMenuItem("2. США");
			_perkMenu.addMenuItem("3. Советы");
			_perkMenu.addMenuItem("4. Немцы");
			this._states[SHOW_PERK_MENU_DD] = _perkMenu;

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
			
            gameAPI.data.addCallBack(CHANGE_STATE, this.onChangeState);
			log("[HelpMe] createWindow");
		}
        private function onChangeState(_arg1:String, _arg2:Boolean):void
		{
			if (this._states[_arg1])
			{
				if (_arg2) {
					gameAPI.stage.addChild(this._states[_arg1]);
				} else {
					gameAPI.stage.removeChild(this._states[_arg1]);
				}
			}
        }
	}
}