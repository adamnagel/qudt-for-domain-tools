namespace cpp        qudt4dt.thrift
namespace java       qudt4dt.thrift
namespace csharp     qudt4dt.thrift
namespace js         qudt4dt.thrift
namespace py         qudt4dt.thrift

struct ModelicaAttr {
    1: string classPath,
    2: optional double max,
    3: optional double min,
    4: optional double start,
    5: string displayUnit = "",
    6: string quantity = "",
}

struct MdaoAttr {
    1: string name,
    2: string expression = "",
    3: string comment = "",
}

struct QudtAttr {
    1: string unitName = "", 
    2: string symbol = "",
    3: string unitClass = "",
    4: string abbreviation = "",
    5: optional double factor,
    6: optional double offset,
}

struct Unit {
    1: string url,
    2: string qudt_url,
//  3: map<string, string> domain_unit_urls,
    4: QudtAttr qudt_attr,    
}

struct Quantity {
    1: Unit unit,
    2: double value,
}

exception InvalidOperation {
    1: string why,
}

//const list<string,string> DOMAIN_CONST = {"modelica", "mdao",}

service Qudt4dt_base{
    Unit query(1: string url) throws (1: InvalidOperation err),
    Quantity quantity_convert(1: Quantity src, 2: string dst_url) throws(1: InvalidOperation err),
    map<string, Quantity> list_domain_unitset(1: Quantity input) throws(1 : InvalidOperation err),
}
