#include <Python.h>
#include <stdio.h>

/**
*print_python_bytes - Print information about Python bytes objects
*@p: PyObject pointer
*/
void print_python_bytes(PyObject *p)
{
char *str = NULL;

Py_ssize_t size, i, max;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

max = (size > 10) ? 10 : size + 1;
printf("  first %ld bytes:", max);
for (i = 0; i < max; i++)
printf(" %02x", (unsigned char)str[i]);

printf("\n");
}

/**
*print_python_list - Print information about Python list objects
*@p: PyObject pointer
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
*print_python_float - Print information about Python float objects
*@p: PyObject pointer
*/
void print_python_float(PyObject *p)
{
printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
