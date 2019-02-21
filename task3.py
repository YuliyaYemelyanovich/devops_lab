#!/usr/bin/python

len1 = int(input())
friends = []
friend_of = []
for i in range(len1):
	friends.append(input())
len2 = int(input())
for i in range(len2):
	friend_of.append(input())

friends.sort()
	
mutual_friends_set = set(friends) & set(friend_of)
mutual_friends = list(mutual_friends_set)
mutual_friends.sort()
	
also_friend_of = list(set(friend_of) - mutual_friends_set)
also_friend_of.sort()
	
print("Friends: " + ", ".join(friends))
print("Mutual Friends: " + ", ".join(mutual_friends))
print("Also Friend of: " + ", ".join(also_friend_of))
