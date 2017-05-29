package {
	import flash.display.Sprite;
	import flash.text.TextField;
    import flash.text.TextFormat;

    public dynamic class MyMenu extends Sprite {

		private var _itemCount:int;
		private var _stageWidth:int;
		private var _stageHeight:int;

        public function MyMenu(stageWidth:int, stageHeight:int){
			this._itemCount = 0;
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
        }
		
		public function addMenuItem(label:String):void
		{
			var _sprite:MyButton;
			_sprite = new MyButton(this._stageWidth, this._stageHeight);
			_sprite.createButton(this._itemCount, label);
			this.addChild(_sprite);
			this._itemCount++;
		}
    }
}//package 
