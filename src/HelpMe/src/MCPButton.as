package {
    import scaleform.clik.controls.*;

    public dynamic class MCPButton extends Button {

        public function MCPButton(){
            addFrameScript(0, this.frame1, 9, this.frame10, 19, this.frame20, 29, this.frame30, 39, this.frame40);
        }
        public function frame1():void{
        }
        public function frame10():void{
            stop();
        }
        public function frame20():void{
            stop();
        }
        public function frame30():void{
            stop();
        }
        public function frame40():void{
            stop();
        }

    }
}//package 
