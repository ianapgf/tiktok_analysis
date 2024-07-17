from setuptools import setup, find_packages

setup(
    name='tiktok_analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'tensorflow',
        'autokeras',
        'scikit-learn',
        'textblob',
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'train_model=scripts.train_autokeras:main',
            'match_campaign=scripts.match_campaign:main'
        ]
    },
)
