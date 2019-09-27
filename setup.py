from setuptools import setup

requirements = [
    "PyQt5>=5.13.1",
    "opencv-python",
    "pandas>=0.25.1"
]


setup(
    name="easy_annotation",
    version="1.2.0",
    description="Programs used in Summer Project 2019.",
    url="https://github.com/KissLeaRon/easy_annotation",
    author="KissLeaRon",
##    license='',  # TBD
    scripts=["mizo_gui.py",
             "resize.py"],
    entry_points={
        "gui_scripts": ["mizotator = mizo_gui:main"]
    },
    install_requires=requirements,
    python_requires='>=3.4',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
    ],
)
