/**
 * Autogenerated by Thrift Compiler (1.0.0-dev)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package qudt4dt.thrift;

import org.apache.thrift.scheme.IScheme;
import org.apache.thrift.scheme.SchemeFactory;
import org.apache.thrift.scheme.StandardScheme;

import org.apache.thrift.scheme.TupleScheme;
import org.apache.thrift.protocol.TTupleProtocol;
import org.apache.thrift.protocol.TProtocolException;
import org.apache.thrift.EncodingUtils;
import org.apache.thrift.TException;
import org.apache.thrift.async.AsyncMethodCallback;
import org.apache.thrift.server.AbstractNonblockingServer.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import javax.annotation.Generated;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked"})
@Generated(value = "Autogenerated by Thrift Compiler (1.0.0-dev)", date = "2014-5-9")
public class QudtUnit implements org.apache.thrift.TBase<QudtUnit, QudtUnit._Fields>, java.io.Serializable, Cloneable, Comparable<QudtUnit> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("QudtUnit");

  private static final org.apache.thrift.protocol.TField URL_FIELD_DESC = new org.apache.thrift.protocol.TField("url", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField UNIT_NAME_FIELD_DESC = new org.apache.thrift.protocol.TField("unitName", org.apache.thrift.protocol.TType.STRING, (short)2);
  private static final org.apache.thrift.protocol.TField SYMBOL_FIELD_DESC = new org.apache.thrift.protocol.TField("symbol", org.apache.thrift.protocol.TType.STRING, (short)3);
  private static final org.apache.thrift.protocol.TField UNIT_CLASS_FIELD_DESC = new org.apache.thrift.protocol.TField("unitClass", org.apache.thrift.protocol.TType.STRING, (short)4);
  private static final org.apache.thrift.protocol.TField ABBREVIATION_FIELD_DESC = new org.apache.thrift.protocol.TField("abbreviation", org.apache.thrift.protocol.TType.STRING, (short)5);
  private static final org.apache.thrift.protocol.TField FACTOR_FIELD_DESC = new org.apache.thrift.protocol.TField("factor", org.apache.thrift.protocol.TType.DOUBLE, (short)6);
  private static final org.apache.thrift.protocol.TField OFFSET_FIELD_DESC = new org.apache.thrift.protocol.TField("offset", org.apache.thrift.protocol.TType.DOUBLE, (short)7);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new QudtUnitStandardSchemeFactory());
    schemes.put(TupleScheme.class, new QudtUnitTupleSchemeFactory());
  }

  public String url; // required
  public String unitName; // required
  public String symbol; // required
  public String unitClass; // required
  public String abbreviation; // required
  public double factor; // optional
  public double offset; // optional

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    URL((short)1, "url"),
    UNIT_NAME((short)2, "unitName"),
    SYMBOL((short)3, "symbol"),
    UNIT_CLASS((short)4, "unitClass"),
    ABBREVIATION((short)5, "abbreviation"),
    FACTOR((short)6, "factor"),
    OFFSET((short)7, "offset");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // URL
          return URL;
        case 2: // UNIT_NAME
          return UNIT_NAME;
        case 3: // SYMBOL
          return SYMBOL;
        case 4: // UNIT_CLASS
          return UNIT_CLASS;
        case 5: // ABBREVIATION
          return ABBREVIATION;
        case 6: // FACTOR
          return FACTOR;
        case 7: // OFFSET
          return OFFSET;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final int __FACTOR_ISSET_ID = 0;
  private static final int __OFFSET_ISSET_ID = 1;
  private byte __isset_bitfield = 0;
  private static final _Fields optionals[] = {_Fields.FACTOR,_Fields.OFFSET};
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.URL, new org.apache.thrift.meta_data.FieldMetaData("url", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.UNIT_NAME, new org.apache.thrift.meta_data.FieldMetaData("unitName", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.SYMBOL, new org.apache.thrift.meta_data.FieldMetaData("symbol", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.UNIT_CLASS, new org.apache.thrift.meta_data.FieldMetaData("unitClass", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.ABBREVIATION, new org.apache.thrift.meta_data.FieldMetaData("abbreviation", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.FACTOR, new org.apache.thrift.meta_data.FieldMetaData("factor", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.DOUBLE)));
    tmpMap.put(_Fields.OFFSET, new org.apache.thrift.meta_data.FieldMetaData("offset", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.DOUBLE)));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(QudtUnit.class, metaDataMap);
  }

  public QudtUnit() {
    this.unitName = "";

    this.symbol = "";

    this.unitClass = "";

    this.abbreviation = "";

  }

  public QudtUnit(
    String url,
    String unitName,
    String symbol,
    String unitClass,
    String abbreviation)
  {
    this();
    this.url = url;
    this.unitName = unitName;
    this.symbol = symbol;
    this.unitClass = unitClass;
    this.abbreviation = abbreviation;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public QudtUnit(QudtUnit other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetUrl()) {
      this.url = other.url;
    }
    if (other.isSetUnitName()) {
      this.unitName = other.unitName;
    }
    if (other.isSetSymbol()) {
      this.symbol = other.symbol;
    }
    if (other.isSetUnitClass()) {
      this.unitClass = other.unitClass;
    }
    if (other.isSetAbbreviation()) {
      this.abbreviation = other.abbreviation;
    }
    this.factor = other.factor;
    this.offset = other.offset;
  }

  public QudtUnit deepCopy() {
    return new QudtUnit(this);
  }

  @Override
  public void clear() {
    this.url = null;
    this.unitName = "";

    this.symbol = "";

    this.unitClass = "";

    this.abbreviation = "";

    setFactorIsSet(false);
    this.factor = 0.0;
    setOffsetIsSet(false);
    this.offset = 0.0;
  }

  public String getUrl() {
    return this.url;
  }

  public QudtUnit setUrl(String url) {
    this.url = url;
    return this;
  }

  public void unsetUrl() {
    this.url = null;
  }

  /** Returns true if field url is set (has been assigned a value) and false otherwise */
  public boolean isSetUrl() {
    return this.url != null;
  }

  public void setUrlIsSet(boolean value) {
    if (!value) {
      this.url = null;
    }
  }

  public String getUnitName() {
    return this.unitName;
  }

  public QudtUnit setUnitName(String unitName) {
    this.unitName = unitName;
    return this;
  }

  public void unsetUnitName() {
    this.unitName = null;
  }

  /** Returns true if field unitName is set (has been assigned a value) and false otherwise */
  public boolean isSetUnitName() {
    return this.unitName != null;
  }

  public void setUnitNameIsSet(boolean value) {
    if (!value) {
      this.unitName = null;
    }
  }

  public String getSymbol() {
    return this.symbol;
  }

  public QudtUnit setSymbol(String symbol) {
    this.symbol = symbol;
    return this;
  }

  public void unsetSymbol() {
    this.symbol = null;
  }

  /** Returns true if field symbol is set (has been assigned a value) and false otherwise */
  public boolean isSetSymbol() {
    return this.symbol != null;
  }

  public void setSymbolIsSet(boolean value) {
    if (!value) {
      this.symbol = null;
    }
  }

  public String getUnitClass() {
    return this.unitClass;
  }

  public QudtUnit setUnitClass(String unitClass) {
    this.unitClass = unitClass;
    return this;
  }

  public void unsetUnitClass() {
    this.unitClass = null;
  }

  /** Returns true if field unitClass is set (has been assigned a value) and false otherwise */
  public boolean isSetUnitClass() {
    return this.unitClass != null;
  }

  public void setUnitClassIsSet(boolean value) {
    if (!value) {
      this.unitClass = null;
    }
  }

  public String getAbbreviation() {
    return this.abbreviation;
  }

  public QudtUnit setAbbreviation(String abbreviation) {
    this.abbreviation = abbreviation;
    return this;
  }

  public void unsetAbbreviation() {
    this.abbreviation = null;
  }

  /** Returns true if field abbreviation is set (has been assigned a value) and false otherwise */
  public boolean isSetAbbreviation() {
    return this.abbreviation != null;
  }

  public void setAbbreviationIsSet(boolean value) {
    if (!value) {
      this.abbreviation = null;
    }
  }

  public double getFactor() {
    return this.factor;
  }

  public QudtUnit setFactor(double factor) {
    this.factor = factor;
    setFactorIsSet(true);
    return this;
  }

  public void unsetFactor() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __FACTOR_ISSET_ID);
  }

  /** Returns true if field factor is set (has been assigned a value) and false otherwise */
  public boolean isSetFactor() {
    return EncodingUtils.testBit(__isset_bitfield, __FACTOR_ISSET_ID);
  }

  public void setFactorIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __FACTOR_ISSET_ID, value);
  }

  public double getOffset() {
    return this.offset;
  }

  public QudtUnit setOffset(double offset) {
    this.offset = offset;
    setOffsetIsSet(true);
    return this;
  }

  public void unsetOffset() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __OFFSET_ISSET_ID);
  }

  /** Returns true if field offset is set (has been assigned a value) and false otherwise */
  public boolean isSetOffset() {
    return EncodingUtils.testBit(__isset_bitfield, __OFFSET_ISSET_ID);
  }

  public void setOffsetIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __OFFSET_ISSET_ID, value);
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case URL:
      if (value == null) {
        unsetUrl();
      } else {
        setUrl((String)value);
      }
      break;

    case UNIT_NAME:
      if (value == null) {
        unsetUnitName();
      } else {
        setUnitName((String)value);
      }
      break;

    case SYMBOL:
      if (value == null) {
        unsetSymbol();
      } else {
        setSymbol((String)value);
      }
      break;

    case UNIT_CLASS:
      if (value == null) {
        unsetUnitClass();
      } else {
        setUnitClass((String)value);
      }
      break;

    case ABBREVIATION:
      if (value == null) {
        unsetAbbreviation();
      } else {
        setAbbreviation((String)value);
      }
      break;

    case FACTOR:
      if (value == null) {
        unsetFactor();
      } else {
        setFactor((Double)value);
      }
      break;

    case OFFSET:
      if (value == null) {
        unsetOffset();
      } else {
        setOffset((Double)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case URL:
      return getUrl();

    case UNIT_NAME:
      return getUnitName();

    case SYMBOL:
      return getSymbol();

    case UNIT_CLASS:
      return getUnitClass();

    case ABBREVIATION:
      return getAbbreviation();

    case FACTOR:
      return Double.valueOf(getFactor());

    case OFFSET:
      return Double.valueOf(getOffset());

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case URL:
      return isSetUrl();
    case UNIT_NAME:
      return isSetUnitName();
    case SYMBOL:
      return isSetSymbol();
    case UNIT_CLASS:
      return isSetUnitClass();
    case ABBREVIATION:
      return isSetAbbreviation();
    case FACTOR:
      return isSetFactor();
    case OFFSET:
      return isSetOffset();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof QudtUnit)
      return this.equals((QudtUnit)that);
    return false;
  }

  public boolean equals(QudtUnit that) {
    if (that == null)
      return false;

    boolean this_present_url = true && this.isSetUrl();
    boolean that_present_url = true && that.isSetUrl();
    if (this_present_url || that_present_url) {
      if (!(this_present_url && that_present_url))
        return false;
      if (!this.url.equals(that.url))
        return false;
    }

    boolean this_present_unitName = true && this.isSetUnitName();
    boolean that_present_unitName = true && that.isSetUnitName();
    if (this_present_unitName || that_present_unitName) {
      if (!(this_present_unitName && that_present_unitName))
        return false;
      if (!this.unitName.equals(that.unitName))
        return false;
    }

    boolean this_present_symbol = true && this.isSetSymbol();
    boolean that_present_symbol = true && that.isSetSymbol();
    if (this_present_symbol || that_present_symbol) {
      if (!(this_present_symbol && that_present_symbol))
        return false;
      if (!this.symbol.equals(that.symbol))
        return false;
    }

    boolean this_present_unitClass = true && this.isSetUnitClass();
    boolean that_present_unitClass = true && that.isSetUnitClass();
    if (this_present_unitClass || that_present_unitClass) {
      if (!(this_present_unitClass && that_present_unitClass))
        return false;
      if (!this.unitClass.equals(that.unitClass))
        return false;
    }

    boolean this_present_abbreviation = true && this.isSetAbbreviation();
    boolean that_present_abbreviation = true && that.isSetAbbreviation();
    if (this_present_abbreviation || that_present_abbreviation) {
      if (!(this_present_abbreviation && that_present_abbreviation))
        return false;
      if (!this.abbreviation.equals(that.abbreviation))
        return false;
    }

    boolean this_present_factor = true && this.isSetFactor();
    boolean that_present_factor = true && that.isSetFactor();
    if (this_present_factor || that_present_factor) {
      if (!(this_present_factor && that_present_factor))
        return false;
      if (this.factor != that.factor)
        return false;
    }

    boolean this_present_offset = true && this.isSetOffset();
    boolean that_present_offset = true && that.isSetOffset();
    if (this_present_offset || that_present_offset) {
      if (!(this_present_offset && that_present_offset))
        return false;
      if (this.offset != that.offset)
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    List<Object> list = new ArrayList<Object>();

    boolean present_url = true && (isSetUrl());
    list.add(present_url);
    if (present_url)
      list.add(url);

    boolean present_unitName = true && (isSetUnitName());
    list.add(present_unitName);
    if (present_unitName)
      list.add(unitName);

    boolean present_symbol = true && (isSetSymbol());
    list.add(present_symbol);
    if (present_symbol)
      list.add(symbol);

    boolean present_unitClass = true && (isSetUnitClass());
    list.add(present_unitClass);
    if (present_unitClass)
      list.add(unitClass);

    boolean present_abbreviation = true && (isSetAbbreviation());
    list.add(present_abbreviation);
    if (present_abbreviation)
      list.add(abbreviation);

    boolean present_factor = true && (isSetFactor());
    list.add(present_factor);
    if (present_factor)
      list.add(factor);

    boolean present_offset = true && (isSetOffset());
    list.add(present_offset);
    if (present_offset)
      list.add(offset);

    return list.hashCode();
  }

  @Override
  public int compareTo(QudtUnit other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetUrl()).compareTo(other.isSetUrl());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUrl()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.url, other.url);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetUnitName()).compareTo(other.isSetUnitName());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUnitName()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.unitName, other.unitName);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetSymbol()).compareTo(other.isSetSymbol());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetSymbol()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.symbol, other.symbol);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetUnitClass()).compareTo(other.isSetUnitClass());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUnitClass()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.unitClass, other.unitClass);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetAbbreviation()).compareTo(other.isSetAbbreviation());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetAbbreviation()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.abbreviation, other.abbreviation);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetFactor()).compareTo(other.isSetFactor());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetFactor()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.factor, other.factor);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetOffset()).compareTo(other.isSetOffset());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetOffset()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.offset, other.offset);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    schemes.get(iprot.getScheme()).getScheme().read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    schemes.get(oprot.getScheme()).getScheme().write(oprot, this);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("QudtUnit(");
    boolean first = true;

    sb.append("url:");
    if (this.url == null) {
      sb.append("null");
    } else {
      sb.append(this.url);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("unitName:");
    if (this.unitName == null) {
      sb.append("null");
    } else {
      sb.append(this.unitName);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("symbol:");
    if (this.symbol == null) {
      sb.append("null");
    } else {
      sb.append(this.symbol);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("unitClass:");
    if (this.unitClass == null) {
      sb.append("null");
    } else {
      sb.append(this.unitClass);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("abbreviation:");
    if (this.abbreviation == null) {
      sb.append("null");
    } else {
      sb.append(this.abbreviation);
    }
    first = false;
    if (isSetFactor()) {
      if (!first) sb.append(", ");
      sb.append("factor:");
      sb.append(this.factor);
      first = false;
    }
    if (isSetOffset()) {
      if (!first) sb.append(", ");
      sb.append("offset:");
      sb.append(this.offset);
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class QudtUnitStandardSchemeFactory implements SchemeFactory {
    public QudtUnitStandardScheme getScheme() {
      return new QudtUnitStandardScheme();
    }
  }

  private static class QudtUnitStandardScheme extends StandardScheme<QudtUnit> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, QudtUnit struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // URL
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.url = iprot.readString();
              struct.setUrlIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // UNIT_NAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.unitName = iprot.readString();
              struct.setUnitNameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // SYMBOL
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.symbol = iprot.readString();
              struct.setSymbolIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // UNIT_CLASS
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.unitClass = iprot.readString();
              struct.setUnitClassIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 5: // ABBREVIATION
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.abbreviation = iprot.readString();
              struct.setAbbreviationIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 6: // FACTOR
            if (schemeField.type == org.apache.thrift.protocol.TType.DOUBLE) {
              struct.factor = iprot.readDouble();
              struct.setFactorIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 7: // OFFSET
            if (schemeField.type == org.apache.thrift.protocol.TType.DOUBLE) {
              struct.offset = iprot.readDouble();
              struct.setOffsetIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, QudtUnit struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.url != null) {
        oprot.writeFieldBegin(URL_FIELD_DESC);
        oprot.writeString(struct.url);
        oprot.writeFieldEnd();
      }
      if (struct.unitName != null) {
        oprot.writeFieldBegin(UNIT_NAME_FIELD_DESC);
        oprot.writeString(struct.unitName);
        oprot.writeFieldEnd();
      }
      if (struct.symbol != null) {
        oprot.writeFieldBegin(SYMBOL_FIELD_DESC);
        oprot.writeString(struct.symbol);
        oprot.writeFieldEnd();
      }
      if (struct.unitClass != null) {
        oprot.writeFieldBegin(UNIT_CLASS_FIELD_DESC);
        oprot.writeString(struct.unitClass);
        oprot.writeFieldEnd();
      }
      if (struct.abbreviation != null) {
        oprot.writeFieldBegin(ABBREVIATION_FIELD_DESC);
        oprot.writeString(struct.abbreviation);
        oprot.writeFieldEnd();
      }
      if (struct.isSetFactor()) {
        oprot.writeFieldBegin(FACTOR_FIELD_DESC);
        oprot.writeDouble(struct.factor);
        oprot.writeFieldEnd();
      }
      if (struct.isSetOffset()) {
        oprot.writeFieldBegin(OFFSET_FIELD_DESC);
        oprot.writeDouble(struct.offset);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class QudtUnitTupleSchemeFactory implements SchemeFactory {
    public QudtUnitTupleScheme getScheme() {
      return new QudtUnitTupleScheme();
    }
  }

  private static class QudtUnitTupleScheme extends TupleScheme<QudtUnit> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, QudtUnit struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetUrl()) {
        optionals.set(0);
      }
      if (struct.isSetUnitName()) {
        optionals.set(1);
      }
      if (struct.isSetSymbol()) {
        optionals.set(2);
      }
      if (struct.isSetUnitClass()) {
        optionals.set(3);
      }
      if (struct.isSetAbbreviation()) {
        optionals.set(4);
      }
      if (struct.isSetFactor()) {
        optionals.set(5);
      }
      if (struct.isSetOffset()) {
        optionals.set(6);
      }
      oprot.writeBitSet(optionals, 7);
      if (struct.isSetUrl()) {
        oprot.writeString(struct.url);
      }
      if (struct.isSetUnitName()) {
        oprot.writeString(struct.unitName);
      }
      if (struct.isSetSymbol()) {
        oprot.writeString(struct.symbol);
      }
      if (struct.isSetUnitClass()) {
        oprot.writeString(struct.unitClass);
      }
      if (struct.isSetAbbreviation()) {
        oprot.writeString(struct.abbreviation);
      }
      if (struct.isSetFactor()) {
        oprot.writeDouble(struct.factor);
      }
      if (struct.isSetOffset()) {
        oprot.writeDouble(struct.offset);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, QudtUnit struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(7);
      if (incoming.get(0)) {
        struct.url = iprot.readString();
        struct.setUrlIsSet(true);
      }
      if (incoming.get(1)) {
        struct.unitName = iprot.readString();
        struct.setUnitNameIsSet(true);
      }
      if (incoming.get(2)) {
        struct.symbol = iprot.readString();
        struct.setSymbolIsSet(true);
      }
      if (incoming.get(3)) {
        struct.unitClass = iprot.readString();
        struct.setUnitClassIsSet(true);
      }
      if (incoming.get(4)) {
        struct.abbreviation = iprot.readString();
        struct.setAbbreviationIsSet(true);
      }
      if (incoming.get(5)) {
        struct.factor = iprot.readDouble();
        struct.setFactorIsSet(true);
      }
      if (incoming.get(6)) {
        struct.offset = iprot.readDouble();
        struct.setOffsetIsSet(true);
      }
    }
  }

}

