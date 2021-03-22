all: qaudio qaudio_library clean

qaudio:
	@echo "Compiling..."
	gcc -fPIC -c src/qaudio.c -o libqaudio.o

qaudio_library:
	@echo "Building shared library..."
	gcc libqaudio.o -shared -lpulse-simple -lpulse -o libqaudio.so

clean:
	@echo "Cleaning..."
	@rm "libqaudio.o"

	@echo "DONE!"