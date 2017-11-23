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
		private var _tf_normal:TextField;
		private var _bg_normal:Bitmap;
		private var _tf_selected:TextField;
		private var _bg_selected:Bitmap;

		public function MyButton(gameAPI:GameAPI, id:String, label:String)
		{
			this._gameAPI = gameAPI;
			this._id = id;
			this._label = label;
		}

		public function getNormalText():TextField
		{
			if (!this._tf_normal) {
				this._tf_normal = new TextField();
				this._tf_normal.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0x96a9af);
				this._tf_normal.htmlText = '<b>' + this._label + '</b>';
				this._tf_normal.width = 190;
				this._tf_normal.x = 4;
				this._tf_normal.y = 4;
			}
			return this._tf_normal;
		}

		public function getSelectedText():TextField
		{
			if (!this._tf_selected) {
				this._tf_selected = new TextField();
				this._tf_selected.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0xffffff);
				this._tf_selected.htmlText = '<b>' + this._label + '</b>';
				this._tf_selected.width = 190;
				this._tf_selected.x = 4;
				this._tf_selected.y = 4;
			}
			return this._tf_selected;
		}

		public function getNormalBackground():Bitmap
		{
			if (!this._bg_normal) {
				this._bg_normal = Res.getMenuItemNormal();
			}
			return this._bg_normal;
		}

		public function getSelectedBackground():Bitmap
		{
			if (!this._bg_selected) {
				this._bg_selected = Res.getMenuItemSelected();
			}
			return this._bg_selected;
		}

		public function createButton(index:int):void
		{
			var width:int = 200;
			var height:int = 30;
			var top:int = 90 + height * index;
			var left:int = ((this._gameAPI.stage.width - width) / 2);

			this.x = left;
			this.y = top;

			this.addChild(this.getNormalBackground());
			this.addChild(this.getNormalText());

			if (this._id) {
				this.addEventListener(MouseEvent.CLICK, this.clicked);
				this.addEventListener(MouseEvent.ROLL_OVER, this.rollover);
				this.addEventListener(MouseEvent.ROLL_OUT, this.rollout);
			}
		}

		public function clicked(event:MouseEvent):void
		{
			this._gameAPI.data.call("HelpMe.MENU_ITEM_CLICKED", new Array(this._id));
		}

		public function rollover(event:MouseEvent):void
		{
			this.addChild(this.getSelectedBackground());
			this.addChild(this.getSelectedText());
		}

		public function rollout(event:MouseEvent):void
		{
			this.removeChild(this.getSelectedText());
			this.removeChild(this.getSelectedBackground());
		}
	}
}//package 
