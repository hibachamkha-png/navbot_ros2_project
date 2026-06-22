from setuptools import setup

package_name = 'navbot_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiba',
    maintainer_email='hiba@example.com',
    description='NavBot bringup package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_navbot_publisher = navbot_bringup.hello_navbot_publisher:main',
            'hello_navbot_subscriber = navbot_bringup.hello_navbot_subscriber:main',
        ],
    },
)
