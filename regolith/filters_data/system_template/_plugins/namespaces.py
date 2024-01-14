from pathlib import Path
from better_json_tools import load_jsonc
import json
from typing import Any

def add_geo_namespaces(pattern: str, namespace: str) -> list[Any]:
    '''
    Walks model files matching the given pattern and adds a namespace prefix
    to the geometry identifiers.

    Example: geometry.my_entity -> geometry.my_namespace_my_entity
    '''
    for file in Path(".").glob(pattern):
        file_walker = load_jsonc(file)
        for desc in file_walker / "minecraft:geometry" // int / "description":
            identifier: str = desc.data["identifier"]  # type: ignore
            # Geometry identifiers are like "geometry.[name]", we're changing
            # that to "geometry.[namespace]_[name]".
            desc.data["identifier"]  = (
                "geometry." + namespace + "_" +
                identifier.removeprefix("geometry."))
        with file.open('w', encoding='utf8') as f:
            json.dump(file_walker.data, f, indent='\t')
    return []

def add_animation_namespaces(pattern: str, namespace: str) -> list[Any]:
    '''
    Walks animation files matching the given pattern and adds a namespace
    prefix to the animation identifiers.

    Example: animation.my_animation -> animation.my_namespace.my_animation
    '''
    for file in Path(".").glob(pattern):
        anim_file_data: dict[str, Any] = load_jsonc(file).data  # type: ignore
        for k in list(anim_file_data["animations"].keys()):
            # Animation identifiers are like "animation.[name]", we're changing
            # that to "animation.[namespace].[name]".
            identifier: str = k
            anim_file_data["animations"][
                "animation." +
                namespace + "." +
                identifier.removeprefix("animation.")
            ] = anim_file_data["animations"].pop(k)
        with file.open('w', encoding='utf8') as f:
            json.dump(anim_file_data, f, indent='\t')
    return []