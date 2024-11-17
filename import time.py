import time
from copy import deepcopy
from queue import PriorityQueue
class LogicMagnets:
    
    def __init__(self):
        self.game_levels = GameLevels()

    def start_game(self):
        level_num = int(input("Enter the number of the level: "))

        level = self.game_levels.get_level(level_num)
        moves = self.game_levels.get_moves(level_num)

        print("Enter 1 if you want to play by yourself")
        print("Enter 2 if you want to solve with BFS")
        #print("Enter 3 if you want to solve with UCS")
        choice = int(input("Choose an option: "))

        if choice == 1:
            user_play = UserPlay(level, moves)
            user_play.play()
        
        elif choice == 2:
            start_time = time.time()
            print("Solving ...")
            print("The path of the solution:")
            bfs_solver = BFS()
            bfs_solver.solve_bfs(level)
            stop_time = time.time()
            print(f"Time: {(stop_time - start_time) * 1000:.2f} milliseconds")
            
        # elif choice == 3:
        #     start_time = time.time()
        #     print("Solving ...")
        #     print("The path of the solution:")
        #     ucs_solver = UCS()
        #     ucs_solver.solve_ucs(level)
        #     stop_time = time.time()
        #     print(f"Time: {(stop_time - start_time) * 1000:.2f} milliseconds")
            
        else:
            print("Error: Invalid choice")


# Assuming these classes and their methods are implemented
class GameLevels:
    def get_level(self, level_num):
      
        pass

    def get_moves(self, level_num):
        
        pass


class UserPlay:
    def __init__(self, level, moves):
        self.level = level
        self.moves = moves

    def play(self):
      
        pass


class BFS:
    def solve_bfs(self, level):
       
        return []


class Actions:
    @staticmethod
    def print(solution, level):
      
        pass


if __name__ == "__main__":
    game = LogicMagnets()
    game.start_game()

##move
class Move:
    def move_north(self, level, rock_to_move, row, col):
        """
        Moves the rock in a given direction in the level grid.
        
        Args:
            level (list of lists): The grid representing the level.
            rock_to_move (str): The rock to be moved.
            row (int): Row index for the new rock position.
            col (int): Column index for the new rock position.

        Returns:
            list of lists: The updated level grid.
        """

        # Remove the rock from its original position
        for i in range(len(level)):
            for j in range(len(level[i])):
                if rock_to_move.upper() in level[i][j].upper():
                    level[i][j] = level[i][j][0] if level[i][j] else ""

        # Place the rock at the new position
        level[row][col] = level[row][col] + rock_to_move.upper()

        # Move rocks to the left
        for i in range(col, -1, -1):
            if i - 1 >= 0:
                if "R" in level[row][i].upper() and "#" != level[row][i - 1] and "R" not in level[row][i - 1].upper():
                    if "P" not in level[row][i - 1].upper() and "N" not in level[row][i - 1].upper():
                        level[row][i] = level[row][i][0]
                        level[row][i - 1] = level[row][i - 1] + "R"
                    break
                elif (i - 2 >= 0 and "R" in level[row][i].upper() and "#" != level[row][i - 2] and "R" in level[row][i - 1].upper()):
                    if "P" not in level[row][i - 2].upper() and "N" not in level[row][i - 2].upper():
                        if "R" not in level[row][i - 2].upper():
                            level[row][i] = level[row][i][0]
                            level[row][i - 2] = level[row][i - 2] + "R"
                        elif i - 3 >= 0:
                            level[row][i] = level[row][i][0]
                            level[row][i - 3] = level[row][i - 3] + "R"
                    break

        # Move rocks to the right
        for i in range(col, len(level[row])):
            if i + 1 < len(level[row]):
                if "R" in level[row][i].upper() and "#" != level[row][i + 1] and "R" not in level[row][i + 1].upper():
                    if "P" not in level[row][i + 1].upper() and "N" not in level[row][i + 1].upper():
                        level[row][i] = level[row][i][0]
                        level[row][i + 1] = level[row][i + 1] + "R"
                    break
                elif (i + 2 < len(level[row]) and "R" in level[row][i].upper() and "#" != level[row][i + 2] and "R" in level[row][i + 1].upper()):
                    if "P" not in level[row][i + 2].upper() and "N" not in level[row][i + 2].upper():
                        if "R" not in level[row][i + 2].upper():
                            level[row][i] = level[row][i][0]
                            level[row][i + 2] = level[row][i + 2] + "R"
                        elif i + 3 < len(level[row]):
                            level[row][i] = level[row][i][0]
                            level[row][i + 3] = level[row][i + 3] + "R"
                    break

        # Move rocks up
        for i in range(row, -1, -1):
            if i - 1 >= 0:
                if "R" in level[i][col].upper() and "#" != level[i - 1][col] and "R" not in level[i - 1][col].upper():
                    if "P" not in level[i - 1][col].upper() and "N" not in level[i - 1][col].upper():
                        level[i][col] = level[i][col][0]
                        level[i - 1][col] = level[i - 1][col] + "R"
                    break
                elif (i - 2 >= 0 and "R" in level[i][col].upper() and "#" != level[i - 2][col] and "R" in level[i - 1][col].upper()):
                    if "P" not in level[i - 2][col].upper() and "N" not in level[i - 2][col].upper():
                        if "R" not in level[i - 2][col].upper():
                            level[i][col] = level[i][col][0]
                            level[i - 2][col] = level[i - 2][col] + "R"
                        elif i - 3 >= 0:
                            level[i][col] = level[i][col][0]
                            level[i - 3][col] = level[i - 3][col] + "R"
                    break

        # Move rocks down
        for i in range(row, len(level)):
            if i + 1 < len(level):
                if "R" in level[i][col].upper() and "#" != level[i + 1][col] and "R" not in level[i + 1][col].upper():
                    if "P" not in level[i + 1][col].upper() and "N" not in level[i + 1][col].upper():
                        level[i][col] = level[i][col][0]
                        level[i + 1][col] = level[i + 1][col] + "R"
                    break
                elif (i + 2 < len(level) and "R" in level[i][col].upper() and "#" != level[i + 2][col] and "R" in level[i + 1][col].upper()):
                    if "P" not in level[i + 2][col].upper() and "N" not in level[i + 2][col].upper():
                        if "R" not in level[i + 2][col].upper():
                            level[i][col] = level[i][col][0]
                            level[i + 2][col] = level[i + 2][col] + "R"
                        elif i + 3 < len(level):
                            level[i][col] = level[i][col][0]
                            level[i + 3][col] = level[i + 3][col] + "R"
                    break

        return level
#to print

class Actions:
    @staticmethod
    def print(level, moves):
        print("Your current state:")
        for row in level:
            print(row)

# to check if can move
class Actions:
    @staticmethod
    def check_if_can_move(level, row, col):
        num_of_rows = len(level)
        num_of_cols = len(level[0])

        if row >= num_of_rows or col >= num_of_cols:
            print("There is no such space in this level.")
            return False

        if level[row][col] == "O" or level[row][col] == "-":
            return True
        else:
            return False
        
        
        from copy import deepcopy

class Actions:
    @staticmethod
    def is_final(level):
        for row in level:
            for cell in row:
                if "O" in cell.upper():
                    if not any(x in cell.upper() for x in ["R", "N", "P"]):
                        return False
        return True

    @staticmethod
    def equals(state1, state2):
        return state1 == state2

    @staticmethod
    def get_next_states(level, rock_to_move, move):
        next_states = []
        num_of_rows = len(level)
        num_of_cols = len(level[0])

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                level_copy = deepcopy(level)
                if "N" in rock_to_move.upper():
                    if Actions.check_if_can_move(level_copy, i, j):
                        new_state = move.move_n(level_copy, rock_to_move, i, j)
                        next_states.append(new_state)
                elif "P" in rock_to_move.upper():
                    if Actions.check_if_can_move(level_copy, i, j):
                        new_state = move.move_p(level_copy, rock_to_move, i, j)
                        next_states.append(new_state)
        return next_states

    @staticmethod
    def check_if_can_move(level, row, col):
        num_of_rows = len(level)
        num_of_cols = len(level[0])

        if row >= num_of_rows or col >= num_of_cols:
            print("There is no such space in this level.")
            return False

        if level[row][col] == "O" or level[row][col] == "-":
            return True
        else:
            return False

