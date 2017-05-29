package {
	import flash.display.Sprite;
	import flash.text.TextField;
    import flash.text.TextFormat;

    public dynamic class MyButton extends Sprite {

		private var _stageWidth:int;
		private var _stageHeight:int;
        public function MyButton(stageWidth:int, stageHeight:int){
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
        }
		public function createButton(index:int, label:String):void
		{
			var width:int = 200;
			var height:int = 20;
			var top:int = 90 + height * index;
			var left:int = ((_stageWidth - width) / 2);

			this.graphics.beginFill(0xFFFFFF);
			this.graphics.drawRect(left, top, width, height);
			this.graphics.endFill();

			var tf:TextField = new TextField();
            tf.defaultTextFormat = new TextFormat("$WWSDefaultFont", 14, 0x000000);
            tf.text = label;
            tf.width = width;
			tf.x = left;
			tf.y = top;

            this.addChild(tf);
		}
    }
}//package 
