import algorithms.notations as nt
import structures.queue as queue
import structures.stack as st
import structures.linkedlist as linked_list

# TEST DRIVERS

# -----------------------   notations    ----------------------------

# Postfix to prefix
# print(nt.postfix_to_prefix('2 3 4 * +'))

# Postfix to infix
# print(nt.postfix_to_infix('a b c - d + / e a - * c *'))

# Infix to postfix
# print(nt.infix_to_postfix('1 + 2 * 3 - 5'))
# print(nt.infix_to_postfix('1 + ( 2 + ( 4  + 34 ) / 2 ) + 6'))
# print(nt.infix_to_postfix('a / d - ( b + c ) * e'))

# Evaluate Postfix
# print(nt.eval_postfix('2 3 * 4 +'))

# -----------------------   end notations    ------------------------

# -----------------------   queue    --------------------------------

# Queue
# queue = queue.Queue()
#
# queue.add(5)
# queue.add(4)
# queue.add(9)
# queue.add(3)
#
# print(queue.size())
# print(queue.first())
# print(queue.last())
# print(queue)
# print(queue.delete())
# queue.add(8)
# queue.add(8)
# queue.add(8)
# print(queue)

# Circular Queue
# queue = queue.CircularQueue(3)
#
# queue.add(3)
# queue.add(4)
# queue.add(2)
#
# print(queue)
#
# print(queue.delete())
# print(queue.delete())
# queue.add('a')
# queue.add('b')
# print(queue.delete())
# print(queue.delete())
# print(queue.delete())

# Double Stack Queue
# queue = queue.DoubleStackQueue()
#
# queue.add('a')
# queue.add('b')
# print(queue.delete())
# print(queue.delete())
# queue.add('c')
# queue.add('d')
# queue.add('e')
#
# print(queue.delete())
# print(queue.delete())
# queue.add('5')
# queue.add('6')
# print(queue.delete())
# print(queue.delete())
# print(queue.delete())

# ----------------------   end queue    -----------------------------

# ----------------------   stack    ---------------------------------

# st = st.Stack()
#
# st.push(5)
# st.push(4)
# st.push(9)
# st.push(7)
#
# print(st.pop())
# print(st.pop())
# print(st.pop())
# st.push('a')
# print(st.pop())
# print(st.pop())
#
#
# print(st)

# st = st.DoubleEndedStack()

# ----------------------   end stack    -----------------------------

# ----------------------   linked list    ----------------------------

# linked_list = linked_list.LinkedList()
#
# linked_list.insert_first('a')
# linked_list.insert_first('b')
# linked_list.insert_first('c')
# linked_list.insert_first('d')
# linked_list.insert_first('e')
# linked_list.insert_first('f')
# linked_list.insert_first('g')
#
# linked_list.insert_last('last')
#
# for element in linked_list:
#     print(element, end='\t')
# print('\n')
#
# linked_list.remove_head()
#
# for element in linked_list:
#     print(element, end='\t')
# print('\n')
#
# linked_list.remove_tail()
#
# for element in linked_list:
#     print(element, end='\t')

# queue = queue.LinkedListQueue()
#
# queue.add('a')
# queue.add('b')
# queue.add('c')
#
# print(queue.delete())
# print(queue.delete())
# queue.add('3')
# print(queue.delete())
# print(queue.delete())
#
# queue.add('4')
# queue.add('5')
#
# print(queue)

# stack = st.LinkedListStack()
#
# stack.push('first')
# stack.push('second')
# stack.push('third')
#
# print(stack.pop())
# print(stack.pop())
# stack.push('4')
# print(stack.pop())
# print(stack.pop())
#
# print(stack)

# first_node = linked_list.Node('1')
#
# second_node = linked_list.Node('2')
# linked_list.insert_before_node(first_node, second_node)
#
# third_node = linked_list.Node('3')
# linked_list.insert_before_node(first_node, third_node)
#
# forth_node = linked_list.Node('4')
# linked_list.insert_before_node(second_node, forth_node)
#
# print(first_node)
# print(second_node)
# print(third_node)
# print(forth_node)

# first_node = linked_list.Node('1')
#
# second_node = linked_list.Node('2')
# linked_list.insert_before_node(first_node, second_node)
#
# third_node = linked_list.Node('3')
# linked_list.insert_before_node(first_node, third_node)
#
# print(first_node)
# print(second_node)
# print(third_node)
#
# linked_list.delete_previous_node(first_node)
#
# print(first_node)
# print(second_node)
