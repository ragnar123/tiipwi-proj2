configuration TempTestAppC
{
	
}

implementation
{
	// General components
	components TempTestC as App;
	components MainC, LedsC;
	components new TimerMilliC();
	
	App.Boot -> MainC;
	App.Leds -> LedsC;
	App.Timer -> TimerMilliC;
	
	// For writing to serial port
	components SerialPrintfC;
	
	// Temperature component
	components new SensirionSht11C() as TempSensor;
	
	App.TempRead -> TempSensor.Temperature;
	
	// Light component
	components new HamamatsuS10871TsrC() as LightSensor;
	App.LightRead -> LightSensor;
}