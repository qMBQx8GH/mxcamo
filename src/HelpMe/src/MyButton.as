package {
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;

	public dynamic class MyButton extends Sprite
	{
		private var _gameAPI:GameAPI;
		private var _id:String;

		public function MyButton(gameAPI:GameAPI, id:String) {
			this._gameAPI = gameAPI;
			this._id = id;
		}

		public function createButton(index:int, label:String):void
		{
			this.addEventListener(MouseEvent.CLICK, this.clicked);
			
			var width:int = 200;
			var height:int = 20;
			var top:int = 90 + height * index;
			var left:int = ((this._gameAPI.stage.width - width) / 2);

			this.graphics.beginFill(0xFFFFFF);
			this.graphics.drawRect(left, top, width, height);
			this.graphics.endFill();

			var tf:TextField = new TextField();
			tf.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0x000000);
			tf.htmlText = label;
			tf.width = width;
			tf.x = left;
			tf.y = top;

			this.addChild(tf);
		}

		public function clicked(event:MouseEvent):void
		{
			if (this._id) {
				this._gameAPI.data.call("HelpMe.MENU_ITEM_CLICKED", new Array(this._id));
			}
		}
	}
}//package 
