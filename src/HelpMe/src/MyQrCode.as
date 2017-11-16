package {
	import flash.display.Sprite;
	import org.qrcode.QRCode;
	import flash.display.Bitmap;
	import lesta.api.GameAPI;

	public dynamic class MyQrCode extends Sprite
	{
		private var _stageWidth:int;
		private var _stageHeight:int;

		public function MyQrCode(stageWidth:int, stageHeight:int)
		{
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
		}

		public static function produceQrCode(_gameAPI:GameAPI, x:int, y:int, label:String):MyQrCode
		{
			var qr_code:MyQrCode = new MyQrCode(_gameAPI.stage.width, _gameAPI.stage.height);
			qr_code.createQrCode(x, y, label);
			return qr_code;
		}

		public function createQrCode(x:int, y:int, label:String):void
		{
			var qr:QRCode = new QRCode();
			qr.encode(label);
			var img:Bitmap = new Bitmap(qr.bitmapData);
			img.x = x;
			img.y = y;
			this.addChild(img);
		}
	}
}//package 
