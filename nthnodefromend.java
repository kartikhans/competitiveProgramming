class nthnodefromend {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode x = head;
        ListNode z = head;
        
        for(int i=0;i<n;i++){
            if(z.next==null){
                if(i==n-1){
                    head=head.next;
                    return (head);
                }
            }
            z = z.next;
        }
        while(z.next!=null){
            z = z.next;
            x = x.next;
        }
        ListNode kappa = x.next;
        x.next = x.next.next;
        kappa.next = null;
        return(head);
    }
}