package 
{
	import flash.display.Bitmap;

	public class Res 
	{
		[Embed(source = "../res/exp.png")]
		private static var _Exp:Class;
		public static function getExp():Bitmap
		{
			return new _Exp();
		}

		[Embed(source = "../res/freexp.png")]
		private static var _FreeExp:Class;
		public static function getFreeExp():Bitmap
		{
			return new _FreeExp();
		}

		[Embed(source = "../res/credits.png")]
		private static var _Credits:Class;
		public static function getCredits():Bitmap
		{
			return new _Credits();
		}

		[Embed(source = "../res/crew.png")]
		private static var _Crew:Class;
		public static function getCrew():Bitmap
		{
			return new _Crew();
		}
	}
}