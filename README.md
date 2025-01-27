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

PS> cat in.txt
琴瑟相和
飲鴆止渇
PS> uv run .\yomi.py in.txt
PS> cat .\out\out.txt
琴瑟相和	キンシツショウワ	琴瑟(キンシツ) / 相(ショウ) / 和(ワ)
飲鴆止渇	イン鴆止カツ	飲(イン) / 鴆止(?) / 渇(カツ)
```

---

[Sudachi](https://github.com/WorksApplications/Sudachi) and [SudachiDict](https://github.com/WorksApplications/SudachiDict) is licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .
