# Name      : Pranav Bhandari
# Student ID: 1001551132
# Date      : 12/06/2020

import sys

class Data:
    def __init__(self, state_type, reward):
        self.state_type = state_type
        self.reward = reward
        self.utility = 0
        self.policy = ""

    def __repr__(self):  
        return "state_type : % s, reward: % s, utility: % s, policy: % s\n" % (self.state_type, self.reward, self.utility, self.policy)  
    
    def __str__(self):  
        return "state_type : % s, reward: % s, utility: % s, policy: % s\n" % (self.state_type, self.reward, self.utility, self.policy)  

def process_environment(environment_file, non_terminal_reward):
    file = open(environment_file, "r")
    data = []
    for line in file:
        intermediate = []
        for state in line.rstrip().split(","):
            if state == ".":
                intermediate.append(Data("non-terminal", non_terminal_reward))
            elif state == "1.0" or state == "-1.0":
                intermediate.append(Data("terminal", float(state)))
            else:
                intermediate.append(Data("blocked", -sys.maxsize))
        data.append(intermediate)
    return data

def value_iteration(environment_file, non_terminal_reward, gamma, K):
    data = process_environment(environment_file, non_terminal_reward)
    U_dash = []
    for i in range(len(data)):
        intermediate = []
        for j in range(len(data[0])):
            intermediate.append(0)
        U_dash.append(intermediate)
    for n in range(K):
        # U = copy of U'
        for i in range(len(U_dash)):
            for j in range(len(U_dash[0])):
                data[i][j].utility = U_dash[i][j]
        # For each state S
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j].state_type == "blocked":
                    continue
                U_dash[i][j] = data[i][j].reward
                if data[i][j].state_type == "terminal":
                    continue
                max_val = -sys.maxsize

                # Up
                temp = 0
                # 0.8 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.8 * data[i-1][j].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.1 * data[i][j-1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.1 * data[i][j+1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp

                # Down
                temp = 0
                # 0.8 Case
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.8 * data[i+1][j].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.1 * data[i][j-1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.1 * data[i][j+1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
                
                # Left
                temp = 0
                # 0.8 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.8 * data[i][j-1].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.1 * data[i-1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.1 * data[i+1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp

                # Right
                temp = 0
                # 0.8 Case
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.8 * data[i][j+1].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.1 * data[i-1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.1 * data[i+1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
        
                U_dash[i][j] += (gamma * max_val)
    print("utilities:")
    for i in range(len(data)):
        for j in range(len(data[0])):
            print("{:6.3f}".format(data[i][j].utility), end= " ")
        print()
    print()

    print("policy:")
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].state_type == "terminal":
                data[i][j].policy = "o"
            elif data[i][j].state_type == "blocked":
                data[i][j].policy = "x"
            else:
                max_val = -sys.maxsize
                max_policy = ""

                # Up
                temp = 0
                # 0.8 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.8 * data[i-1][j].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.1 * data[i][j-1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.1 * data[i][j+1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
                    max_policy = "^"

                # Down
                temp = 0
                # 0.8 Case
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.8 * data[i+1][j].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.1 * data[i][j-1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.1 * data[i][j+1].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
                    max_policy = "v"
                
                # Left
                temp = 0
                # 0.8 Case
                if j-1 >=0 and data[i][j-1].state_type != "blocked":
                    temp += (0.8 * data[i][j-1].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.1 * data[i-1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.1 * data[i+1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
                    max_policy = "<"

                # Right
                temp = 0
                # 0.8 Case
                if j+1 <=len(data[0])-1 and data[i][j+1].state_type != "blocked":
                    temp += (0.8 * data[i][j+1].utility)
                else:
                    temp += (0.8 * data[i][j].utility)
                # 0.2 Case
                if i-1 >=0 and data[i-1][j].state_type != "blocked":
                    temp += (0.1 * data[i-1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if i+1 <=len(data)-1 and data[i+1][j].state_type != "blocked":
                    temp += (0.1 * data[i+1][j].utility)
                else:
                    temp += (0.1 * data[i][j].utility)
                
                if temp > max_val:
                    max_val = temp
                    max_policy = ">"
                data[i][j].policy = max_policy
            print("{:6s}".format(data[i][j].policy), end=" ")
        print()


if __name__ == "__main__":
    value_iteration(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]))