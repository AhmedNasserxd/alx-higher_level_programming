#include <stdio.h>
#include <Python.h>

/**
*print_python_bytes - print basic info about Python bytes objects
*@p: Python object
*/
void print_python_bytes(PyObject *p)
{
char *s;
Py_ssize_t len, i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

PyBytes_AsStringAndSize(p, &s, &len);
printf("  size: %ld\n", len);
printf("  trying string: %s\n", s);

Py_ssize_t limit = len > 10 ? 10 : len;
printf("  first %ld bytes: ", limit);
for (i = 0; i < limit; i++)
printf("%02x ", s[i] & 0xff);
printf("\n");
}

/**
*print_python_list - print basic info about Python lists
*@p: Python object
*/
void print_python_list(PyObject *p)
{
Py_ssize_t i;
PyObject *in_list;

if (!PyList_Check(p))
return;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < PyList_Size(p); i++)
{
in_list = PySequence_GetItem(p, i);
if (!in_list)
continue;

printf("Element %ld: %s\n", i, in_list->ob_type->tp_name);
        
if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
print_python_bytes(in_list);

Py_XDECREF(in_list);
}
}
