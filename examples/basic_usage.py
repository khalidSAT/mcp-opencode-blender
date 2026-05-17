#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أمثلة أساسية على استخدام MCP OpenCode Blender
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import MCPClient
import time


def print_header(text):
    """طباعة رأس قسم"""
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}\n")


def example_1_ping():
    """مثال 1: اختبار الاتصال"""
    print_header("مثال 1: اختبار الاتصال")
    
    client = MCPClient()
    result = client.send_command('ping')
    
    print(f"الحالة: {result['status']}")
    print(f"الرسالة: {result['message']}")


def example_2_create_primitives():
    """مثال 2: إنشاء أشكال أولية"""
    print_header("مثال 2: إنشاء أشكال أولية")
    
    client = MCPClient()
    
    # إنشاء مكعب
    print("إنشاء مكعب...")
    cube_result = client.create_cube('my_cube', scale=1.0)
    print(f"✅ {cube_result['message']}")
    
    # إنشاء كرة
    print("\nإنشاء كرة...")
    sphere_result = client.create_sphere('my_sphere', scale=0.8)
    print(f"✅ {sphere_result['message']}")
    
    # إنشاء أسطوانة
    print("\nإنشاء أسطوانة...")
    cylinder_result = client.create_cylinder('my_cylinder', scale=1.2)
    print(f"✅ {cylinder_result['message']}")


def example_3_transform_objects():
    """مثال 3: تعديل خصائص الكائنات"""
    print_header("مثال 3: تعديل خصائص الكائنات")
    
    client = MCPClient()
    
    # إنشاء كائن
    print("إنشاء مكعب...")
    client.create_cube('transform_test')
    
    # تعديل الموقع
    print("\nتعديل الموقع...")
    loc_result = client.set_location('transform_test', x=2, y=3, z=1)
    print(f"✅ الموقع: {loc_result['object']['location']}")
    
    # تعديل الدوران
    print("\nتعديل الدوران...")
    rot_result = client.set_rotation('transform_test', x=0.5, y=1.0, z=0.2)
    print(f"✅ الدوران: {rot_result['object']['rotation']}")
    
    # تعديل الحجم
    print("\nتعديل الحجم...")
    scale_result = client.set_scale('transform_test', x=2, y=2, z=0.5)
    print(f"✅ الحجم: {scale_result['object']['scale']}")


def example_4_apply_materials():
    """مثال 4: تطبيق المواد والألوان"""
    print_header("مثال 4: تطبيق المواد والألوان")
    
    client = MCPClient()
    
    # إنشاء كائنات
    print("إنشاء كائنات...")
    client.create_cube('red_cube')
    client.create_sphere('green_sphere')
    client.create_cylinder('blue_cylinder')
    
    # تطبيق ألوان مختلفة
    print("\nتطبيق الألوان...")
    
    print("  تطبيق أحمر على المكعب...")
    client.apply_color('red_cube', (1, 0, 0))
    
    print("  تطبيق أخضر على الكرة...")
    client.apply_color('green_sphere', (0, 1, 0))
    
    print("  تطبيق أزرق على الأسطوانة...")
    client.apply_color('blue_cylinder', (0, 0, 1))
    
    print("\n✅ تم تطبيق الألوان بنجاح")


def example_5_complex_scene():
    """مثال 5: إنشاء مشهد معقد"""
    print_header("مثال 5: إنشاء مشهد معقد")
    
    client = MCPClient()
    
    print("إنشاء مشهد بـ 5 كائنات...\n")
    
    colors = [
        (1, 0, 0),  # أحمر
        (0, 1, 0),  # أخضر
        (0, 0, 1),  # أزرق
        (1, 1, 0),  # أصفر
        (1, 0, 1)   # بنفسجي
    ]
    
    for i in range(5):
        obj_name = f'sphere_{i}'
        print(f"إنشاء {obj_name}...")
        
        # إنشاء كرة
        client.create_sphere(obj_name, scale=0.5 + i*0.1)
        
        # تعديل الموقع
        x = i * 3
        client.set_location(obj_name, x=x, y=0, z=0)
        
        # تطبيق لون
        client.apply_color(obj_name, colors[i])
    
    print("\n✅ تم إنشاء المشهد بنجاح")


def example_6_get_scene_info():
    """مثال 6: الحصول على معلومات المشهد"""
    print_header("مثال 6: معلومات المشهد")
    
    client = MCPClient()
    
    # إنشاء بعض الكائنات
    client.create_cube('info_cube')
    client.create_sphere('info_sphere')
    
    # الحصول على المعلومات
    print("الحصول على معلومات المشهد...\n")
    info = client.get_scene_info()
    
    if info['status'] == 'success':
        scene = info['scene']
        print(f"عدد الكائنات: {scene['object_count']}")
        print(f"عدد المواد: {scene['material_count']}")
        
        print(f"\nالكائنات:")
        for obj in scene['objects']:
            print(f"  - {obj['name']} ({obj['type']})")


def example_7_export_scene():
    """مثال 7: تصدير المشهد"""
    print_header("مثال 7: تصدير المشهد")
    
    client = MCPClient()
    
    # إنشاء مشهد
    print("إنشاء مشهد للتصدير...")
    client.create_cube('export_cube')
    client.create_sphere('export_sphere')
    
    # تصدير بصيغ مختلفة
    print("\nتصدير المشهد...")
    
    formats = [
        ('glb', './output/scene.glb'),
        ('fbx', './output/scene.fbx'),
        ('obj', './output/scene.obj')
    ]
    
    for fmt, filepath in formats:
        print(f"  تصدير {fmt}...")
        result = client.send_command('export_scene', {
            'format': fmt,
            'filepath': filepath
        })
        print(f"    ✅ {result['message']}")


def example_8_server_status():
    """مثال 8: الحصول على حالة الخادم"""
    print_header("مثال 8: حالة الخادم")
    
    client = MCPClient()
    
    print("الحصول على حالة الخادم...\n")
    status = client.get_status()
    
    print(f"الحالة: {status['status']}")
    print(f"الإصدار: {status['version']}")
    print(f"عدد الكائنات: {status['scene']['object_count']}")
    print(f"الوقت: {status['timestamp']}")


def example_9_list_commands():
    """مثال 9: عرض قائمة الأوامر"""
    print_header("مثال 9: قائمة الأوامر المتاحة")
    
    client = MCPClient()
    
    print("الأوامر المتاحة:\n")
    commands = client.list_commands()
    
    if commands['status'] == 'success':
        for cmd, desc in commands['commands'].items():
            print(f"  • {cmd}: {desc}")


def main():
    """تشغيل جميع الأمثلة"""
    print("\n" + "#"*50)
    print("# أمثلة MCP OpenCode Blender")
    print("#"*50)
    
    examples = [
        example_1_ping,
        example_2_create_primitives,
        example_3_transform_objects,
        example_4_apply_materials,
        example_5_complex_scene,
        example_6_get_scene_info,
        example_7_export_scene,
        example_8_server_status,
        example_9_list_commands
    ]
    
    for example in examples:
        try:
            example()
            time.sleep(0.5)
        except Exception as e:
            print(f"\n❌ خطأ: {str(e)}")
            print("تأكد من تشغيل الخادم: python server.py")
            break
    
    print("\n" + "#"*50)
    print("# انتهت الأمثلة")
    print("#"*50 + "\n")


if __name__ == '__main__':
    main()
