###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################



class TurnTrackerNode:
# Hint: This class should look just like the LinkNode class (the doubly linked list version)
    def __init__(self, data, prev=None, Next=None):
        self.data = data
        self.prev = prev
        self.Next = Next
        if prev is not None:
            self.prev.next = self
        if Next is not None:
            self.Next.prev = self

    def __str__(self):
        return f"{self.data}"


class TurnTracker:
# Hint: This class shares a lot of functionality/logic with the DoublyLinkedList class from the textbook.
# A good place to start is by looking at that DoublyLinkedList class and examining which methods are going
# to be similar to those needed by the TurnTracker. Then start adjusting those methods to suit your needs here.
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
        self._nextPlayer = None
        self._reversed = False
        self._skipping = False

    def addPlayer(self, Player):
        #               h,t  h,t  h,t
        # list is empty: 1 <- 1 -> 1
        # head, tail
        if self._length == 0:
            # first node will be both head and the tail
            self.head = self.tail = TurnTrackerNode(Player)

            # set the pointers:
            self.head.Next = self.tail
            self.head.prev = self.tail

            # setting the tail pointers
            self.tail.Next = self.head
            self.tail.prev = self.head

        else:
            # second case:  more than one node (player)
            newNode = TurnTrackerNode(Player, self.tail, self.head)

            # 2 <- 3 -> 1
            #      h          t
            # 2 <- 1 -> 2 <-> 3 -> 1

            self.tail.Next = newNode
            self.tail = newNode

        # next player
        self._nextPlayer = self.tail
        self._length += 1
    
    def nextPlayer(self):
        # list     Jake <-> Lina <-> tim
        
        if self._length == 0:
            raise RuntimeError()
        
        # is the order reversed?
        if self._nextPlayer == None:
            self._nextPlayer = self.head
            return self._nextPlayer.data
        
        # if it is move backwrads (prev)
        if self._reversed == True:
            if self._skipping == True:
                self._nextPlayer = self._nextPlayer.prev.prev
                self._skipping = False
            else:
                self._nextPlayer = self._nextPlayer.prev

        # if not, move forwards (Next / link)
        else:
            if self._skipping == True:
                self._nextPlayer = self._nextPlayer.Next.Next
                self._skipping = False
            else:
                self._nextPlayer = self._nextPlayer.Next

        # return
        return self._nextPlayer.data
    
    def numberOfPlayers(self):
        return self._length
    
    def skipNextPlayer(self):
        # first we check what order its in

        # either reversed or not
        if self._skipping == True:
            self._skipping = False

        else:
            self._skipping = True

        # update the pointer accordingly

        # similar to nextPlayer
        pass

    def reverseTurnOrder(self):
        # its a boolean
        if self._reversed is True:
            self._reversed = False

        # if the opposite of whatever it is
        else:
            self._reversed = True




if __name__ == "__main__":

    """ ex = TurnTracker()
    plyr1 = TurnTrackerNode("tim")
    plyr2 = TurnTrackerNode("lina")
    plyr3 = TurnTrackerNode("jake")
    plyr4 = TurnTrackerNode("filipe")
    ex.addPlayer(plyr1)
    ex.addPlayer(plyr2)
    ex.addPlayer(plyr3)
    ex.addPlayer(plyr4)
    
    print(ex.head.Next) """