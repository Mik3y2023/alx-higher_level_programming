#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints basic info about Python lists
 * @p: PyObject list
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int x;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (x = 0; x < size; x++)
		printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
}
