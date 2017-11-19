package {
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.events.MouseEvent;
	import lesta.api.GameAPI;

	public dynamic class MyButton extends Sprite
	{
		private var _gameAPI:GameAPI;
		private var _id:String;
		private var _label:String;
		private var _tf:TextField;

		public function MyButton(gameAPI:GameAPI, id:String, label:String) {
			this._gameAPI = gameAPI;
			this._id = id;
			this._label = label;
		}

		public function createButton(index:int):void
		{
			this.addEventListener(MouseEvent.CLICK, this.clicked);
			this.addEventListener(MouseEvent.ROLL_OVER, this.rollover);
			this.addEventListener(MouseEvent.ROLL_OUT, this.rollout);
			
			var width:int = 180;
			var height:int = 27;
			var top:int = 90 + height * index;
			var left:int = ((this._gameAPI.stage.width - width) / 2);

			this.x = left;
			this.y = top;
			this.addChild(Res.getMenuItem());

			this._tf = new TextField();
			this._tf.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0x96a9af);
			this._tf.htmlText = '<b>' + this._label + '</b>';
			this._tf.width = width;
			this._tf.x = 4;
			this._tf.y = 2;

			this.addChild(this._tf);
		}

		public function clicked(event:MouseEvent):void
		{
			if (this._id) {
				this._gameAPI.data.call("HelpMe.MENU_ITEM_CLICKED", new Array(this._id));
			}
		}

		public function rollover(event:MouseEvent):void
		{
			if (this._tf) {
				this._tf.htmlText = '<b>&gt;' + this._label + '</b>';
			}
		}

		public function rollout(event:MouseEvent):void
		{
			if (this._tf) {
				this._tf.htmlText = '<b>' + this._label + '</b>';
			}
		}
		
	}
}//package 
