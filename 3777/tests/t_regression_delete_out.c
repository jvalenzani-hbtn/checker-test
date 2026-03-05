#include "store.h"

int main(void)
{
    store_t st;
    session_t *s;
    session_t *out;

    store_init(&st);

    s = session_create("a", 1, (const unsigned char *)"x", 1);
    if (!s)
        return 1;

    if (!store_add(&st, s))
        return 1;

    out = NULL;
    if (!store_delete(&st, "a", &out))
        return 1;

    if (!out)
        return 1;

    session_destroy(out);
    store_destroy(&st);
    return 0;
}
