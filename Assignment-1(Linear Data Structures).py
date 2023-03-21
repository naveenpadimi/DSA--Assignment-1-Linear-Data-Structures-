# 1. Delete the elements in an linked list whose sum is equal to zero

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def getNode(data):
	temp = ListNode(data)
	temp.next = None
	return temp

def printList(head):
	while (head.next):
		print(head.val, end=' -> ')
		head = head.next
	print(head.val, end='')

def removeZeroSum(head, K):
	root = ListNode(0)
	root.next = head

	umap = dict()

	umap[0] = root

	sum = 0

	while (head != None):

		sum += head.val

		if ((sum - K) in umap):

			prev = umap[sum - K]
			start = prev

			aux = sum

			sum = sum - K

			while (prev != head):
				prev = prev.next
				aux += prev.val
				if (prev != head):
					umap.remove(aux)

			start.next = head.next

		else:
			umap[sum] = head

		head = head.next

	return root.next

if __name__ == '__main__':
	head = getNode(1)
	head.next = getNode(2)
	head.next.next = getNode(-3)
	head.next.next.next = getNode(3)
	head.next.next.next.next = getNode(1)

	K = 5
	head = removeZeroSum(head, K)
	if(head != None):
		printList(head)

# 2. Reverse a linked list in groups of given size

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_linked_list_in_groups(head, k):
    if not head or not head.next or k == 1:
        return head
        
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while True:
        count = k
        curr = prev.next
        
        while count > 1 and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            count -= 1
        
        if count != 1:
            break
        
        prev = curr
    
    return dummy.next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = reverse_linked_list_in_groups(head, 2)
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next

# 3.Merge a linked list into another linked list at alternate positions.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge_linked_lists_at_alternate_positions(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    p1 = l1
    p2 = l2
    
    while p1 and p2:
        temp1 = p1.next
        temp2 = p2.next
        
        p1.next = p2
        p2.next = temp1
        
        p1 = temp1
        p2 = temp2
        
    return l1
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

new_head = merge_linked_lists_at_alternate_positions(l1, l2)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next

# 4. In an array, Count Pairs with given sum

def count_pairs_with_given_sum(arr, target_sum):
    count = 0
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)
        
    return count
arr = [1, 5, 7, -1, 5]
target_sum = 6
num_pairs = count_pairs_with_given_sum(arr, target_sum)
print(num_pairs)

# 5. Find duplicates in an array

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
        
    return duplicates
arr = [1, 2, 3, 4, 3, 5, 6, 4]
duplicates = find_duplicates(arr)
print(duplicates)

# 6. Find the Kth largest and Kth smallest number in an array

def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
    
def find_kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

arr = [3, 5, 2, 8, 6, 1, 9, 4, 7]

kth_largest = find_kth_largest(arr, 3)
print(kth_largest)
kth_smallest = find_kth_smallest(arr, 4)
print(kth_smallest)

# 7. Move all the negative elements to one side of the array

def move_negatives(arr):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
    
    return arr

arr = [2, -5, 1, 0, -3, 8, -4, -2]
new_arr = move_negatives(arr)
print(new_arr)

# 8. Reverse a string using a stack data structure

def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    
    reversed_string = ''
    while len(stack) > 0:
        reversed_string += stack.pop()
    
    return reversed_string

string = 'hello world'
reversed_string = reverse_string(string)
print(reversed_string)

# 9. Evaluate a postfix expression using stack

def evaluate_postfix_expression(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            value2 = stack.pop()
            value1 = stack.pop()
            if char == '+':
                stack.append(value1 + value2)
            elif char == '-':
                stack.append(value1 - value2)
            elif char == '*':
                stack.append(value1 * value2)
            elif char == '/':
                stack.append(value1 / value2)

    return stack.pop()
expression = "44+2*"
result = evaluate_postfix_expression(expression)
print(result)

# 10. Implement a queue using the stack data structure

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        if not self.dequeue_stack:
            raise IndexError("Queue is empty")

        return self.dequeue_stack.pop()
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  
print(q.dequeue())  
q.enqueue(4)
print(q.dequeue())  
print(q.dequeue())  







