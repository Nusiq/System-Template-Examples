[
    # Visuals
    {
        "source": "visuals/*.geo.json",
        "target": AUTO_FLAT
    },
    
    {
        "source": "visuals/*.animation.json",
        "target": AUTO_FLAT
    },
    {
        "source": "visuals/ore_golem_*.entity.png",
        "target": AUTO_FLAT
    },
    # Entity definition
    {
        "source": "ore_golem.behavior.json",
        "target": AUTO_FLAT,
        "json_template": True,
        "scope": {
            "variants": [
                p.stem.removeprefix('ore_golem_').removesuffix('.entity')
                for p in Path("visuals").glob("ore_golem_*.entity.png")
            ]
        }
    },
    {
        "source": "ore_golem.entity.json",
        "target": AUTO_FLAT,
        "json_template": True,
        "scope": {
            "variants": [
                p.stem.removeprefix('ore_golem_').removesuffix('.entity')
                for p in Path("visuals").glob("ore_golem_*.entity.png")
            ]
        }
    },
    {
        "source": "ore_golem.rp_ac.json",
        "target": AUTO_FLAT
    },
    {
        "source": "ore_golem.rc.json",
        "target": AUTO_FLAT,
        "json_template": True,
        "scope": {
            "variants": [
                p.stem.removeprefix('ore_golem_').removesuffix('.entity')
                for p in Path("visuals").glob("ore_golem_*.entity.png")
            ]
        }
    },
]