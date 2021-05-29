#include<stdio.h>
#include<math.h>
int main()
{
    int t;
    scanf("%d",&t);
    int s,w1,w2,w3;
    for(int i=t;i>0;i--)
    {
        scanf("%d ",&s);
        scanf("%d ",&w1);
        scanf("%d ",&w2);
        scanf("%d ",&w3);
        if((w1+w2+w3)<=s)
        {
            printf("1\n");
        }
        else if(w1+w2<=s&&w3<=s||w2+w3<=s&&w1<=s)
        {
            printf("2\n");
        }
        else 
        {
            printf("3\n");
        }
    }
}
