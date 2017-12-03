
val init= Map((0,0)->1,(0,1)->2)


def next(board:Map[(Int,Int),Int],pos:(Int,Int),dir:String):((Int,Int),String) = {
  dir match   {
    case "u"=> board.get((pos._1-1,pos._2)) match {
      case _:Some[Int] => ((pos._1,pos._2+1),dir)
      case _ => ((pos._1-1,pos._2),"l")
    }
    case "r"=> board.get((pos._1,pos._2+1)) match {
      case _: Some[Int] => ((pos._1+1,pos._2),dir)
      case _=> ((pos._1,pos._2+1),"u")
    }
    case "l"=> board.get((pos._1,pos._2-1)) match {
      case _:Some[Int] => ((pos._1-1,pos._2),dir)
      case _ => ((pos._1,pos._2-1),"d")
    }
    case "d"=> board.get((pos._1+1,pos._2)) match {
      case _:Some[Int] =>  ((pos._1,pos._2-1),dir)
      case _ => ((pos._1+1,pos._2),"r")
    }

  }
}
def generate(board:Map[(Int,Int),Int],limit:Int,current:(Int,Int)=(0,1),dir:String="r") : ((Int,Int),Int) = {


  if (limit == board(current) ) {

      (current,board(current))
    } else {
      val x = next(board,current,dir)

      val nextval = board.getOrElse(current,0) + 1
      generate(board ++ Map((x._1._1,x._1._2) -> nextval),limit,(x._1._1,x._1._2),x._2)

    }
}
val data = generate(init,368078)
math.abs(data._1._1) + math.abs(data._1._2)