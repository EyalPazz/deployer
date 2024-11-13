import typer
import yaml


from structures.config import Config

from utils import prompt_fields

app = typer.Typer()


@app.command()
def create_manifest():
    config = prompt_fields(Config)
    print(yaml.dump(config.model_dump(), sort_keys=False))


if __name__ == "__main__":
    app()
