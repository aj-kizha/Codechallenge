import re
import sys

count = 0

def print_tree(rootnode=None):
    ''' prints the nodes in tree according to the rules '''
    tempnode = rootnode
    signset = ('+','-')
    tempcount = 0
   
    if tempnode is None:
        print "Nothing to print"
        return
    with open('output.txt','a+') as fp:        
        while(tempnode):
            if tempnode.identifier.startswith('*') and tempnode.itemlen == 1:
                global count
                count = count + 1
                decimalcount = .1
                print str(count) + tempnode.item[0]
                fp.write(str(count) + tempnode.item[0])
            elif tempnode.identifier.startswith('*') and tempnode.itemlen > 1 and tempnode.itemlen > tempnode.parent.itemlen or tempnode.right == None:
                if tempnode.parent == rootnode:
                    tempcount =  str(count) + str(decimalcount)[1:]
                else:
                    tempcount = str(tempcount) + str(.1)[1:]
                print str(tempcount) + tempnode.item[0]
                fp.write(str(tempcount) + tempnode.item[0])
            elif tempnode.identifier.startswith('*') and tempnode.itemlen > 1 and tempnode.itemlen < tempnode.parent.itemlen or tempnode.right == None:
                decimalcount = decimalcount + .1
                tempcount = str(count) + str(decimalcount)[1:]
                print str(tempcount) + tempnode.item[0]
                fp.write(str(tempcount) + tempnode.item[0])
            if tempnode.left:           
                leftnode = tempnode.left
                while leftnode:                
                    if leftnode.left and leftnode.left.itemlen > leftnode.itemlen:                    
                         if len(leftnode.item) == 1:                   
                             print " " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0])
                             fp.write(" " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0]))
                         elif len(leftnode.item) > 1:
                             print " " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0])
                             fp.write(" " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0]))
                             for elem in leftnode.item[1:]:
                                 print " " * (leftnode.itemlen + 1) * 2 + elem
                                 fp.write(" " * (leftnode.itemlen + 1) * 2 + elem)
                    elif leftnode.left and leftnode.left.itemlen == leftnode.itemlen or leftnode.left == None:
                         if len(leftnode.item) == 1:
                             print " " * (leftnode.itemlen + 1) + signset[1] + str(leftnode.item[0])
                             fp.write(" " * (leftnode.itemlen + 1) + signset[1] + str(leftnode.item[0]))
                         elif len(leftnode.item) > 1:
                             print " " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0])
                             fp.write(" " * (leftnode.itemlen + 1) + signset[0] + str(leftnode.item[0]))
                             for item in leftnode.item[1:]:
                                 print " " * (leftnode.itemlen + 1) * 2 + item
                                 fp.write(" " * (leftnode.itemlen + 1) * 2 + item)
                    leftnode = leftnode.left                         
            tempnode = tempnode.right
                     
class binaryTree(object):
    ''' binary tree to represent the tokens'''
    class _Node(object):
        def __init__(self,item=None,itemlen=None,identifier=None,parent=None,left=None,right=None):
            self.item = []
            self.left = left
            self.right = right
            self.identifier = identifier
            self.item.append(item)
            self.parent = parent
            self.itemlen = itemlen

    def __init__(self,item=None,itemlen=None,identifier=None):        
        self.root = None

    def createnode(self,item,itemlen,identifier):
        self._node = self._Node(item,itemlen,identifier)
        return self._node       


fp = sys.stdin.readlines()
root = None
current = None
obj = binaryTree()
for lines in fp:        
    if len(lines.rstrip('\r\n')) > 1: #discard blank lines            
        mt = re.match(r'(\.*\**)(.*)',lines,re.DOTALL) #matches the line starting with '.' or '*' or '**'
        tokenlen = len(mt.group(1))
        if mt.group(1).startswith('*') and tokenlen == 1: #if it is a '*' and count of '*' is 1
            if obj.root is not None:
                print_tree(obj.root)
                obj.root = None
            obj.root = obj.createnode(mt.group(2).rstrip('\r\n'),tokenlen,mt.group(1))
            current = obj.root
            leftcurrent = current
            current.right = None
        elif mt.group(1).startswith('*') and tokenlen > 1: #if it is a '*' and count of '*' is greater than one
            newnode = obj.createnode(mt.group(2).rstrip('\r\n'),tokenlen,mt.group(1)) #create a new right child
            current.right = newnode                
            newnode.parent = current
            current = newnode
            leftcurrent = current
            current.right = None
        elif mt.group(1).startswith('.'): # if its a '.' token
            newnode = obj.createnode(mt.group(2).rstrip('\r\n'),tokenlen,mt.group(1)) #create a new left child                              
            leftcurrent.left = newnode
            newnode.parent = leftcurrent
            leftcurrent = newnode
            leftcurrent.left = None                
        elif mt.group(1) == '':  # if line does not start with '*' or '.'
            leftcurrent.item.append(mt.group(2).rstrip('\r\n'))
if obj.root is not None:
    print_tree(obj.root)
   



                
                
            
               
                
                
                    
                
                
                
            

        
