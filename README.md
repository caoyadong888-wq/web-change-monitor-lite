# Web Change Monitor (Lite)

## English

Compare two local files by SHA-256 of the raw bytes. The tool prints MATCH or DIFFER and both hashes.

This subset does not read HTML structure, does not keep a snapshot, does not write a diff, and does not fetch a URL.

### Deliverables

- `deliverables/compare_files.py` — raw SHA-256 compare
- `examples/page-a.html` — database line says up
- `examples/page-b.html` — database line says down

### Quick start

```bash
python3 deliverables/compare_files.py examples/page-a.html examples/page-b.html
```

Exit 0 on MATCH, 1 on DIFFER, 2 when a file cannot be read.

## 中文

按原始字节的 SHA-256 比较两个本地文件。工具打印 MATCH 或 DIFFER，以及两边的哈希。

精简版不解析 HTML 结构，不保存快照，不写 diff，也不抓取 URL。

### 交付文件

- `deliverables/compare_files.py` — 原始 SHA-256 比较
- `examples/page-a.html` — 数据库一行是 up
- `examples/page-b.html` — 数据库一行是 down

### 快速开始

```bash
python3 deliverables/compare_files.py examples/page-a.html examples/page-b.html
```

MATCH 时退出码为 0，DIFFER 时为 1，文件读不到时为 2。

Full version: GUMROAD_URL
