#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Function declarations

double calc_iou(double* box1, double* box2);

// Python functions

static PyObject* _n_max(PyObject* self)
{
  return PyUnicode_FromString("KEY KEY KEY!");
}

static PyObject* _iou(PyObject* self, PyObject* args)
{
  PyObject* _box1; PyObject* _box2;

  if(args == NULL) printf("\nARGS == NULL");
  // Parse argumentss
  if(!PyArg_ParseTuple(args, "OO", &_box1, &_box2)) return NULL;

  // Check if arguments are actually lists
  if(!PyList_Check(_box1) && !PyList_Check(_box2)) return NULL;

  // These will be our gracious boxes
  double box1[4] = {0,0,0,0}; double box2[4] = {0,0,0,0};

  for(int i = 0; i < 4; i++) {
    box1[i] = PyFloat_AsDouble(PyList_GetItem(_box1, i));
    box2[i] = PyFloat_AsDouble(PyList_GetItem(_box2, i));
  }

  double result = calc_iou(box1, box2);
  return PyFloat_FromDouble(result);
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