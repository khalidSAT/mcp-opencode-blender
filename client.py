#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عميل MCP OpenCode Blender
للتواصل مع الخادم وتنفيذ الأوامر
"""

import requests
import json
from typing import Dict, Any, Optional


class MCPClient:
    """عميل للتواصل مع خادم MCP"""
    
    def __init__(self, host: str = 'localhost', port: int = 5000):
        """
        إنشاء عميل جديد
        
        Args:
            host: عنوان الخادم
            port: منفذ الخادم
        """
        self.base_url = f'http://{host}:{port}'
        self.session = requests.Session()
    
    def send_command(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        إرسال أمر إلى الخادم
        
        Args:
            command: اسم الأمر
            params: معاملات الأمر
        
        Returns:
            استجابة الخادم
        """
        if params is None:
            params = {}
        
        try:
            response = self.session.post(
                f'{self.base_url}/api/command',
                json={'command': command, 'params': params},
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.ConnectionError:
            return {
                'status': 'error',
                'message': 'تعذر الاتصال بالخادم. تأكد من تشغيل الخادم.'
            }
        
        except requests.exceptions.Timeout:
            return {
                'status': 'error',
                'message': 'انتهت مهلة الانتظار. الخادم بطيء جداً.'
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'message': f'حدث خطأ: {str(e)}'
            }
    
    def get_status(self) -> Dict[str, Any]:
        """الحصول على حالة الخادم"""
        try:
            response = self.session.get(
                f'{self.base_url}/api/status',
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def list_commands(self) -> Dict[str, Any]:
        """عرض قائمة الأوامر المتاحة"""
        try:
            response = self.session.get(
                f'{self.base_url}/api/commands',
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def ping(self) -> bool:
        """اختبار الاتصال"""
        result = self.send_command('ping')
        return result.get('status') == 'success'
    
    def create_cube(self, name: str = 'cube', scale: float = 1.0) -> Dict[str, Any]:
        """إنشاء مكعب"""
        return self.send_command('create_primitive', {
            'type': 'cube',
            'name': name,
            'scale': scale
        })
    
    def create_sphere(self, name: str = 'sphere', scale: float = 1.0) -> Dict[str, Any]:
        """إنشاء كرة"""
        return self.send_command('create_primitive', {
            'type': 'sphere',
            'name': name,
            'scale': scale
        })
    
    def create_cylinder(self, name: str = 'cylinder', scale: float = 1.0) -> Dict[str, Any]:
        """إنشاء أسطوانة"""
        return self.send_command('create_primitive', {
            'type': 'cylinder',
            'name': name,
            'scale': scale
        })
    
    def set_location(self, object_name: str, x: float = 0, y: float = 0, z: float = 0) -> Dict[str, Any]:
        """تعديل موقع الكائن"""
        return self.send_command('set_object_property', {
            'object_name': object_name,
            'location': [x, y, z]
        })
    
    def set_rotation(self, object_name: str, x: float = 0, y: float = 0, z: float = 0) -> Dict[str, Any]:
        """تعديل دوران الكائن"""
        return self.send_command('set_object_property', {
            'object_name': object_name,
            'rotation': [x, y, z]
        })
    
    def set_scale(self, object_name: str, x: float = 1, y: float = 1, z: float = 1) -> Dict[str, Any]:
        """تعديل حجم الكائن"""
        return self.send_command('set_object_property', {
            'object_name': object_name,
            'scale': [x, y, z]
        })
    
    def apply_color(self, object_name: str, color: tuple = (1, 0, 0)) -> Dict[str, Any]:
        """تطبيق لون على الكائن"""
        return self.send_command('apply_material', {
            'object_name': object_name,
            'color': list(color)
        })
    
    def export_glb(self, filepath: str) -> Dict[str, Any]:
        """تصدير المشهد بصيغة GLB"""
        return self.send_command('export_scene', {
            'format': 'glb',
            'filepath': filepath
        })
    
    def export_fbx(self, filepath: str) -> Dict[str, Any]:
        """تصدير المشهد بصيغة FBX"""
        return self.send_command('export_scene', {
            'format': 'fbx',
            'filepath': filepath
        })
    
    def get_scene_info(self) -> Dict[str, Any]:
        """الحصول على معلومات المشهد"""
        return self.send_command('get_scene_info')


if __name__ == '__main__':
    # مثال على الاستخدام
    client = MCPClient()
    
    print("اختبار الاتصال...")
    if client.ping():
        print("✅ الاتصال ��اجح!")
        print(f"\nحالة الخادم: {client.get_status()}")
    else:
        print("❌ فشل الاتصال. تأكد من تشغيل الخادم.")
