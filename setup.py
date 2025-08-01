from setuptools import setup, find_packages

setup(
    name='mlfinlab',
    version='0.1.2.8',  # Empfehlung: Erhöhe die Patch-Version für diese Kompatibilitätsupdates
    packages=find_packages(),
    url='https://github.com/Moccazio/mlfinlab-updated',
    license='Apache License 2.0',
    author='Hudson & Thames Quantitative Research',
    author_email='hello@hudsonthames.org',
    description='Python library for Machine Learning in Finance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy>=1.20.0,<2.0.0',       # Kompatibel mit Py 3.8-3.12, vor NumPy 2.0 Breaking Changes
        'pandas>=1.2.0,<3.0.0',       # Kompatibel mit Py 3.8-3.12, vor Pandas 3.0 Breaking Changes
        'scipy>=1.6.0,<2.0.0',        # Breite Kompatibilität
        'statsmodels>=0.12.0,<1.0.0', # Breite Kompatibilität
        'scikit-learn>=0.24.0,<2.0.0',# Für sklearn 1.x (wie in Fehlermeldung behoben)
        'matplotlib>=3.3.0,<4.0.0',   # Breite Kompatibilität
        'seaborn>=0.11.0,<0.14.0',    # Kompatibel mit aktuellen Versionen
        'joblib>=1.0.0,<2.0.0',       # Breite Kompatibilität
        'tqdm>=4.50.0,<5.0.0'         # Breite Kompatibilität
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        # Aktualisierte unterstützte Python-Versionen
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)
