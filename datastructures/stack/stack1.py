if __name__=="__main__":
	no_test_case=int(raw_input())
	while(no_test_case>0):
		pass_stack=[]
		no_pass,player1=map(int,raw_input().split())
		pass_stack.append(player1)
		while(no_pass > 0):
			action_player=raw_input()
			if action_player[0] == "B":
				pass_stack.append(pass_stack[-2])
			elif action_player[0] == "P":
				splitl=action_player.split()
				pl=int(splitl[1])
				pass_stack.append(pl)
			no_pass = no_pass - 1
		print "Player", pass_stack[-1] 	
		no_test_case = no_test_case - 1