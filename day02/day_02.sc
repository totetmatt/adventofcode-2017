import scala.io.Source

val filename = "C:/Users/totetmatt/projects/adventofcode-2017/day02/input"
//Part 01
/*
Source.fromFile(filename)
  .getLines
  .map(x=>x.split("\t").map(p=>p.toInt).red)
  .map(x=>x.max-x.min).sum
*/
Source.fromFile(filename)
  .getLines
  .map(
    x=>x.split("\t")
      .map(p=>p.toInt)
      .foldLeft[(Int,Int,Int)]((0,Int.MaxValue,0))((acc,v)=>
      (scala.math.max(acc._1,v),scala.math.min(acc._2,v),scala.math.max(acc._1,v)-scala.math.min(acc._2,v))
    )._3
  ).sum



//Part 02
// Didn't find itertools.permutation(2) equivalent, that's why using min max
Source.fromFile(filename)
  .getLines
  .map(x=>x.split("\t")
    .map(p=>p.toInt)
    .combinations(2)
    .filter(a=>a.max%a.min==0)
    .map(a=>a.max/a.min).reduceLeft((_,x)=>x)
  )
  .sum

// Funky Functional Delirium
def Checksum(filename:String,lineCheck:Array[Int]=>Int) = Source.fromFile(filename).getLines.map(lineToSeqInt).map(lineCheck).sum
def lineToSeqInt(x:String) = x.split("\t").map(p=>p.toInt)
def Part01(x:Array[Int]) = x.foldLeft[(Int,Int,Int)]((0,Int.MaxValue,0))((acc,v)=> (scala.math.max(acc._1,v),scala.math.min(acc._2,v),scala.math.max(acc._1,v)-scala.math.min(acc._2,v)))._3
def Part02(x:Array[Int]) = x.combinations(2).filter(a=>a.max%a.min==0).map(a=>a.max/a.min).reduceLeft((_,y)=>y)

Checksum(filename,Part01)
Checksum(filename,Part02)

