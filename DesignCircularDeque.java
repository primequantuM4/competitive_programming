class DoublyNode {
    int val;
    DoublyNode next;
    DoublyNode prev;
    public DoublyNode(int val){
        next = null;
        prev = null;
        this.val = val;
    }
}

class MyCircularDeque {
    int maxSize;
    DoublyNode head;
    DoublyNode tail;
    int size;
    public MyCircularDeque(int k) {
        maxSize = k;
        head = new DoublyNode(-1);
        tail = new DoublyNode(-1);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }
    
    public boolean insertFront(int value) {
        if (isFull()) return false;
        DoublyNode nodeValue = new DoublyNode(value);
        nodeValue.next = head.next;
        nodeValue.next.prev = nodeValue;
        head.next = nodeValue;
        nodeValue.prev = head;
        size++;

        return true;

    }
    
    public boolean insertLast(int value) {
        if (isFull()) return false;

        DoublyNode nodeValue = new DoublyNode(value);
        tail.prev.next = nodeValue;
        nodeValue.prev = tail.prev;
        tail.prev = nodeValue;
        nodeValue.next = tail;
        size++;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty()) return false;
        
        DoublyNode node = head.next;
        head.next = node.next;
        node.next.prev = head;

        size --;
        return true;
    }
    
    public boolean deleteLast() {
       if (isEmpty()) return false;
       
       DoublyNode node = tail.prev;
       node.prev.next = tail;
       tail.prev = node.prev;

        size --;
       return true;
    }
    
    public int getFront() {
        if(head.next.val == -1) return -1;
        return head.next.val;
    }
    
    public int getRear() {
        if(tail.prev.val == -1) return -1;
        return tail.prev.val;
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == maxSize;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
