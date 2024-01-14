add_geo_namespaces("**/*.geo.json", namespace) + add_animation_namespaces("**/*.animation.json", namespace) + [
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
        "source": "visuals/*.namespaced.entity.png",
        "target": AUTO_FLAT
    },
    # Entity definition
    {
        "source": "snail.behavior.json",
        "target": AUTO_FLAT,
        "json_template": True
    },
    {
        "source": "snail.entity.json",
        "target": AUTO_FLAT,
        "json_template": True
    }
]