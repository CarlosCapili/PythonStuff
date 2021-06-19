/*
This program finds a possible pathway from the top left corner 
to the bottom right corner using recursion.

0s are walls and 1s are possible pathways
*/
import java.util.Scanner;

class MazeSolver{
	public static void main(String[]arg){
		
		Maze path = new Maze();
		int menu = 0;

		//MENU
		Scanner in = new Scanner(System.in);
		System.out.println("Welcome to Maze Solver!");
		System.out.println("\n1. When importing a textfile, make sure the rows and column lengths are equal");
		System.out.println("2. Make sure the all the values are either 1s or 0s, where 1s are walkable paths and 0s are walls");
		System.out.println("3. Values must be separated by commas. Ex. 0,1,0,0\n");
		System.out.println("Please enter the name of the file with the maze you want to be solved:");
		String fileName = in.nextLine();
		//pass filename to generateMaze function
		path.generateMaze(fileName);

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
	private int[][] maze;

	//make get/set methods for private maze

	public void generateMaze(String fileName){
		//open file and read each line as a row and place into maze

	}

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
			maze[row][col] = 1; 
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