* Модель: BAAI/bge-m3
* Ссылка: https://huggingface.co/BAAI/bge-m3
* Размер эмбеддингов: 1024
* Чанкинг:
    * Используем RecursiveCharacterTextSplitter из langchain-text-splitters.
    * Держим размер ~100–300 слов (удобно для RAG), с overlap ~30–50 слов.
    * Разделители: заголовки/абзацы → ["\n## ", "\n### ", "\n\n", "\n", " ", ""].
    * Сохраняем оригинальный источник и позицию: doc_path, doc_id, title, chunk_id (стабильный)


`
py -m pip install langchain-text-splitters
py build_index.py --kb_dir "C:\practicum\am-ml\Task2" --out_dir "C:\practicum\am-ml\Task3\faiss_index" --pattern "**/*.md" --model "BAAI/bge-m3"
`
1/1 [00:33<00:00, 33.48s/it]

## запрос
`
py query.py --index_dir "C:\practicum\am-ml\Task3\faiss_index" --query "Кто управляет Turbo Scooter?" --top_k 5
`

## ответ

`
{
"query": "Кто управляет Turbo Scooter?",
"results": [
{
"rank": 1,
"score": 0.5786,
"chunk_id": "ep/s01e17-broken-zord::chunk-0000",
"title": "Broken Zord",
"path": "C:\\practicum\\am-ml\\Task2\\s01e17-broken-zord.md"
},
{
"rank": 2,
"score": 0.4565,
"chunk_id": "tech/zords/tubby-zords::chunk-0000",
"title": "Tubby-Zords",
"path": "C:\\practicum\\am-ml\\Task2\\tubby-zords.md"
},
{
"rank": 3,
"score": 0.4387,
"chunk_id": "canon/00-overview::chunk-0000",
"title": "Teletubby Rangers — Overview",
"path": "C:\\practicum\\am-ml\\Task2\\overview.md"
},
{
"rank": 4,
"score": 0.4311,
"chunk_id": "ep/s01e23-core-collapse::chunk-0000",
"title": "Core Collapse",
"path": "C:\\practicum\\am-ml\\Task2\\s01e23-core-collapse.md"
},
{
"rank": 5,
"score": 0.416,
"chunk_id": "ep/s01e16-rise-of-vacuum-king::chunk-0000",
"title": "Rise of the Vacuum King",
"path": "C:\\practicum\\am-ml\\Task2\\s01e16-rise-of-vacuum-king.md"
}
]
}
`