#Game levels implimentation
class GameLevels:
    def __init__(self):
       
        self.levels = {
            1: [["-", "-", "-", "-"], ["-", "O", "-R", "O"], ["-N1", "-", "-", "-"]],
            2: [["-", "-", "O", "-", "-"], ["-", "-", "-R", "-", "-"],
                ["O", "-R", "O", "-R", "O"], ["-", "-", "-R", "-", "-"], ["-N1", "-", "O", "-", "-"]],
            3: [["#", "#", "#", "O"], ["-", "-", "-R", "-"], ["-N1", "-", "-", "O"]],
            4: [["O", "-", "O"], ["#", "-R", "-"], ["-N1", "-", "-"], ["#", "-R", "-"], ["-", "O", "-"]],
            5: [["O", "#", "O"], ["OR", "#", "OR"], ["-R", "#", "-R"], ["O", "-N1", "-"]],
            6: [["-", "-", "-", "O", "-"], ["-", "-R", "O", "-R", "-"], ["-N1", "-", "-", "O", "-"]],
            7: [["O", "-", "-", "-"], ["OR", "-", "-", "-"], ["-R", "-N1", "-", "O"],
                ["-", "-R", "OR", "-"], ["#", "#", "#", "O"]],
            8: [["O", "-", "O", "-"], ["-", "-R", "-R", "-"], ["-N1", "-", "O", "-"]],
            9: [["-N1", "O", "-", "OR", "-", "-R", "O"]],
            10: [["-N1", "-", "-", "-"], ["-", "O", "-", "O"], ["-", "-", "-R", "-R"], ["O", "-R", "-", "O"]]
        }

       
        self.moves_num = {
            1: 5, 2: 5, 3: 5, 4: 2, 5: 2,
            6: 2, 7: 2, 8: 2, 9: 2, 10: 2
        }

    def get_level(self, level):
       
        return self.levels.get(level)

    def get_moves(self, level):
       
        return self.moves_num.get(level)


#to play by itself

import random

class Actions:

    @staticmethod
    def print(level, moves):
        print("Your current state:")
        for row in level:
            print(row)

    @staticmethod
    def check_if_can_move(level, row, col):
        num_of_rows = len(level)
        num_of_cols = len(level[0])

        if row < 0 or row >= num_of_rows or col < 0 or col >= num_of_cols:
            print("There is no such space in this level.")
            return False

        if level[row][col] == "O" or level[row][col] == "-":
            return True
        else:
            return False

    @staticmethod
    def is_final(level):
        for row in level:
            for cell in row:
                if 'O' in cell:
                    if 'R' not in cell and 'N' not in cell and 'P' not in cell:
                        return False
        return True

    @staticmethod
    def get_next_states(level, rock_to_move):
        next_states = []
        num_of_rows = len(level)
        num_of_cols = len(level[0])

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                level_copy = [row.copy() for row in level]
                if rock_to_move == "N":
                    if Actions.check_if_can_move(level_copy, i, j):
                        new_state = level_copy  
                        next_states.append(new_state)
                elif rock_to_move == "P":
                    if Actions.check_if_can_move(level_copy, i, j):
                        new_state = level_copy 
                        next_states.append(new_state)

        return next_states


