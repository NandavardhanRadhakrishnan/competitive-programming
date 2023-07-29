# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
# given a head pointer find if the linked list has a cycle or not

# i dont know how the code works, the algo is simple, but since python no proper pointer support, we have modify the code to consider input code stub, not the proper way of solving 

def has_cycle(head):
    itr = head
    pointer_arr = [None for i in range(llist_count)]
    count = 0
    while itr:
        if count<=llist_count-1:
            pointer_arr[count] = itr
        elif itr in pointer_arr:
            return 1
        else:
            return 0
        itr = itr.next
        count += 1