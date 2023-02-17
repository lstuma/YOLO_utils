#include <Python.h>

/* Docstrings */
static char module_docstring[] =
    "This module provides some basic utilities required for training, evaluating and using a YOLO model in C.";
static char hello_world_docstring[] =
    "Calculate the factorial of some given number";

/* Available functions */
static PyObject *hello_world(PyObject *self, PyObject *args);

/* Module specification */
static PyMethodDef module_methods[] = {
    {"hello_world", hello_world, METH_VARARGS, hello_world_docstring},
    {NULL, NULL, 0, NULL}
};

/* Initialize the module */
PyMODINIT_FUNC inityolo_utils(void)
{
  PyObject *m = Py_InitModule3("yolo_utils", module_methods, module_docstring);
  if (m == NULL)
    return;

}

static PyObject *hello_world(PyObject *self, PyObject *args)
{
  int n;

  /* Parse the input tuple */
  if (!PyArg_ParseTuple(args, "i", &n))
    return NULL;

  int value = n+2;

  /* Build the output tuple */
  PyObject *ret = Py_BuildValue("i", value);
  return ret;
}