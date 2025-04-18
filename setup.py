from setuptools import setup, find_packages

setup(
    name="weather_CLI",
    version="0.1",
    packages=find_packages(),
    install_requires = ["requests"],
    entry_points= {
        "console_scripts": [
            'weather-cli = WeatherCLI.CLI:main'
            ]
                },
    tests_require = ["unittest"],
    test_suite = "Tests",
    description="A CLI tools to check the weather",
    long_description= open("README.md").read(),
    long_description_content_type='text/markdown',
    author="Reeda031",
    url="https://github.com/Reeda013/Weather-Api",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independant']
    )