var Graph = function(xDimen, yDimen, people, person_dict){
	this.xDim = xDimen;
	this.yDim = yDimen;
	this.people_list[] = people;
	this.person_dict[][] = person_dict;
}
function Graph.prototype.getXDimen = function() {
	return this.xDim;
}
function Graph.prototype.getYDimen = function() {
	return this.yDim;
}
function Graph.prototype.getPeopleList = function(){
	return this.people_list;
}
function Graph.prototype.getPersonDict = function(){
	return this.person_dict;
}

