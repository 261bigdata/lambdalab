from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_DIR = ROOT / "pyspark" / "notebooks"
DOCS_DIR = ROOT / "docs"
INDEX_SOURCE = NOTEBOOKS_DIR / "index.md"

NOTEBOOKS = {
    "unidad-1": [
        ("01_arquitecturas_big_data.ipynb", "01_arquitecturas_big_data.md"),
        ("02_fundamentos_practica.ipynb", "02_fundamentos_spark.md"),
        ("03_etl_spark.ipynb", "03_etl_spark.md"),
        ("04_hdfs_formatos.ipynb", "04_hdfs_formatos.md"),
    ],
    "unidad-2": [
        ("07_spark_streaming_consumer_ordenes.ipynb", "08_spark_streaming.md"),
        ("08_observabilidad_pipeline_kafka_spark.ipynb", "09_observabilidad_costos.md"),
        ("09_ml_distribuido_regresion_mllib.ipynb", "10_bi_ml_distribuido_spark.md"),
        ("10_series_tiempo_inferencia_spark.ipynb", "11_series_tiempo_inferencia_spark.md"),
    ],
}

STATIC_PAGES = {
    "index.md": None,
    "unidad-1/05_evaluacion_u1.md": "# Evaluacion U1\n\nProducto: pipeline batch en Spark con dataset listo para BI/ML.\n",
    "unidad-2/06_ingesta_kafka.md": "06_ingesta_kafka.md",
    "unidad-2/07_ingesta_sensores.md": "07_ingesta_sensores.md",
    "unidad-2/12_evaluacion_u2.md": "12_evaluacion_u2.md",
    "unidad-2/12_plantilla_entregable_u2.md": "12_plantilla_entregable_u2.md",
}

APPEND_PAGES = {
    "unidad-2/08_spark_streaming.md": [
        "07_spark_streaming_guia.md",
    ],
    "unidad-2/09_observabilidad_costos.md": [
        "08_costos_escalado.md",
    ],
}


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return source


def convert_notebook(path: Path) -> str:
    notebook = json.loads(path.read_text(encoding="utf-8-sig"))
    chunks: list[str] = []

    for cell in notebook.get("cells", []):
        source = cell_source(cell).rstrip()
        if not source.strip():
            continue

        if cell.get("cell_type") == "markdown":
            chunks.append(source)
        elif cell.get("cell_type") == "code":
            chunks.append(f"```python\n{source}\n```")

    return "\n\n".join(chunks).rstrip() + "\n"


def main() -> None:
    for unit, notebooks in NOTEBOOKS.items():
        output_dir = DOCS_DIR / unit
        output_dir.mkdir(parents=True, exist_ok=True)

        for notebook_name, markdown_name in notebooks:
            notebook_path = NOTEBOOKS_DIR / notebook_name
            if not notebook_path.exists():
                raise FileNotFoundError(f"No existe {notebook_path}")

            markdown_path = output_dir / markdown_name
            markdown_path.write_text(convert_notebook(notebook_path), encoding="utf-8")
            print(f"Exportado {notebook_path.relative_to(ROOT)} -> {markdown_path.relative_to(ROOT)}")

    for relative_path, content in STATIC_PAGES.items():
        output_path = DOCS_DIR / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if content is None:
            if not INDEX_SOURCE.exists():
                raise FileNotFoundError(f"No existe {INDEX_SOURCE}")
            content = INDEX_SOURCE.read_text(encoding="utf-8")
        elif content.endswith(".md"):
            source_path = NOTEBOOKS_DIR / content
            if not source_path.exists():
                raise FileNotFoundError(f"No existe {source_path}")
            content = source_path.read_text(encoding="utf-8")
        output_path.write_text(content, encoding="utf-8")
        print(f"Generado {output_path.relative_to(ROOT)}")

    for relative_path, source_names in APPEND_PAGES.items():
        output_path = DOCS_DIR / relative_path
        if not output_path.exists():
            raise FileNotFoundError(f"No existe {output_path}")
        chunks = [output_path.read_text(encoding="utf-8").rstrip()]
        for source_name in source_names:
            source_path = NOTEBOOKS_DIR / source_name
            if not source_path.exists():
                raise FileNotFoundError(f"No existe {source_path}")
            chunks.append(source_path.read_text(encoding="utf-8").strip())
        output_path.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")
        print(f"Actualizado {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
