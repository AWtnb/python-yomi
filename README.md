# README

```
PS> echo 水魚の交わり | scb
PS> uv run .\yomi.py
PS> cat .\out\out.txt
水魚の交わり	スイギョノマジワリ	水魚(スイギョ) / の / 交わり(マジワリ)
PS> cat .\out\out.txt|ConvertFrom-Csv -Delimiter "`t" -Header line,reading,detail

line         reading            detail
----         -------            ------
水魚の交わり スイギョノマジワリ 水魚(スイギョ) / の / 交わり(マジワリ)
```

---

[Sudachi](https://github.com/WorksApplications/Sudachi) and [SudachiDict](https://github.com/WorksApplications/SudachiDict) is licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .
