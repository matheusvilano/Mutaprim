if __name__ == "__main__":
    from setuptools import find_packages, setup
    from pathlib import Path

    setup(
        author="Matheus Vilano",
        author_email="",
        classifiers=[
            "DEVELOPMENT STATUS :: 4 - BETA",
            "INTENDED AUDIENCE :: DEVELOPERS",
            "INTENDED AUDIENCE :: EDUCATION",
            "LICENSE :: OSI APPROVED :: APACHE SOFTWARE LICENSE",
            "OPERATING SYSTEM :: OS INDEPENDENT",
            "PROGRAMMING LANGUAGE :: PYTHON :: 3",
        ],
        description="Mutable primitives - types that encapsulate a primitive so it can be modified inside a function.",
        install_requires=(Path(__file__).parent / "requirements.txt").read_text().splitlines(),
        keywords="reference mutable primitive modify pass encapsulation container",
        license="Apache Software License (Apache License 2.0)",
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type="text/markdown",  # GitHub-flavored Markdown (GFM)
        name="mutaprim",
        packages=find_packages("mutaprim"),
        package_dir={"": "mutaprim"},
        project_urls={
            "Author Website": "https://www.matheusvilano.com/",
            "Git Repository": "https://github.com/matheusvilano/mutaprim.git",
        },
        python_requires=">=3.6",
        url="https://github.com/matheusvilano/PyWwise.git",
        version="0.1.0",
    )
