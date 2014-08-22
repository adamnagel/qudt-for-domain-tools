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
@Generated(value = "Autogenerated by Thrift Compiler (1.0.0-dev)", date = "2014-6-18")
public class ModelicaAttr implements org.apache.thrift.TBase<ModelicaAttr, ModelicaAttr._Fields>, java.io.Serializable, Cloneable, Comparable<ModelicaAttr> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ModelicaAttr");

  private static final org.apache.thrift.protocol.TField CLASS_PATH_FIELD_DESC = new org.apache.thrift.protocol.TField("classPath", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField MAX_FIELD_DESC = new org.apache.thrift.protocol.TField("max", org.apache.thrift.protocol.TType.DOUBLE, (short)2);
  private static final org.apache.thrift.protocol.TField MIN_FIELD_DESC = new org.apache.thrift.protocol.TField("min", org.apache.thrift.protocol.TType.DOUBLE, (short)3);
  private static final org.apache.thrift.protocol.TField START_FIELD_DESC = new org.apache.thrift.protocol.TField("start", org.apache.thrift.protocol.TType.DOUBLE, (short)4);
  private static final org.apache.thrift.protocol.TField DISPLAY_UNIT_FIELD_DESC = new org.apache.thrift.protocol.TField("displayUnit", org.apache.thrift.protocol.TType.STRING, (short)5);
  private static final org.apache.thrift.protocol.TField QUANTITY_FIELD_DESC = new org.apache.thrift.protocol.TField("quantity", org.apache.thrift.protocol.TType.STRING, (short)6);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new ModelicaAttrStandardSchemeFactory());
    schemes.put(TupleScheme.class, new ModelicaAttrTupleSchemeFactory());
  }

  public String classPath; // required
  public double max; // optional
  public double min; // optional
  public double start; // optional
  public String displayUnit; // required
  public String quantity; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    CLASS_PATH((short)1, "classPath"),
    MAX((short)2, "max"),
    MIN((short)3, "min"),
    START((short)4, "start"),
    DISPLAY_UNIT((short)5, "displayUnit"),
    QUANTITY((short)6, "quantity");

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
        case 1: // CLASS_PATH
          return CLASS_PATH;
        case 2: // MAX
          return MAX;
        case 3: // MIN
          return MIN;
        case 4: // START
          return START;
        case 5: // DISPLAY_UNIT
          return DISPLAY_UNIT;
        case 6: // QUANTITY
          return QUANTITY;
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
  private static final int __MAX_ISSET_ID = 0;
  private static final int __MIN_ISSET_ID = 1;
  private static final int __START_ISSET_ID = 2;
  private byte __isset_bitfield = 0;
  private static final _Fields optionals[] = {_Fields.MAX,_Fields.MIN,_Fields.START};
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.CLASS_PATH, new org.apache.thrift.meta_data.FieldMetaData("classPath", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.MAX, new org.apache.thrift.meta_data.FieldMetaData("max", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.DOUBLE)));
    tmpMap.put(_Fields.MIN, new org.apache.thrift.meta_data.FieldMetaData("min", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.DOUBLE)));
    tmpMap.put(_Fields.START, new org.apache.thrift.meta_data.FieldMetaData("start", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.DOUBLE)));
    tmpMap.put(_Fields.DISPLAY_UNIT, new org.apache.thrift.meta_data.FieldMetaData("displayUnit", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.QUANTITY, new org.apache.thrift.meta_data.FieldMetaData("quantity", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ModelicaAttr.class, metaDataMap);
  }

  public ModelicaAttr() {
    this.displayUnit = "";

    this.quantity = "";

  }

  public ModelicaAttr(
    String classPath,
    String displayUnit,
    String quantity)
  {
    this();
    this.classPath = classPath;
    this.displayUnit = displayUnit;
    this.quantity = quantity;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ModelicaAttr(ModelicaAttr other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetClassPath()) {
      this.classPath = other.classPath;
    }
    this.max = other.max;
    this.min = other.min;
    this.start = other.start;
    if (other.isSetDisplayUnit()) {
      this.displayUnit = other.displayUnit;
    }
    if (other.isSetQuantity()) {
      this.quantity = other.quantity;
    }
  }

  public ModelicaAttr deepCopy() {
    return new ModelicaAttr(this);
  }

  @Override
  public void clear() {
    this.classPath = null;
    setMaxIsSet(false);
    this.max = 0.0;
    setMinIsSet(false);
    this.min = 0.0;
    setStartIsSet(false);
    this.start = 0.0;
    this.displayUnit = "";

    this.quantity = "";

  }

  public String getClassPath() {
    return this.classPath;
  }

  public ModelicaAttr setClassPath(String classPath) {
    this.classPath = classPath;
    return this;
  }

  public void unsetClassPath() {
    this.classPath = null;
  }

  /** Returns true if field classPath is set (has been assigned a value) and false otherwise */
  public boolean isSetClassPath() {
    return this.classPath != null;
  }

  public void setClassPathIsSet(boolean value) {
    if (!value) {
      this.classPath = null;
    }
  }

  public double getMax() {
    return this.max;
  }

  public ModelicaAttr setMax(double max) {
    this.max = max;
    setMaxIsSet(true);
    return this;
  }

  public void unsetMax() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __MAX_ISSET_ID);
  }

  /** Returns true if field max is set (has been assigned a value) and false otherwise */
  public boolean isSetMax() {
    return EncodingUtils.testBit(__isset_bitfield, __MAX_ISSET_ID);
  }

  public void setMaxIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __MAX_ISSET_ID, value);
  }

  public double getMin() {
    return this.min;
  }

  public ModelicaAttr setMin(double min) {
    this.min = min;
    setMinIsSet(true);
    return this;
  }

  public void unsetMin() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __MIN_ISSET_ID);
  }

  /** Returns true if field min is set (has been assigned a value) and false otherwise */
  public boolean isSetMin() {
    return EncodingUtils.testBit(__isset_bitfield, __MIN_ISSET_ID);
  }

  public void setMinIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __MIN_ISSET_ID, value);
  }

  public double getStart() {
    return this.start;
  }

  public ModelicaAttr setStart(double start) {
    this.start = start;
    setStartIsSet(true);
    return this;
  }

  public void unsetStart() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __START_ISSET_ID);
  }

  /** Returns true if field start is set (has been assigned a value) and false otherwise */
  public boolean isSetStart() {
    return EncodingUtils.testBit(__isset_bitfield, __START_ISSET_ID);
  }

  public void setStartIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __START_ISSET_ID, value);
  }

  public String getDisplayUnit() {
    return this.displayUnit;
  }

  public ModelicaAttr setDisplayUnit(String displayUnit) {
    this.displayUnit = displayUnit;
    return this;
  }

  public void unsetDisplayUnit() {
    this.displayUnit = null;
  }

  /** Returns true if field displayUnit is set (has been assigned a value) and false otherwise */
  public boolean isSetDisplayUnit() {
    return this.displayUnit != null;
  }

  public void setDisplayUnitIsSet(boolean value) {
    if (!value) {
      this.displayUnit = null;
    }
  }

  public String getQuantity() {
    return this.quantity;
  }

  public ModelicaAttr setQuantity(String quantity) {
    this.quantity = quantity;
    return this;
  }

  public void unsetQuantity() {
    this.quantity = null;
  }

  /** Returns true if field quantity is set (has been assigned a value) and false otherwise */
  public boolean isSetQuantity() {
    return this.quantity != null;
  }

  public void setQuantityIsSet(boolean value) {
    if (!value) {
      this.quantity = null;
    }
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case CLASS_PATH:
      if (value == null) {
        unsetClassPath();
      } else {
        setClassPath((String)value);
      }
      break;

    case MAX:
      if (value == null) {
        unsetMax();
      } else {
        setMax((Double)value);
      }
      break;

    case MIN:
      if (value == null) {
        unsetMin();
      } else {
        setMin((Double)value);
      }
      break;

    case START:
      if (value == null) {
        unsetStart();
      } else {
        setStart((Double)value);
      }
      break;

    case DISPLAY_UNIT:
      if (value == null) {
        unsetDisplayUnit();
      } else {
        setDisplayUnit((String)value);
      }
      break;

    case QUANTITY:
      if (value == null) {
        unsetQuantity();
      } else {
        setQuantity((String)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case CLASS_PATH:
      return getClassPath();

    case MAX:
      return Double.valueOf(getMax());

    case MIN:
      return Double.valueOf(getMin());

    case START:
      return Double.valueOf(getStart());

    case DISPLAY_UNIT:
      return getDisplayUnit();

    case QUANTITY:
      return getQuantity();

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case CLASS_PATH:
      return isSetClassPath();
    case MAX:
      return isSetMax();
    case MIN:
      return isSetMin();
    case START:
      return isSetStart();
    case DISPLAY_UNIT:
      return isSetDisplayUnit();
    case QUANTITY:
      return isSetQuantity();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof ModelicaAttr)
      return this.equals((ModelicaAttr)that);
    return false;
  }

  public boolean equals(ModelicaAttr that) {
    if (that == null)
      return false;

    boolean this_present_classPath = true && this.isSetClassPath();
    boolean that_present_classPath = true && that.isSetClassPath();
    if (this_present_classPath || that_present_classPath) {
      if (!(this_present_classPath && that_present_classPath))
        return false;
      if (!this.classPath.equals(that.classPath))
        return false;
    }

    boolean this_present_max = true && this.isSetMax();
    boolean that_present_max = true && that.isSetMax();
    if (this_present_max || that_present_max) {
      if (!(this_present_max && that_present_max))
        return false;
      if (this.max != that.max)
        return false;
    }

    boolean this_present_min = true && this.isSetMin();
    boolean that_present_min = true && that.isSetMin();
    if (this_present_min || that_present_min) {
      if (!(this_present_min && that_present_min))
        return false;
      if (this.min != that.min)
        return false;
    }

    boolean this_present_start = true && this.isSetStart();
    boolean that_present_start = true && that.isSetStart();
    if (this_present_start || that_present_start) {
      if (!(this_present_start && that_present_start))
        return false;
      if (this.start != that.start)
        return false;
    }

    boolean this_present_displayUnit = true && this.isSetDisplayUnit();
    boolean that_present_displayUnit = true && that.isSetDisplayUnit();
    if (this_present_displayUnit || that_present_displayUnit) {
      if (!(this_present_displayUnit && that_present_displayUnit))
        return false;
      if (!this.displayUnit.equals(that.displayUnit))
        return false;
    }

    boolean this_present_quantity = true && this.isSetQuantity();
    boolean that_present_quantity = true && that.isSetQuantity();
    if (this_present_quantity || that_present_quantity) {
      if (!(this_present_quantity && that_present_quantity))
        return false;
      if (!this.quantity.equals(that.quantity))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    List<Object> list = new ArrayList<Object>();

    boolean present_classPath = true && (isSetClassPath());
    list.add(present_classPath);
    if (present_classPath)
      list.add(classPath);

    boolean present_max = true && (isSetMax());
    list.add(present_max);
    if (present_max)
      list.add(max);

    boolean present_min = true && (isSetMin());
    list.add(present_min);
    if (present_min)
      list.add(min);

    boolean present_start = true && (isSetStart());
    list.add(present_start);
    if (present_start)
      list.add(start);

    boolean present_displayUnit = true && (isSetDisplayUnit());
    list.add(present_displayUnit);
    if (present_displayUnit)
      list.add(displayUnit);

    boolean present_quantity = true && (isSetQuantity());
    list.add(present_quantity);
    if (present_quantity)
      list.add(quantity);

    return list.hashCode();
  }

  @Override
  public int compareTo(ModelicaAttr other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetClassPath()).compareTo(other.isSetClassPath());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetClassPath()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.classPath, other.classPath);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetMax()).compareTo(other.isSetMax());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetMax()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.max, other.max);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetMin()).compareTo(other.isSetMin());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetMin()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.min, other.min);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetStart()).compareTo(other.isSetStart());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetStart()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.start, other.start);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetDisplayUnit()).compareTo(other.isSetDisplayUnit());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDisplayUnit()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.displayUnit, other.displayUnit);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetQuantity()).compareTo(other.isSetQuantity());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetQuantity()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.quantity, other.quantity);
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
    StringBuilder sb = new StringBuilder("ModelicaAttr(");
    boolean first = true;

    sb.append("classPath:");
    if (this.classPath == null) {
      sb.append("null");
    } else {
      sb.append(this.classPath);
    }
    first = false;
    if (isSetMax()) {
      if (!first) sb.append(", ");
      sb.append("max:");
      sb.append(this.max);
      first = false;
    }
    if (isSetMin()) {
      if (!first) sb.append(", ");
      sb.append("min:");
      sb.append(this.min);
      first = false;
    }
    if (isSetStart()) {
      if (!first) sb.append(", ");
      sb.append("start:");
      sb.append(this.start);
      first = false;
    }
    if (!first) sb.append(", ");
    sb.append("displayUnit:");
    if (this.displayUnit == null) {
      sb.append("null");
    } else {
      sb.append(this.displayUnit);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("quantity:");
    if (this.quantity == null) {
      sb.append("null");
    } else {
      sb.append(this.quantity);
    }
    first = false;
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

  private static class ModelicaAttrStandardSchemeFactory implements SchemeFactory {
    public ModelicaAttrStandardScheme getScheme() {
      return new ModelicaAttrStandardScheme();
    }
  }

  private static class ModelicaAttrStandardScheme extends StandardScheme<ModelicaAttr> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, ModelicaAttr struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // CLASS_PATH
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.classPath = iprot.readString();
              struct.setClassPathIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // MAX
            if (schemeField.type == org.apache.thrift.protocol.TType.DOUBLE) {
              struct.max = iprot.readDouble();
              struct.setMaxIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // MIN
            if (schemeField.type == org.apache.thrift.protocol.TType.DOUBLE) {
              struct.min = iprot.readDouble();
              struct.setMinIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // START
            if (schemeField.type == org.apache.thrift.protocol.TType.DOUBLE) {
              struct.start = iprot.readDouble();
              struct.setStartIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 5: // DISPLAY_UNIT
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.displayUnit = iprot.readString();
              struct.setDisplayUnitIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 6: // QUANTITY
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.quantity = iprot.readString();
              struct.setQuantityIsSet(true);
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

    public void write(org.apache.thrift.protocol.TProtocol oprot, ModelicaAttr struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.classPath != null) {
        oprot.writeFieldBegin(CLASS_PATH_FIELD_DESC);
        oprot.writeString(struct.classPath);
        oprot.writeFieldEnd();
      }
      if (struct.isSetMax()) {
        oprot.writeFieldBegin(MAX_FIELD_DESC);
        oprot.writeDouble(struct.max);
        oprot.writeFieldEnd();
      }
      if (struct.isSetMin()) {
        oprot.writeFieldBegin(MIN_FIELD_DESC);
        oprot.writeDouble(struct.min);
        oprot.writeFieldEnd();
      }
      if (struct.isSetStart()) {
        oprot.writeFieldBegin(START_FIELD_DESC);
        oprot.writeDouble(struct.start);
        oprot.writeFieldEnd();
      }
      if (struct.displayUnit != null) {
        oprot.writeFieldBegin(DISPLAY_UNIT_FIELD_DESC);
        oprot.writeString(struct.displayUnit);
        oprot.writeFieldEnd();
      }
      if (struct.quantity != null) {
        oprot.writeFieldBegin(QUANTITY_FIELD_DESC);
        oprot.writeString(struct.quantity);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ModelicaAttrTupleSchemeFactory implements SchemeFactory {
    public ModelicaAttrTupleScheme getScheme() {
      return new ModelicaAttrTupleScheme();
    }
  }

  private static class ModelicaAttrTupleScheme extends TupleScheme<ModelicaAttr> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, ModelicaAttr struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetClassPath()) {
        optionals.set(0);
      }
      if (struct.isSetMax()) {
        optionals.set(1);
      }
      if (struct.isSetMin()) {
        optionals.set(2);
      }
      if (struct.isSetStart()) {
        optionals.set(3);
      }
      if (struct.isSetDisplayUnit()) {
        optionals.set(4);
      }
      if (struct.isSetQuantity()) {
        optionals.set(5);
      }
      oprot.writeBitSet(optionals, 6);
      if (struct.isSetClassPath()) {
        oprot.writeString(struct.classPath);
      }
      if (struct.isSetMax()) {
        oprot.writeDouble(struct.max);
      }
      if (struct.isSetMin()) {
        oprot.writeDouble(struct.min);
      }
      if (struct.isSetStart()) {
        oprot.writeDouble(struct.start);
      }
      if (struct.isSetDisplayUnit()) {
        oprot.writeString(struct.displayUnit);
      }
      if (struct.isSetQuantity()) {
        oprot.writeString(struct.quantity);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, ModelicaAttr struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(6);
      if (incoming.get(0)) {
        struct.classPath = iprot.readString();
        struct.setClassPathIsSet(true);
      }
      if (incoming.get(1)) {
        struct.max = iprot.readDouble();
        struct.setMaxIsSet(true);
      }
      if (incoming.get(2)) {
        struct.min = iprot.readDouble();
        struct.setMinIsSet(true);
      }
      if (incoming.get(3)) {
        struct.start = iprot.readDouble();
        struct.setStartIsSet(true);
      }
      if (incoming.get(4)) {
        struct.displayUnit = iprot.readString();
        struct.setDisplayUnitIsSet(true);
      }
      if (incoming.get(5)) {
        struct.quantity = iprot.readString();
        struct.setQuantityIsSet(true);
      }
    }
  }

}
