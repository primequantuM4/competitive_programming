class Solution {
    public int leastInterval(char[] tasks, int n) {
        Arrays.sort(tasks);
        Deque<Integer> queue = new LinkedList<Integer>();
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(Collections.reverseOrder());
        char currentAlphabet = tasks[0];
        int count = 0;
        int time = 0;
        int i = 0;
        while (i < tasks.length) {
            if (currentAlphabet == tasks[i]) {
                count ++;
            }
            else {
                heap.add(count);
                currentAlphabet = tasks[i];
                count = 1;
            }
            if (i + 1 == tasks.length) {
                if (currentAlphabet == tasks[i]){
                    heap.add(count);
                    
                } else {
                    heap.add(1);
                }
            }
            i ++;
        }
        
        while (!heap.isEmpty() || !queue.isEmpty()) {
            time ++;
            
            if (!heap.isEmpty()) {
                int aNumber = heap.poll() - 1;
                
                if (aNumber > 0) {
                    queue.add(time + n);
                    queue.add(aNumber);
                }
            }
            if ((!queue.isEmpty()) && queue.peek() == time) {
                queue.pop();
                heap.add(queue.pop());
            }
        }
        return time;
    }
}
