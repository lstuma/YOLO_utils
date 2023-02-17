#include <Python.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Python functions

static PyObject* _n_max(PyObject* self)
{
  return PyUnicode_FromString("KEY KEY KEY!");
}

static PyObject* _iou(PyObject* self, PyObject* args)
{
  PyObject* private;
  if(!PyArg_ParseTuple(args, "U", &private)) return NULL;

  return PyUnicode_FromString("IOU");
}

// Init function

void init()
{
  // nothing
}

// Method definition
static struct PyMethodDef methods[] = {
    {"iou", (PyCFunction)_iou, METH_VARARGS},
    {"n_max", (PyCFunction)_n_max, METH_VARARGS},
    {NULL, NULL, NULL}
};

// Module definition
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "yolo_utils",
    NULL,
    -1,
    methods
};

// Initialize module
PyMODINIT_FUNC PyInit_yolo_utils(void) {
  init();
  return PyModule_Create(&module);
}