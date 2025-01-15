"""
   Copyright 2025 AWtnb

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import re
from pathlib import Path
from typing import List

import pyperclip
from sudachipy import Tokenizer, Dictionary, Morpheme


class SudachiToken:
    reg = re.compile(
        r"^([ぁ-んァ-ヴ・ー]|[a-zA-Z\uff41-\uff5a\uff21-\uff3a]|[0-9\uff10-\uff19]|[\W\s])+$"
    )

    def __init__(self, morpheme: Morpheme) -> None:
        self._surface = morpheme.surface()
        self._pos = morpheme.part_of_speech()[0]
        self._reading = morpheme.reading_form()

    @property
    def katakana_surface(self) -> str:
        return "".join(
            [
                chr(ord(c) + 96) if (0x3041 <= ord(c) and ord(c) <= 0x3094) else c
                for c in self._surface
            ]
        )

    def _is_verbatim(self) -> bool:
        return (
            "記号" in self._pos or "空白" in self._pos or self.reg.match(self._surface)
        )

    @property
    def reading(self) -> str:
        if self._is_verbatim():
            if re.match(r"[ぁ-ん]", self._surface):
                return self.katakana_surface
            return self._surface

        if len(self._reading) < 1:
            return self._surface

        return self._reading

    @property
    def detail(self) -> str:
        if self._is_verbatim():
            return self._surface

        if len(self._reading) < 1:
            return self._surface + "(?)"

        return "{}({})".format(self._surface, self._reading)


SUDACHI_TOKENIZER = Dictionary().create()


class ParsedLine:
    reg_paren = re.compile(r"\(.+?\)|\[.+?\]|\uff08.+?\uff09|\uff3b.+?\uff3d")
    reg_noise = re.compile(r"　　[^\d]?\d.*$|　→.+$")

    def __init__(self, line: str) -> None:
        self.raw_line = line
        self.line = line

    def trim_paren(self) -> None:
        self.line = self.reg_paren.sub("", self.line)

    def trim_noise(self) -> None:
        self.line = self.reg_noise.sub("", self.line)

    @property
    def tokens(self) -> List[SudachiToken]:
        if len(self.line.strip()) < 1:
            return []
        return [
            SudachiToken(morpheme)
            for morpheme in SUDACHI_TOKENIZER.tokenize(self.line, Tokenizer.SplitMode.C)
        ]


def main():
    lines = pyperclip.paste().splitlines()

    if len(lines) < 1:
        print("No text is copied on clipboard.")
        return

    out = []
    for line in lines:
        pl = ParsedLine(line)
        pl.trim_noise()
        pl.trim_paren()
        tokens = pl.tokens
        reading = "".join([token.reading for token in tokens])
        detail = " / ".join([token.detail for token in tokens])

        out.append("\t".join([line, reading, detail]))

    Path("out/out.txt").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
