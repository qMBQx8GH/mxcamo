package {
	import flash.display.Sprite;
	import lesta.api.GameAPI;

	public dynamic class MyMenu extends Sprite
	{
		private var _itemCount:int;
		private var _gameAPI:GameAPI;

		public function MyMenu(gameAPI:GameAPI)
		{
			this._itemCount = 0;
			this._gameAPI = gameAPI;
		}

		public function addMenuItem(label:String, id:String):void
		{
			var _sprite:MyButton;
			_sprite = new MyButton(this._gameAPI, id, label);
			_sprite.createButton(this._itemCount);
			this.addChild(_sprite);
			this._itemCount++;
		}
	}
}//package 
