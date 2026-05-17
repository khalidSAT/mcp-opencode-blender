# استكشاف الأخطاء والحلول

## المشاكل الشائعة

### ❌ "Connection refused" / "الاتصال مرفوض"

**السبب:** الخادم غير مشغّل

**الحل:**
```bash
# تأكد من تشغيل الخادم في نافذة أخرى
python server.py
```

---

### ❌ "Module not found" / "الوحدة غير موجودة"

**السبب:** المكتبات المطلوبة لم تُثبّت

**الحل:**
```bash
# ثبّت المكتبات
pip install -r requirements.txt
```

---

### ❌ "Blender not found" / "Blender غير موجود"

**السبب:** Blender لم يتم تثبيته أو لم يتم العثور عليه

**الحل:**
1. تثبيت Blender من [blender.org](https://www.blender.org)
2. تحديث `config.json` بمسار Blender:
```json
{
  "blender": {
    "path": "/path/to/blender"
  }
}
```

---

### ❌ "Object not found" / "الكائن غير موجود"

**السبب:** محاولة تعديل كائن غير موجود

**الحل:**
```python
# تحقق من اسم الكائن
scene_info = client.get_scene_info()
for obj in scene_info['scene']['objects']:
    print(obj['name'])

# ثم استخدم الاسم الصحيح
client.set_location('correct_name', x=1, y=2, z=3)
```

---

### ❌ "Port already in use" / "المنفذ قيد الاستخدام"

**السبب:** المنفذ 5000 مستخدم بالفعل

**الحل 1:** استخدام منفذ آخر
```python
app.run(port=5001)
```

**الحل 2:** إيقاف البرنامج الذي يستخدم المنفذ
```bash
# على Linux/Mac
lsof -i :5000
kill -9 <PID>

# على Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

---

### ❌ "Request timeout" / "انتهت مهلة الانتظار"

**السبب:** الخادم بطيء جداً

**الحل:**
1. تقليل عدد العمليات
2. تحسين أداء الكمبيوتر
3. زيادة مهلة الانتظار:
```python
client.session.timeout = 60  # 60 ثانية
```

---

## نصائح للصيانة

✅ احتفظ بـ config.json محدثًا  
✅ افحص ملفات السجل بانتظام  
✅ استخدم بيئة افتراضية  
✅ حدّث المكتبات بشكل دوري  

