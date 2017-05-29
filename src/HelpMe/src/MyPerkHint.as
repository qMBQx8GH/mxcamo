package {
	import flash.display.Sprite;
	import flash.text.TextField;
    import flash.text.TextFormat;
	import lesta.api.GameAPI;

    public dynamic class MyPerkHint extends Sprite {

		private var _stageWidth:int;
		private var _stageHeight:int;
        public function MyPerkHint(stageWidth:int, stageHeight:int){
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
        }
		public static function produceHint(_gameAPI:GameAPI, col:int, row:int, label:String):MyPerkHint
		{
			var hint:MyPerkHint = new MyPerkHint(_gameAPI.stage.width, _gameAPI.stage.height);
			hint.createHint(col, row, label);
			return hint;
		}
		public function createHint(col:int, row:int, label:String):void
		{
			var centerX:int = this._stageWidth / 2 + this.getInGroup() / 2;
			var width:int = 60;
			var height:int = this.getHintHeight();
			var inGroup:int = this.getInGroup();
			var interGroup:int = this.getInterGroup();
			var x:int;
			if (col == 3) {
				x = centerX - interGroup / 2 - width;
			} else if (col == 2) {
				x = centerX - interGroup / 2 - inGroup - width * 2;
			} else if (col == 1) {
				x = centerX - interGroup / 2 - inGroup - interGroup - width * 3;
			} else if (col == 0) {
				x = centerX - interGroup / 2 - inGroup * 2 - interGroup  - width * 4;
			} else if (col == 4) {
				x = centerX + interGroup / 2;
			} else if (col == 5) {
				x = centerX + interGroup / 2 + inGroup + width;
			} else if (col == 6) {
				x = centerX + interGroup / 2 + inGroup + interGroup + width * 2;
			} else if (col == 7) {
				x = centerX + interGroup / 2 + inGroup * 2 + interGroup + width * 3;
			}
			var y:int = this.getTopOffset();
			this.graphics.lineStyle(2, 0xFF0000);
			this.graphics.moveTo(x, y + height * row + height);
			this.graphics.lineTo(x + width, y + height * row + height);
			
			var tf:TextField = new TextField();
            tf.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0xFF0000);
			tf.multiline = true; 
            tf.wordWrap = true;
            tf.text = label;
            tf.width = width;
			tf.height = 60; //iconSize
			tf.x = x;
			tf.y = y + height * row + height + 2;

            this.addChild(tf);

		}
		/*
		 * 
		 * 
		 * 
		<marginLeft value="10px"/>
		<marginRight value="10px"/>
		<marginTop value="32px"/>
		--------------------------
			<bind name="style" value="'marginTop'; (17 + (_stageHeight-720) / 6) + 'px'"/>
			<bind name="var" value="{iconSize: 60}"/>
			<bind name="watch" value="'iconHorizontalPadding'; 9 + (_stageWidth-1280) / 28"/>
			<bind name="watch" value="'iconVerticalPadding'; 15 + (_stageHeight-720) / 18"/>
			<bind name="watch" value="'groupPaddingCoeff'; 1.5"/>
		
			<bind name="style" value="'height'; ((26 + iconVerticalPadding) + 'px')"/>
		---------------------------
			<bind name="style" value="'width'; (8 * iconSize) + (7 * iconHorizontalPadding) + 3 * iconHorizontalPadding * groupPaddingCoeff)"/>
			<bind name="style" value="'height'; (4 * (iconSize + iconVerticalPadding) - iconVerticalPadding)"/>
		 */
		public function getTopOffset():int
		{
			var mainBarHeight:int = 90;
			var stageHeight:int = this._stageHeight;
			var marginTop:int = (17 + (stageHeight - 720) / 6);
			var iconVerticalPadding:int = 15 + (stageHeight - 720) / 18;
			var height:int = (26 + iconVerticalPadding);
			return  mainBarHeight + marginTop + height - iconVerticalPadding;
		}
		public function getHintHeight():int
		{
			var iconSize:int = 60;
			var mainBarHeight:int = 90;
			var stageHeight:int = this._stageHeight;
			var iconVerticalPadding:int = 15 + (stageHeight - 720) / 18;
			return iconSize + iconVerticalPadding + 1;
		}
		public function getInGroup():int
		{
			var stageWidth:int = this._stageWidth;
			var iconHorizontalPadding:int = 9 + (stageWidth - 1280) / 28;
			return iconHorizontalPadding;
		}
		public function getInterGroup():int
		{
			return this.getInGroup() * 5 / 2;
		}
    }
}//package 
