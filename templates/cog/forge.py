import pathlib
from fabricius.generator import Generator

def run():
    generator = Generator()
    data = {
        "cog_name": "my_cog",
        "pascal_cog_name": "MyCog",  # Actually, this should use fabricius.utils.pascal_case()
        "use_config": True,
        "config_id": 8456132846
    }

    template_cwd = pathlib.Path(__file__).parent.resolve()

    file = generator.add_file("__init__", "py")
    file.from_file(template_cwd.joinpath("__init__.py.mustache")).to_directory(f"./{data['cog_name']}").use_mustache().with_data(data)

    file = generator.add_file("core", "py")
    file.from_file(template_cwd.joinpath("core.py.mustache")).to_directory(f"./{data['cog_name']}").use_mustache().with_data(data)

    file = generator.add_file("info.json")
    file.from_file(template_cwd.joinpath("info.json.mustache")).to_directory(f"./{data['cog_name']}").use_mustache().with_data(data)

    generator.execute()

if __name__ == '__main__':
    run()