class GameLevels:

    @staticmethod
    def get_level(level):
        levels = {
            1: [["-", "-", "-", "-"], ["-", "O", "-R", "O"], ["-N1", "-", "-", "-"]],
            2: [["-", "-", "O", "-", "-"], ["-", "-", "-R", "-", "-"], ["O", "-R", "O", "-R", "O"],
                ["-", "-", "-R", "-", "-"], ["-N1", "-", "O", "-", "-"]],
            3: [["#", "#", "#", "O"], ["-", "-", "-R", "-"], ["-N1", "-", "-", "O"]],
            4: [["O", "-", "O"], ["#", "-R", "-"], ["-N1", "-", "-"], ["#", "-R", "-"], ["-", "O", "-"]],
            5: [["O", "#", "O"], ["OR", "#", "OR"], ["-R", "#", "-R"], ["O", "-N1", "-"]],
            6: [["-", "-", "-", "O", "-"], ["-", "-R", "O", "-R", "-"], ["-N1", "-", "-", "O", "-"]],
            7: [["O", "-", "-", "-"], ["OR", "-", "-", "-"], ["-R", "-N1", "-", "O"], ["-", "-R", "OR", "-"],
                ["#", "#", "#", "O"]],
            8: [["O", "-", "O", "-"], ["-", "-R", "-R", "-"], ["-N1", "-", "O", "-"]],
            9: [["-N1", "O", "-", "OR", "-", "-R", "O"]],
            10: [["-N1", "-", "-", "-"], ["-", "O", "-", "O"], ["-", "-", "-R", "-R"], ["O", "-R", "-", "O"]]
        }
        return levels.get(level)

    @staticmethod
    def get_moves(level):
        moves_num = {
            1: 5, 2: 5, 3: 5, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2
        }
        return moves_num.get(level)

class Actions:
    def print(self, level, moves):
        print("Your current state: ")
        for row in level:
            print(row)
        print(f"Moves left: {moves}")

    def isFinal(self, level):
       
        for row in level:
            for cell in row:
                if 'O' in cell and ('R' not in cell and 'N' not in cell and 'P' not in cell):
                    return False
        return True

    def checkIfCanMove(self, level, row, col):
        numOfRows = len(level)
        numOfCols = len(level[0])

        if row >= numOfRows or col >= numOfCols:
            print("There is no such space in this level.")
            return False

        if level[row][col] in ["O", "-"]:
            return True
        return False


class Move:
    def moveN(self, level, rockToMove, row, col):
       
        level[row][col] = rockToMove
        return level

    def moveP(self, level, rockToMove, row, col):
       
        level[row][col] = rockToMove
        return level


class UserPlay:
    def __init__(self, level, moves):
        self.level = level
        self.moves = moves
        self.play()

    def play(self):
        actions = Actions()
        while True:
           
            actions.print(self.level, self.moves)

            if actions.isFinal(self.level):
                print("\n=========== GAME FINISHED ==============\n")
                return

            if self.moves == 0:
                print("\n=========== OUT OF MOVES ==============\n")
                return

            
            rockToMove = input("What rock do you want to move? ")

            if rockToMove in ["O", "-", "#"]:
                print("You can't move this rock!")
                return

            try:
                row = int(input("Enter the row to move: ")) - 1
                col = int(input("Enter the column to move: ")) - 1
            except ValueError:
                print("Invalid input. Please enter numbers for row and column.")
                continue

           
            canMove = actions.checkIfCanMove(self.level, row, col)
            if not canMove:
                print("You can't put your rock here.")
                continue

            if canMove:
                if "N" in rockToMove.upper():
                    move = Move()
                    self.level = move.moveN(self.level, rockToMove, row, col)
                    self.moves -= 1

                elif "P" in rockToMove.upper():
                    move = Move()
                    self.level = move.moveP(self.level, rockToMove, row, col)
                    self.moves -= 1



level_example = [
    ["-", "-", "-", "-"],
    ["-", "O", "-R", "O"],
    ["-N", "-", "-", "-"]
]
moves_example = 5


game = UserPlay(level_example, moves_example)


from collections import deque

class Actions:
    @staticmethod
    def equals(state1, state2):
      
        for i in range(len(state1)):
            for j in range(len(state1[0])):
                if state1[i][j] != state2[i][j]:
                    return False
        return True
    
    @staticmethod
    def isFinal(level):
        
        for row in level:
            for cell in row:
                if 'O' in cell and ('R' not in cell and 'N' not in cell and 'P' not in cell):
                    return False
        return True
    
    @staticmethod
    def getNextStates(level, rock):
        
        return []

    @staticmethod
    def print(level, depth):
       
        print(f"Depth {depth}:")
        for row in level:
            print(" ".join(row))


