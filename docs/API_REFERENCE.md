# مرجع API الكامل

## نقاط النهاية (Endpoints)

### 1. GET `/api/status`
الحصول على حالة الخادم

**المثال:**
```bash
curl http://localhost:5000/api/status
```

**الاستجابة:**
```json
{
  "status": "online",
  "version": "1.0.0",
  "timestamp": "2026-05-17T13:33:58Z",
  "scene": {
    "object_count": 5,
    "material_count": 3
  }
}
```

### 2. GET `/api/commands`
عرض قائمة الأوامر المتاحة

**المثال:**
```bash
curl http://localhost:5000/api/commands
```

**الاستجابة:**
```json
{
  "status": "success",
  "commands": {
    "ping": "اختبار الاتصال",
    "create_primitive": "إنشاء شكل أولي",
    "set_object_property": "تعديل خصائص الكائن",
    "apply_material": "تطبيق مادة وألوان",
    "export_scene": "تصدير المشهد",
    "get_scene_info": "الحصول على معلومات المشهد",
    "help": "عرض الأوامر المتاحة"
  }
}
```

### 3. POST `/api/command`
تنفيذ أمر

**الطلب:**
```bash
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{
    "command": "ping",
    "params": {}
  }'
```

**الاستجابة:**
```json
{
  "status": "success",
  "message": "الخادم يعمل بشكل صحيح",
  "timestamp": "2026-05-17T13:33:58Z"
}
```

---

## الأوامر المتاحة

### `ping`
اختبار الاتصال

**المعاملات:** لا توجد

**المثال:**
```python
response = client.send_command('ping')
```

### `create_primitive`
إنشاء شكل أولي

**المعاملات:**
- `type` (string): نوع الشكل (cube, sphere, cylinder, plane)
- `name` (string): اسم الكائن
- `scale` (float): الحجم الأولي

**المثال:**
```python
response = client.send_command('create_primitive', {
    'type': 'cube',
    'name': 'my_cube',
    'scale': 1.0
})
```

### `set_object_property`
تعديل خصائص الكائن

**المعاملات:**
- `object_name` (string): اسم الكائن
- `location` (array): الموقع [x, y, z]
- `rotation` (array): الدوران [x, y, z]
- `scale` (array): الحجم [x, y, z]

**المثال:**
```python
response = client.send_command('set_object_property', {
    'object_name': 'my_cube',
    'location': [1, 2, 3],
    'rotation': [0, 0, 0],
    'scale': [1, 1, 1]
})
```

### `apply_material`
تطبيق مادة وألوان

**المعاملات:**
- `object_name` (string): اسم الكائن
- `color` (array): RGB اللون [r, g, b]
- `metallic` (float): درجة المعدنية (0-1)
- `roughness` (float): درجة الخشونة (0-1)

**المثال:**
```python
response = client.send_command('apply_material', {
    'object_name': 'my_cube',
    'color': [1, 0, 0],  # أحمر
    'metallic': 0.5,
    'roughness': 0.3
})
```

### `export_scene`
تصدير المشهد

**المعاملات:**
- `format` (string): صيغة التصدير (glb, fbx, obj, usdz, blend)
- `filepath` (string): مسار الملف

**المثال:**
```python
response = client.send_command('export_scene', {
    'format': 'glb',
    'filepath': './output/scene.glb'
})
```

### `get_scene_info`
الحصول على معلومات المشهد

**المعاملات:** لا توجد

**المثال:**
```python
response = client.send_command('get_scene_info')
```

**الاستجابة:**
```json
{
  "status": "success",
  "scene": {
    "object_count": 2,
    "material_count": 1,
    "objects": [
      {
        "name": "cube_001",
        "type": "cube",
        "scale": 1.0,
        "location": [0, 0, 0],
        "rotation": [0, 0, 0]
      }
    ],
    "materials": []
  }
}
```

---

## رموز الأخطاء

| الكود | الوصف |
|------|-------|
| 200 | نجح الطلب |
| 400 | طلب غير صحيح |
| 404 | كائن غير موجود |
| 500 | خطأ في الخادم |

