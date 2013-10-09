using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt
{
    public class Converter
    {
        public static double ConvertValue(qudt.Unit srcUnit, qudt.Unit dstUnit, double value)
        {
            double s_offset = srcUnit.conversionOffset;
            double s_mult = srcUnit.conversionMultiplier;
            double d_offset = dstUnit.conversionOffset;
            double d_mult = dstUnit.conversionMultiplier;

            return ( ( s_offset - d_offset ) + value ) * ( s_mult / d_mult );
        }
    }
}

namespace qudt4dt.qudt
{
    public partial class Unit
    {
        /// <summary>
        /// Convert a value from this unit to another unit.
        /// </summary>
        /// <param name="dstUnit"></param>
        /// <param name="value"></param>
        /// <returns></returns>
        public double ConvertValueTo(qudt.Unit dstUnit,double value)
        {
            return Converter.ConvertValue(this,dstUnit,value);
        }

        /// <summary>
        /// Convert a value from another unit to this unit.
        /// </summary>
        /// <param name="srcUnit"></param>
        /// <param name="value"></param>
        /// <returns></returns>
        public double ConvertValueFrom(qudt.Unit srcUnit,double value)
        {
            return Converter.ConvertValue(srcUnit, this, value);
        }
    }
}