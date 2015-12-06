#include <Timer.h>
#include <string.h>
#include <stdio.h>

module TempTestC
{
	uses
	{
		interface Boot;
		interface Timer<TMilli>;
		interface Leds;
		
		interface Read<uint16_t> as TempRead;	
		interface Read<uint16_t> as LightRead;	
	}
}
implementation
{
	uint16_t centiGrade;
	uint16_t lux;
	
	event void Boot.booted()
	{
		call Timer.startPeriodic(1000);
		call Leds.led1On();
	}
	
	event void Timer.fired()
	{
		if (call TempRead.read() == SUCCESS) {
			call Leds.led2Toggle();
		} else {
			call Leds.led0Toggle();
		}
		if (call LightRead.read() == SUCCESS) {
			call Leds.led2Toggle();
		} else {
			call Leds.led0Toggle();
		}
		
	}
	
	event void TempRead.readDone(error_t result, uint16_t val)
	{
		if (result == SUCCESS) 
		{
			centiGrade = (-39.6 + 0.01 * val);
			printf("current temp is : %d \r\n", centiGrade);
		} 
		else 
		{
			// something bad happened
			printf("error reading from sensor! \r\n");
		}	
	}

	event void LightRead.readDone(error_t result, uint16_t val){
		if (result == SUCCESS) 
		{
			lux = 2.5 * (((val)/4096.0) * 6250.0);
			printf("current light is : %d \r\n", lux);
		} 
		else 
		{
			// something bad happened
			printf("error reading from sensor! \r\n");
		}	
	}
}