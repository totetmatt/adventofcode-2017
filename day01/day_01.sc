import scala.io.Source

var id = Source.fromFile("C:/Users/totetmatt/projects/adventofcode-2017/day01/input")
  .getLines
  .mkString
  .map(_.asDigit)
// Part 1
(id.last +: id )
  .sliding(2)
  .filter(_.distinct.size==1)
  .map(_(0)).sum

// Part 2
id.zipWithIndex.
  filter(x=>x._1 == id((x._2+id.size/2)%id.size))
  .map(_._1)
  .sum

id.takeRight(id.size/2).zip(id.take(id.size/2)).filter(x=>x._1==x._2).map(_._1).sum*2

// Old version got 'if' in 'map' to return directly the correct value to sum
// Not use if it makes it quicker , but using filter makes it more readable

// Funky Functional Delirium


def Capcha(id:Seq[Int],fct: (Int,Int)=>Int) = id.indices.map(idx => ((1-id(idx).compare(id(fct(idx,id.size))))%2) * id(idx)).sum
// Could use filter but the boolean trick is more fun
def Part01(idx:Int,size:Int) = (idx+1)%size
def Part02(idx:Int,size:Int) = (idx + id.size/2)%id.size

Capcha(id,Part01)
Capcha(id,Part02)


