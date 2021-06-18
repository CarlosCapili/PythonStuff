/*
This program finds a path to the bottom right corner of a maze using recursion, 
where 0's represent walls, 1 represents a possible path, and 8 is the path taken
*/

class MazeSolver{
	public static void main(String[]arg){
		Maze path = new Maze();
		path.displayMaze();

		if(path.recursiveSolver(0,0) == 0){
			System.out.println("You failed to find a way out!");
			path.displayMaze();
		}
		else{
			path.displayMaze();
			System.out.println("You made it through!");
		}
	}
}

class Maze{

	private int[][] maze = {
		{1,1,0,1,1},
		{0,1,0,0,0},
		{0,1,1,1,0},
		{0,0,0,1,1}
	};

	//Only goes right and down for now
	public int recursiveSolver(int row, int col){

		if(maze[row][col] == 1){
			//Change the maze path to an 8 indicating path taken
			maze[row][col] = 8;

			//Check if last element in 2d array is reached
			if(row == maze.length-1 && col == maze[0].length-1){
				return 1;
			}

			//Go right
			if(maze[row][col+1] == 1){
				return recursiveSolver(row, col+1);
			}
			else{
				return recursiveSolver(row+1, col);
			}
		}
		else{
			return 0; //base case
		}
	}// end of recursiveSolver

	public void displayMaze(){
		for(int i=0; i<maze.length; i++){
			for(int j=0; j<maze[i].length; j++){
				System.out.print(maze[i][j]);
				System.out.print(" ");
			}
			System.out.println("");
		}
	}
		
}