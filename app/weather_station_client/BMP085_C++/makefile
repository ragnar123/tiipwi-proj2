CXXFLAGS += -g -Wall -O2

BMP085.o: BMP085.cpp BMP085.hpp

demo: demo.cpp BMP085.o
	$(CXX) $(CXXFLAGS) demo.cpp BMP085.o -o demo

clean:
	@-rm *.o *.a *.so *.gch *.log
	@-rm test demo a.out
