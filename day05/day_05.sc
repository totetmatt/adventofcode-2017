import scala.io.Source

val filename = "C:/Users/totetmatt/projects/adventofcode-2017/day05/input"
//Part 01
/*
Source.fromFile(filename)
  .getLines
  .map(x=>x.split("\t").map(p=>p.toInt).red)
  .map(x=>x.max-x.min).sum
*/
Source.fromFile(filename)
  .getLines.map(_.toInt)

// Very nice, but very inefficient
val P = Seq(0,3,0,1,-3)
P.patch(0,Seq(10),1)
def run(p:Seq[Int],i:Int=0,acc:Int=0): Int={
     p.lift(i) match {
       case a:Some[Int] => run(p.updated(i,a.get+1),i+a.get,acc+1)
       case _ => acc
     }
}

run(Source.fromFile(filename)
  .getLines.map(_.toInt).toSeq)


def run2(p:Seq[Int],i:Int=0,acc:Int=0): Int= {
  p.lift(i) match {
    case a: Some[Int] => if (a.get >= 3) {
      run(p.updated(i, a.get - 1), i + a.get, acc + 1)
    } else {
      run(p.updated(i, a.get + 1), i + a.get, acc + 1)
    }
    case _ => acc
  }
}

run2(Source.fromFile(filename)
  .getLines.map(_.toInt).toSeq)
