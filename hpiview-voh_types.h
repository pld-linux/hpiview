
#ifndef __VOH_TYPES_H__
#define __VOH_TYPES_H__

#include <glib.h>

typedef struct VohEventState {
	gchar		*string;
	guint		value;
	gboolean	active;
	gpointer	data;
} VohEventStateT;

enum {
	VOH_OBJECT_TYPE_UNSPECIFIED = 0,
	VOH_OBJECT_TYPE_INT,
	VOH_OBJECT_TYPE_UINT,
	VOH_OBJECT_TYPE_FLOAT,
	VOH_OBJECT_TYPE_BUFFER
};

typedef struct VohValue {
	guint		type;
	gint		vint;
	guint		vuint;
	gdouble		vfloat;
	gchar		*vbuffer;
} VohValueT;

#define VOH_OBJECT_NOT_AVAILABLE	0x1
#define VOH_OBJECT_READABLE		0x2
#define VOH_OBJECT_WRITABLE		0x4

typedef struct VohObject {
	gchar		*name;
	guint		numerical;
	VohValueT	value;
	guint		state;
	gpointer	data;
} VohObjectT;

#endif /* __VOH_TYPES_H__ */
