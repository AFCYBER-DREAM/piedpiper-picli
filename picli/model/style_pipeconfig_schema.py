from marshmallow import fields
from marshmallow import Schema
from marshmallow import RAISE
from marshmallow import ValidationError


class PiStylePipeVarsSchema(Schema):
    run_pipe = fields.Bool(required=True)
    url = fields.Str(required=True)
    version = fields.Str(required=True)


class StylePipeConfigSchema(Schema):
    pi_style_pipe_vars = fields.Nested(PiStylePipeVarsSchema)


def validate(config):
    schema = StylePipeConfigSchema(unknown=RAISE)
    try:
        _ = schema.load(config)
        result = None
    except ValidationError as err:
        result = err
    return result
