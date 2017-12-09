import scala.io.Source

val filename = "C:/Users/totetmatt/projects/adventofcode-2017/day09/input"

case class Acc (depth:Int,acc:Int,garbage_count:Int,garbage:Boolean)

def compute(acc:Acc,head:Char) : Acc= {
  {
    if(acc.garbage) {
      head match {
        case '>'  => Acc(acc.depth,acc.acc,acc.garbage_count,false)
        case _ =>Acc(acc.depth,acc.acc,acc.garbage_count+1,acc.garbage)
      }
    } else {
      head match {
        case '{'  => Acc(acc.depth+1,acc.acc+acc.depth+1,acc.garbage_count,acc.garbage)
        case '}' => Acc(acc.depth-1,acc.acc,acc.garbage_count,acc.garbage)
        case '<' => Acc(acc.depth,acc.acc,acc.garbage_count,true)
        case _ =>acc
      }
    }
  }
}

Source.fromFile(filename)
  .getLines()
  .mkString
  .replaceAll("!.","")
  .foldLeft(Acc(0,0,0,false))(compute)
