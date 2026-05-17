#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
خادم MCP OpenCode Blender
يوفر واجهة REST API للتحكم في Blender
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import logging
import os
from datetime import datetime

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# إنشاء تطبيق Flask
app = Flask(__name__)
CORS(app)

# تحميل الإعدادات
def load_config():
    """تحميل الإعدادات من config.json"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning('ملف config.json غير موجود، استخدام الإعدادات الافتراضية')
        return {
            'server': {'host': 'localhost', 'port': 5000},
            'blender': {'version': '3.0+'}
        }

config = load_config()

# قاموس الأوامر المتاحة
AVAILABLE_COMMANDS = {
    'ping': 'اختبار الاتصال',
    'create_primitive': 'إنشاء شكل أولي',
    'set_object_property': 'تعديل خصائص الكائن',
    'apply_material': 'تطبيق مادة وألوان',
    'export_scene': 'تصدير المشهد',
    'get_scene_info': 'الحصول على معلومات المشهد',
    'help': 'عرض الأوامر المتاحة'
}

# حفظ البيانات الوهمية
scene_data = {
    'objects': [],
    'materials': [],
    'frame': 0
}


def execute_command(command, params):
    """تنفيذ أمر معين"""
    logger.info(f"تنفيذ الأمر: {command} مع المعاملات: {params}")
    
    if command == 'ping':
        return {'status': 'success', 'message': 'الخادم يعمل بشكل صحيح'}
    
    elif command == 'create_primitive':
        obj_type = params.get('type', 'cube')
        obj_name = params.get('name', f'{obj_type}_001')
        scale = params.get('scale', 1.0)
        
        new_object = {
            'name': obj_name,
            'type': obj_type,
            'scale': scale,
            'location': [0, 0, 0],
            'rotation': [0, 0, 0]
        }
        scene_data['objects'].append(new_object)
        
        return {
            'status': 'success',
            'message': f'تم إنشاء {obj_type} باسم {obj_name}',
            'object': new_object
        }
    
    elif command == 'set_object_property':
        obj_name = params.get('object_name')
        location = params.get('location')
        rotation = params.get('rotation')
        scale = params.get('scale')
        
        for obj in scene_data['objects']:
            if obj['name'] == obj_name:
                if location:
                    obj['location'] = location
                if rotation:
                    obj['rotation'] = rotation
                if scale:
                    obj['scale'] = scale
                
                return {
                    'status': 'success',
                    'message': f'تم تعديل خصائص {obj_name}',
                    'object': obj
                }
        
        return {'status': 'error', 'message': f'الكائن {obj_name} غير موجود'}
    
    elif command == 'apply_material':
        obj_name = params.get('object_name')
        color = params.get('color', [1, 1, 1])
        metallic = params.get('metallic', 0.0)
        roughness = params.get('roughness', 0.5)
        
        material = {
            'object': obj_name,
            'color': color,
            'metallic': metallic,
            'roughness': roughness
        }
        scene_data['materials'].append(material)
        
        return {
            'status': 'success',
            'message': f'تم تطبيق المادة على {obj_name}',
            'material': material
        }
    
    elif command == 'export_scene':
        export_format = params.get('format', 'glb')
        filepath = params.get('filepath', f'./output/scene.{export_format}')
        
        # إنشاء المجلد إذا لم يكن موجوداً
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        return {
            'status': 'success',
            'message': f'تم تصدير المشهد بصيغة {export_format}',
            'filepath': filepath
        }
    
    elif command == 'get_scene_info':
        return {
            'status': 'success',
            'scene': {
                'object_count': len(scene_data['objects']),
                'material_count': len(scene_data['materials']),
                'objects': scene_data['objects'],
                'materials': scene_data['materials']
            }
        }
    
    elif command == 'help':
        return {
            'status': 'success',
            'commands': AVAILABLE_COMMANDS
        }
    
    else:
        return {'status': 'error', 'message': f'الأمر "{command}" غير معروف'}


@app.route('/api/command', methods=['POST'])
def handle_command():
    """معالج طلب الأوامر"""
    try:
        data = request.get_json()
        command = data.get('command')
        params = data.get('params', {})
        
        if not command:
            return jsonify({
                'status': 'error',
                'message': 'لم يتم توفير أمر'
            }), 400
        
        result = execute_command(command, params)
        result['timestamp'] = datetime.now().isoformat()
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f'خطأ في معالجة الأمر: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': f'حدث خطأ: {str(e)}'
        }), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """الحصول على حالة الخادم"""
    return jsonify({
        'status': 'online',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'scene': {
            'object_count': len(scene_data['objects']),
            'material_count': len(scene_data['materials'])
        }
    })


@app.route('/api/commands', methods=['GET'])
def list_commands():
    """عرض قائمة الأوامر المتاحة"""
    return jsonify({
        'status': 'success',
        'commands': AVAILABLE_COMMANDS
    })


@app.route('/', methods=['GET'])
def home():
    """الصفحة الرئيسية"""
    return jsonify({
        'name': 'MCP OpenCode Blender',
        'version': '1.0.0',
        'description': 'خادم Model Context Protocol للتحكم في Blender',
        'endpoints': {
            'status': '/api/status',
            'commands': '/api/commands',
            'execute': '/api/command (POST)'
        }
    })


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 MCP OpenCode Blender Server")
    print("="*50)
    print(f"📍 الخادم يعمل على: localhost:5000")
    print(f"✅ جاهز لقبول الاتصالات")
    print(f"📝 الإصدار: 1.0.0")
    print("="*50 + "\n")
    
    app.run(
        host=config['server']['host'],
        port=config['server']['port'],
        debug=config['server'].get('debug', False)
    )
