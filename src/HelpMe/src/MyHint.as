package {
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import lesta.api.GameAPI;

	public dynamic class MyHint extends Sprite
	{
		private var _stageWidth:int;
		private var _stageHeight:int;

		public function MyHint(stageWidth:int, stageHeight:int)
		{
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
		}

		public static function produceHint(_gameAPI:GameAPI, col:int, row:int):MyHint
		{
			var hint:MyHint = new MyHint(_gameAPI.stage.width, _gameAPI.stage.height);
			hint.createHint(col, row);
			return hint;
		}

		public function createHint(col:int, row:int):void
		{
			this.graphics.lineStyle(1, 0xfbc62c);
			var width:int = 68;
			this.graphics.drawRoundRect(
				this.getLeftOffset() + this.getColumnStep() * col - width / 2,
				this.getTopOffset() + this.getRowStep() * row - width / 2,
				width, width, 6
			);
			this.graphics.moveTo(
				this.getLeftOffset() + this.getColumnStep() * col + width / 2,
				this.getTopOffset() + this.getRowStep() * row - width / 2 + 3
			);
			this.graphics.lineTo(
				this.getLeftOffset() + this.getColumnStep() * col + width / 2,
				this.getTopOffset() + this.getRowStep() * row + width / 2 - 3
			);
		}

		public function getLeftOffset():int
		{
			return 50;
		}

		public function getTopOffset():int
		{
			return 230;
		}

		public function getColumnStep():int
		{
			return 80;
		}

		public function getRowStep():int
		{
			return 80;
		}
	}
}//package 
