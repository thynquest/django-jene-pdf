from setuptools import setup, find_packages

setup(
    name='django-jene-pdf',
    description='open source project designed to generate pdf from django template using xhtml2pdf',
    long_description="""See the Github project page (https://github.com/thynquest/django-jene-pdf) for more on information""",
    license='MIT',
    keywords="pdf generator from django template using xhtml2pdf",
    version='1.0.1',
    author='Franck Kambiwa',
    author_email='thynquest@gmail.com',
    url='https://github.com/thynquest/django-jene-pdf',

    packages=find_packages(exclude=['jenesample']),
    install_requires=['Django>=2.0.7', 'xhtml2pdf>=0.2.2'],
        
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    )
)
