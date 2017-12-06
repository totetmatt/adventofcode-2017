import scala.io.Source

val filename = "C:/Users/totetmatt/projects/adventofcode-2017/day04/input"
//Part 01
/*
Source.fromFile(filename)
  .getLines
  .map(x=>x.split("\t").map(p=>p.toInt).red)
  .map(x=>x.max-x.min).sum
*/
Source.fromFile(filename)
  .getLines
      .filter(x=>x.split(' ').distinct.size == x.split(' ').size).size

Source.fromFile(filename)
  .getLines
  .filter(x=>x.split(' ').map(_.sorted).distinct.size == x.split(' ').size).size

def Day04(filename:String,fct:String=>Boolean) =  Source.fromFile(filename).getLines.filter(fct).size
def Part01(line:String) = line.split(' ').distinct.size == line.split(' ').size
def Part02(line:String) = line.split(' ').map(_.sorted).distinct.size == line.split(' ').size

Day04(filename,Part01)
Day04(filename,Part02)