


var Person = function(macId, xLoc, yLoc, entryTime){
	this.xLoc = x;
	this.yLoc = y;
	this.macID = macID;
	this.timeEntered = entryTime.valueOf();
	this.exitTime = -1;
}
// public class Person {
// 	private double xLoc;
// 	private double yLoc;
// 	private String macID;
// 	public Person(String macID, double x, double y, String entryTime){
// 		this.xLoc = x;
// 		this.yLoc = y;
// 		this.macID = macID;
// 		Time timeEntered = Time.valueOf(entryTime);
// 	}
function Person.prototype.update = function(xNew, yNew){
		xLoc = xNew; 
		yLoc = yNew; 
	}
function Person.prototype.getX= function(){
		return this.xLoc;
	}
function Person.prototype.getY = function(){
		return this.yLoc;
	}
function Person.prototype.getMac = function(){
		return this.macID;
	}
function Person.prototype.getEntryTime = function(){
		return this.timeEntered;
	}
function Person.prototype.getLeavingTime = function(){
	return this.exitTime;
}
// function Person.prototype.hasLeft(){
// 		if (this.timeEntered == null){
// 			return true;
// 		}
// 		return false;
// 	}

}