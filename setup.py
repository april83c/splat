from setuptools import setup

setup(
    name="nxbt",
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python==1.2.16",
        "Flask==1.1.2",
        "Flask-SocketIO==5.0.1",
        "eventlet==0.33.3",
        "blessed==1.17.10",
        "pynput==1.7.1",
        "psutil==5.6.6",
        "cryptography==3.3.2",
        "jinja2<3.1.0",
        "itsdangerous==2.0.1",
        "werkzeug==2.0.3",
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)
