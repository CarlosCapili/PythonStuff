/*
This program finds a path to the bottom right corner of a maze using recursion starting from the first index, 
where 0's represent walls, 1 represents a possible path, and 8 is the path taken
*/
class MazeSolver{
	public static void main(String[]arg){
		Maze path = new Maze();
		path.displayMaze();

		if(path.recursiveSolver(0,0) == false){
			System.out.println("You failed to find a way out!");
			path.displayMaze();
		}
		else{
			System.out.println("You made it through!");
			path.displayMaze();	
		}
	}
}

class Maze{
	private int[][] maze = {
		{1,1,1,1,1},
		{0,1,0,0,1},
		{0,1,0,0,1},
		{1,1,0,1,0},
		{0,1,1,1,1}
	};

	public boolean recursiveSolver(int row, int col){
		
		if (checkRowBounds(row) && checkColBounds(col) && maze[row][col] == 1 && maze[row][col] == 1){
			//Change the maze path to an 8 indicating path taken
			maze[row][col] = 8;
			//Check if last element in 2d array is reached
			if (row == maze.length-1 && col == maze[0].length-1){
				return true;
			}
			//Path movements
			if (recursiveSolver(row, col+1)){
				return true; //Move right
			}
			if (recursiveSolver(row+1, col)){
				return true; //Move down
			}
			if (recursiveSolver(row, col-1)){
				return true;//Move left
			}
			if (recursiveSolver(row-1, col)){
				return true;//Move Up
			}
			maze[row][col] = 6; 
			return false; //If it makes it here then it is false
		}
		return false;
	}// end of recursiveSolver

	private boolean checkColBounds(int col){
		return (col >= 0) && (col < maze[0].length);
	}
	private boolean checkRowBounds(int row){
		return (row >= 0) && (row < maze.length);
	}

	public void displayMaze(){
		for(int i=0; i<maze.length; i++){
			for(int j=0; j<maze[i].length; j++){
				System.out.print(maze[i][j]);
				System.out.print(" ");
			}
			System.out.println("");
		}
	}
		
}//end of class Maze