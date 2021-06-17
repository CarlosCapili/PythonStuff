/*
This program finds a path to the bottom right corner of a maze using recursion, 
where 0's represent walls and 1 represent a possible path.
*/
class MazeSolver{
	public static void main(String[]arg){
		Maze path = new Maze();
		path.displayMaze();
	}
}

class Maze{

	private int[][] maze = {
		{1,1,1,1,1},
		{0,1,0,0,0},
		{0,1,1,1,0},
		{0,0,0,1,1}
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
		


}