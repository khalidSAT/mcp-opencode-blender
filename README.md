# 🚀 MCP OpenCode Blender

**MCP OpenCode Blender** هو خادم Model Context Protocol يوفر تكاملًا قويًا بين **OpenCode** و **Blender** لإدارة وتشغيل نماذج ثلاثية الأبعاد برمجيًا.

## ✨ المميزات

✅ التحكم الكامل في Blender عبر API  
✅ إنشاء وتعديل الأشكال ثلاثية الأبعاد  
✅ تطبيق المواد والألوان  
✅ تصدير النماذج بصيغ متعددة (GLB, FBX, OBJ)  
✅ دعم سكريبتات Python  
✅ معالجة الأخطاء المتقدمة  
✅ تسجيل شامل للعمليات  

## 📋 المتطلبات

- **Python** 3.8 أو أحدث
- **Blender** 3.0 أو أحدث
- **pip** (مدير الحزم)

## 🛠️ التثبيت

### 1. استنساخ المستودع
```bash
git clone https://github.com/khalidSAT/mcp-opencode-blender.git
cd mcp-opencode-blender
```

### 2. إنشاء بيئة افتراضية
```bash
# على Linux/Mac
python3 -m venv venv
source venv/bin/activate

# على Windows
python -m venv venv
venv\Scripts\activate
```

### 3. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

## 🚀 البدء السريع

### تشغيل الخادم
```bash
python server.py
```

**الناتج المتوقع:**
```
🚀 MCP OpenCode Blender Server Started
📍 Server running on: localhost:5000
✅ Ready to accept connections
```

### تشغيل الأمثلة
في نافذة أخرى:
```bash
python examples/basic_usage.py
```

## 📚 الأوامر المتاحة

### 1. `ping`
اختبار الاتصال بالخادم
```python
response = client.send_command('ping')
```

### 2. `create_primitive`
إنشاء شكل أولي
```python
response = client.send_command('create_primitive', {
    'type': 'cube',  # cube, sphere, cylinder, plane
    'name': 'my_object',
    'scale': 1.0
})
```

### 3. `set_object_property`
تعديل خصائص الكائن
```python
response = client.send_command('set_object_property', {
    'object_name': 'my_object',
    'location': [0, 0, 0],
    'rotation': [0, 0, 0],
    'scale': [1, 1, 1]
})
```

### 4. `apply_material`
تطبيق مادة وألوان
```python
response = client.send_command('apply_material', {
    'object_name': 'my_object',
    'color': [1, 0, 0],  # RGB (أحمر)
    'metallic': 0.5,
    'roughness': 0.3
})
```

### 5. `export_scene`
تصدير المشهد
```python
response = client.send_command('export_scene', {
    'format': 'glb',  # glb, fbx, obj, usdz
    'filepath': './output/scene.glb'
})
```

### 6. `get_scene_info`
الحصول على معلومات المشهد
```python
response = client.send_command('get_scene_info')
```

### 7. `help`
عرض جميع الأوامر المتاحة
```python
response = client.send_command('help')
```

## 📁 البنية الدليلية

```
mcp-opencode-blender/
├── server.py                 # خادم MCP الرئيسي
├── client.py                 # عميل للاتصال بالخادم
├── requirements.txt          # المكتبات المطلوبة
├── config.json              # إعدادات المشروع
├── .gitignore               # ملف استثناء Git
├── README.md                # هذا الملف
├── LICENSE                  # رخصة MIT
├── examples/
│   ├── basic_usage.py      # أمثلة أساسية
│   ├── advanced_usage.py   # أمثلة متقدمة
│   └── blender_integration.py  # التكامل مع Blender
├── tests/
│   ├── test_server.py      # اختبارات الخادم
│   ├── test_commands.py    # اختبارات الأوامر
│   └── test_client.py      # اختبارات العميل
├── docs/
│   ├── API_REFERENCE.md    # مرجع API
│   ├── TROUBLESHOOTING.md  # استكشاف الأخطاء
│   └── EXAMPLES.md         # أمثلة متقدمة
└── src/
    ├── blender_handler.py  # معالج Blender
    ├── command_parser.py   # محلل الأوامر
    └── utils.py            # دوال مساعدة
```

## 💡 أمثلة عملية

### مثال 1: إنشاء مشهد بسيط
```python
from client import MCPClient

client = MCPClient('localhost', 5000)

# إنشاء مكعب
client.send_command('create_primitive', {'type': 'cube', 'name': 'cube1'})

# تعديل الموقع
client.send_command('set_object_property', {
    'object_name': 'cube1',
    'location': [2, 0, 0]
})

# تطبيق لون أحمر
client.send_command('apply_material', {
    'object_name': 'cube1',
    'color': [1, 0, 0]
})
```

### مثال 2: إنشاء نموذج معقد
```python
# إنشاء عدة كائنات
for i in range(5):
    client.send_command('create_primitive', {
        'type': 'sphere',
        'name': f'sphere_{i}',
        'scale': 0.5 + i * 0.1
    })
    
    client.send_command('set_object_property', {
        'object_name': f'sphere_{i}',
        'location': [i * 3, 0, 0]
    })

# تصدير النموذج
client.send_command('export_scene', {
    'format': 'glb',
    'filepath': './models/scene.glb'
})
```

## 🐛 استكشاف الأخطاء

### المشكلة: "Connection refused"
**الحل:** تأكد من تشغيل الخادم:
```bash
python server.py
```

### المشكلة: "Module not found"
**الحل:** تثبيت المكتبات:
```bash
pip install -r requirements.txt
```

### المشكلة: Blender لم يتم اكتشافه
**الحل:** تعديل `config.json` وتحديد مسار Blender:
```json
{
  "blender_path": "/path/to/blender"
}
```

## 📖 التوثيق الإضافية

- 📘 [مرجع API الكامل](docs/API_REFERENCE.md)
- 🛠️ [استكشاف الأخطاء والحلول](docs/TROUBLESHOOTING.md)
- 💻 [أمثلة متقدمة](docs/EXAMPLES.md)

## 🤝 المساهمة

نرحب بمساهماتك! يرجى:

1. Fork المستودع
2. إنشاء فرع جديد (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'إضافة ميزة رائعة'`)
4. Push إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

## 📄 الرخصة

هذا المشروع مرخص تحت [MIT License](LICENSE) - انظر الملف للتفاصيل.

## 📧 التواصل

- 🐙 GitHub: [@khalidSAT](https://github.com/khalidSAT)
- 💬 Issues: [GitHub Issues](https://github.com/khalidSAT/mcp-opencode-blender/issues)

---

**صُنع بـ ❤️ بواسطة khalidSAT**
