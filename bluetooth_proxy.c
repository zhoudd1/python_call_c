#include <stdio.h>

struct bluetooth_t{    
    int status;
    char buf[128];
};

int bluetooth_proxy_cb(struct bluetooth_t bluetooth)
{
        printf("bluetooth status:%d, buf:%s \n", bluetooth.status, bluetooth.buf);

        return 0;
}
