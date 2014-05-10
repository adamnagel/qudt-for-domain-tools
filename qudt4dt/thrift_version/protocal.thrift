namespace cpp        qudt4dt.thrift
namespace java       qudt4dt.thrift
namespace csharp     qudt4dt.thrift
namespace js         qudt4dt.thrift
namespace py         qudt4dt.thrift


struct QudtUnit {
    1: string url,
    2: string unitName = "", 
    3: string symbol = "",
    4: string unitClass = "",
    5: string abbreviation = "",
    6: optional double factor,
    7: optional double offset,
}

struct ModelicaUnit {
    1: string url,
    2: string classPath,
    3: optional double max,
    4: optional double min,
    5: optional double start,
    6: string displayUnit = "",
    7: string quantity = "",
}

struct MdaoUnit {
    1: string url,
    2: string name,
    3: string expression = "",
    4: string comment = "",
}

struct Unit {
    1: string url,
    2: optional QudtUnit qudt_u,
    3: optional ModelicaUnit modelica_u,
    4: optional MdaoUnit mdao_u,
}
service Qudt4dt{
    Unit query(1: string url),
}