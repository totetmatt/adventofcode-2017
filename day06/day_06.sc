import scala.io.Source

val filename = "C:/Users/totetmatt/projects/adventofcode-2017/day06/input"
//Part 01
/*
Source.fromFile(filename)
  .getLines
  .map(x=>x.split("\t").map(p=>p.toInt).red)
  .map(x=>x.max-x.min).sum
*/
Source.fromFile(filename) .getLines.flatMap(_.split('\t').map(_.toInt)).mkString("|")


val p = Seq(0, 2, 7, 0)
def run(list:Seq[Int]): Int ={

  val size:Int = list.size
  val idx = list.indexOf(list.max)
  println((1 to list.max).map(idx+_)
    .map(x=> x % size)
    .groupBy(x=>x)
    .map(x=>(x._1,x._2.size))
    .mkString("|"))

    0
}
val l = Map(0->1)
p.zipWithIndex.map(w=>(w._2,w._1)).toMap.zip(l).mkString("|")
run(p)