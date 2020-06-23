import os

import click

from prefect.utilities.storage import extract_flow_from_file


@click.group(hidden=True)
def register():
    """
    Register flows
    """


@register.command(
    hidden=True,
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
@click.option(
    "--file",
    "-f",
    required=True,
    help="A file that contains a flow",
    hidden=True,
    default=None,
    type=click.Path(exists=True),
)
@click.option(
    "--name",
    "-n",
    required=False,
    help="The name of a flow to pull out of the file provided.",
    hidden=True,
    default=None,
)
@click.option(
    "--project",
    "-p",
    required=False,
    help="The name of a Prefect Cloud project to register this flow.",
    hidden=True,
    default=None,
)
def flow(file, name, project):
    """
    Register a flow from a file. This call will pull a Flow object out of a `.py` file
    and call `flow.register` on it.

    \b
    Options:
        --file, -f      TEXT    The path to a local file which contains a flow  [required]
        --name, -n      TEXT    The name of a flow to pull out of the file provided. If a name
                                is not provided then the first flow object found will be registered.
        --project       TEXT    The name of a Prefect Cloud project to register this flow

    \b
    Examples:
        $ prefect register flow --file my_flow.py --name My-Flow
    """
    file_path = os.path.abspath(file)
    flow_obj = extract_flow_from_file(file_path=file_path, flow_name=name)

    flow_obj.register(project_name=project)
