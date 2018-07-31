from setuptools import setup, find_packages

setup(
    name='Django-jene-pdf',
    description='open source project designed to generate pdf from django template using xhtml2pdf',
    long_description="""See the Github project page (https://github.com/thynquest/django-jene.git) for more on information""",
    license='MIT',
    keywords="pdf generator from django template using xhtml2pdf",
    version='1.0.0',
    author='Franck Kambiwa',
    author_email='thynquest@gmail.com',
    url='https://github.com/thynquest/django-jene.git',

    packages=find_packages(exclude=['jenesample']),
    install_requires=['Django>=2.0.7', 'xhtml2pdf>=0.2.2'],
        
    classifiers=[
        "Development Status :: 2 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Distributed Computing",
    ]
)
