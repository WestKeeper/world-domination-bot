from typing import Any, Dict, Optional

import jinja2

from common.config import TEMPLATES_DIR


def render_template(template_name: str, data: Optional[Dict[str, Any]] = None) -> str:
    if data is None:
        data = {}

    template = _get_template_env().get_template(template_name)
    rendered = template.render(**data).replace('\n', '')
    rendered = rendered.replace('<br>', '\n')

    return rendered


def _get_template_env():
    if not getattr(_get_template_env, 'template_env', None):
        template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
        env = jinja2.Environment(loader=template_loader, trim_blocks=True, lstrip_blocks=True)
        setattr(
            _get_template_env,
            'template_env',
            env,
        )

    return getattr(_get_template_env, 'template_env')
