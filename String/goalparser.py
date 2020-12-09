#Goal Parser Interpretation
'''
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
'''
def interpret(command: str):
	res=''
	i=0
	while len(command)>i:
		if command[i]=='G':
			res+='G'
		elif command[i]=='('and command[i+1]==')':
			res+='o'
		elif command[i]=='(' and command[i+3]==')':
			res+='al'
		i+=1
	return res
	

out=interpret("G()(al)")
print(out)