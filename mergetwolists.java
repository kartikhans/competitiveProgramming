public class mergetwolists{
	public ListNode mergeTwoList(ListNode l1, ListNode l2){
		        ListNode x;
        ListNode y;
        if(l1==null){
            return(l2);
        }
        else if(l2==null){
            return(l1);
        }
        if(l1.val<l2.val){
            y = l1;
            l1 = l1.next;
        }
        else{
            y=l2;
            l2=l2.next;
        }
        ListNode z = y;
        while(l1!=null || l2!=null){
            if(l1==null || l2==null){
                if(l1==null){
                    while(l2!=null){
                        y.next = l2;
                        l2 = l2.next;
                        y = y.next;
                    }
                    break;
                }
                else{
                   while(l1!=null){
                       y.next = l1;
                       l1 = l1.next;
                       y = y.next;
                   }
                    break;
                }
            }
            if(l1.val<l2.val){
                y.next = l1;
                l1 = l1.next;
                y=y.next;
            }
            else{
                y.next = l2;
                l2 = l2.next;
                y = y.next;
            }
        }
        return(z);
    }
	}
}