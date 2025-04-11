from parse import parse

class FormattedFilename:

    def __init__(self, filename_stem:str, pattern:str):
        self._filename_stem = filename_stem
        self._pattern = pattern
        self._parsed_filename = self._parse_filename()

    def _parse_filename(self):
        parsed = parse(self._pattern, self._filename_stem)
        if not parsed:
            raise ValueError(f"Filename '{self._filename_stem}' does not match pattern '{self._pattern}'")
        return parsed.named

    def format(self, output_pattern: str) -> str:
        return output_pattern.format(**self._parsed_filename)