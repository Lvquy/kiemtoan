# -*- coding: utf-8 -*-
{
    'name': 'Trung tâm đào tạo Kiểm Toán Nhà Nước',
    'version': '1',
    'category': 'Trung tâm đào tạo kiểm toán',
    'live_test_url': '#',
    'summary': 'Phần mềm quản lý',
    'author': 'Lv Quy',
    'company': 'Trường Phát',
    'website': 'https://#',
    'depends': ['base_setup','website'],
    'data': [
        #data

        # security
        'security/groups.xml',
        'security/ir.model.access.csv',
        # report
        # views
        'views/custom_footer.xml',
        'views/event_views.xml',
        'views/tkb_views.xml',
        'views/zalo_link_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # 'kiem_toan/static/src/css/style.css'
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
}
