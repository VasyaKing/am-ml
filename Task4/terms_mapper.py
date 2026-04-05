import json, re
from pathlib import Path
from typing import Dict, Literal

Mode = Literal["annotate", "replace"]

TERMS_MAP_PATH = Path(r"C:\practicum\am-ml\Task2\terms_map.json")

def _preserve_case(src: str, repl: str) -> str:
    if not src:
        return repl
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl

def compile_patterns(terms: Dict[str, str]):
    patterns = []
    for k, v in terms.items():
        pat = r"\b" + re.escape(k) + r"\b"
        patterns.append((re.compile(pat, re.IGNORECASE), k, v))
    return patterns

class TermsMapper:
    def __init__(self, map_path: Path = TERMS_MAP_PATH):
        data = json.loads(map_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("terms_map.json must be a dict {term: explanation}")
        self.terms = data
        self.patterns = compile_patterns(self.terms)

    def transform(self, text: str, mode: Mode = "annotate") -> str:
        def _repl(m, key, expl):
            src = m.group(0)
            if mode == "replace":
                return _preserve_case(src, expl)
            if re.search(r"\s*\(", text[max(0, m.start()-1):m.end()+1]):
                return src
            return f"{src} ({expl})"

        out = text
        for rgx, key, expl in self.patterns:
            out = rgx.sub(lambda m: _repl(m, key, expl), out)
        return out

if __name__ == "__main__":
    import sys
    mapper = TermsMapper()
    txt = sys.stdin.read()
    print(mapper.transform(txt, mode="annotate"))