class BFS:
    def __init__(self):
        self.queueStates = deque()  
        self.visitedList = []       
        self.solution = []          
        self.parent = {}            

    def isVisited(self, level):
        for state in self.visitedList:
            if Actions.equals(state, level):
                return True
        return False

    def solveBFS(self, level):
        self.queueStates.append(level)
        
        if Actions.isFinal(level):
            return level

        while self.queueStates:
            current_state = self.queueStates.popleft()
            self.visitedList.append(level)
            rocksCanMove = []

            
            for i in range(len(current_state)):
                for j in range(len(current_state[0])):
                    if 'N' in current_state[i][j].upper() or 'P' in current_state[i][j].upper():
                        rocksCanMove.append(current_state[i][j][1:]) 

           
            for rock in rocksCanMove:
                next_states = Actions.getNextStates(current_state, rock)
                for child in next_states:
                    if not self.isVisited(child):
                        self.parent[tuple(map(tuple, child))] = current_state  # Store parent state

                        if not Actions.isFinal(child):
                            self.queueStates.append(child)
                        else:
                          
                            self.solution.append(child)
                            while not Actions.equals(child, level):
                                self.solution.append(self.parent.get(tuple(map(tuple, child))))
                                if self.parent.get(tuple(map(tuple, child))) is not None:
                                    child = self.parent.get(tuple(map(tuple, child)))
                            for state in reversed(self.solution):
                                Actions.print(state, 1)

                            print(f"size of visited: {len(self.visitedList)}")
                            print(f"solution depth: {len(self.solution) - 1}")

                            return child
        
        return None


initial_state = [
    ["-", "-", "-", "-"],
    ["-", "O", "-R", "O"],
    ["-N", "-", "-", "-"]
]

bfs = BFS()
result = bfs.solveBFS(initial_state)

from queue import PriorityQueue
from copy import deepcopy


# class UCS:
#     def __init__(self):
#         self.p_queue = PriorityQueue()  # Priority queue for UCS
#         self.visited_list = []  # List to track visited states
#         self.solution = []  # List to store the solution path
#         self.parent = {}  # Map to track parent-child relationships for backtracking

#     def is_visited(self, level):
#         # Check if a level (state) has already been visited
#         return any(self.are_states_equal(state, level) for state in self.visited_list)

#     def solve_ucs(self, level):
#         rocks_can_move = []

#         self.p_queue.put((0, level))  # Add the initial state with cost 0

#         while not self.p_queue.empty():
#             cost, current_state = self.p_queue.get()
#             self.visited_list.append(current_state)

#             # Identify movable rocks
#             for i in range(len(current_state)):
#                 for j in range(len(current_state[0])):
#                     if "N" in current_state[i][j].upper() or "P" in current_state[i][j].upper():
#                         rocks_can_move.append(current_state[i][j][1:])  # Extract rock identifier

#             # Explore possible moves for each rock
#             for rock in rocks_can_move:
#                 for child in Actions.get_next_states(current_state, rock):  # Generate possible next states
#                     if not self.is_visited(child):
#                         self.parent[self.hash_state(child)] = current_state

#                         if not Actions.is_final(child):  # Check if it's the final state
#                             self.p_queue.put((cost + 1, child))  # Assume uniform cost (1 for all moves)
#                         else:
#                             # Solution found, construct the solution path
#                             self.solution.append(child)
#                             while not self.are_states_equal(child, level):
#                                 self.solution.append(self.parent.get(self.hash_state(child)))
#                                 if self.parent.get(self.hash_state(child)) is not None:
#                                     child = self.parent.get(self.hash_state(child))

#                             # Print the solution path
#                             for state in reversed(self.solution):
#                                 Actions.print(state)
#                             print(f"Size of visited: {len(self.visited_list)}")
#                             print(f"Solution depth: {len(self.solution) - 1}")
#                             return child

#         print("No solution found.")
#         return None

#     @staticmethod
#     def are_states_equal(state1, state2):
#         # Compare two states to determine if they are identical
#         return state1 == state2

#     @staticmethod
#     def hash_state(state):
#         # Hash a state to create a unique, hashable representation
#         return tuple(tuple(row) for row in state)
