#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبارات الخادم
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app, execute_command


class TestServer(unittest.TestCase):
    """اختبارات الخادم الرئيسية"""
    
    def setUp(self):
        """إعداد الاختبارات"""
        self.app = app
        self.client = self.app.test_client()
    
    def test_home_endpoint(self):
        """اختبار نقطة النهاية الرئيسية"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'MCP OpenCode Blender')
    
    def test_status_endpoint(self):
        """اختبار نقطة النهاية للحالة"""
        response = self.client.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'online')
    
    def test_commands_endpoint(self):
        """اختبار نقطة النهاية للأوامر"""
        response = self.client.get('/api/commands')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('ping', data['commands'])
    
    def test_ping_command(self):
        """اختبار أمر ping"""
        response = self.client.post('/api/command',
            json={'command': 'ping', 'params': {}})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
    
    def test_create_primitive_command(self):
        """اختبار أمر إنشاء شكل أولي"""
        response = self.client.post('/api/command',
            json={
                'command': 'create_primitive',
                'params': {'type': 'cube', 'name': 'test_cube'}
            })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')


class TestCommands(unittest.TestCase):
    """اختبارات الأوامر"""
    
    def test_execute_ping(self):
        """اختبار تنفيذ ping"""
        result = execute_command('ping', {})
        self.assertEqual(result['status'], 'success')
    
    def test_execute_create_primitive(self):
        """اختبار تنفيذ create_primitive"""
        result = execute_command('create_primitive', {
            'type': 'sphere',
            'name': 'test_sphere'
        })
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['object']['type'], 'sphere')
    
    def test_execute_unknown_command(self):
        """اختبار أمر غير معروف"""
        result = execute_command('unknown', {})
        self.assertEqual(result['status'], 'error')


if __name__ == '__main__':
    unittest.main()
