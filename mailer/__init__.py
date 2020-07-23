from setuptools import setup, find_packages

setup(
    name='mailgunmailer',
    url='https://github.com/jenslaufer/mailgunmailer',
    author='Jens Laufer',
    author_email='jenslaufer@jenslaufer.com',
    packages=['mailer'],  # find_packages()
    install_requires=['requests', 'logging'
                      ],
    version='0.1.0',
    license='MIT',
    description='Simple service to send mail with attachment with Mailgun',
    include_package_data=True