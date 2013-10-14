within ;
package CustomUnitLibraryTest 


extends Modelica.Icons.Package;

  type Velocity = Real (final quantity="Velocity", final unit="mph");

  type VelocityKph =
                  Real (final quantity="Velocity", final unit="kph");

  type SinkRate = Real (final quantity="Velocity", final unit="ft/min");

  type Velocity2D=Velocity[2];

  type Velocity3D=Velocity[3];

annotation (uses(Modelica(version="3.2")));
end CustomUnitLibraryTest;
