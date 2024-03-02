from langchain_community.graphs import __all__

EXPECTED_ALL = [
    "MemgraphGraph",
    "NetworkxEntityGraph",
    "Neo4jGraph",
    "NebulaGraph",
    "NeptuneGraph",
    "NeptuneRdfGraph",
    "KuzuGraph",
    "HugeGraph",
    "RdfGraph",
    "ArangoGraph",
    "FalkorDBGraph",
    "TigerGraph",
    "OntotextGraphDBGraph",
    "GremlinGraph",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
