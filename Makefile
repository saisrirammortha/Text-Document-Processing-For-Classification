# Karan Bajaj

#### local macros
RM = /bin/rm -f

# compiler name and flags
CCC = gcc
CCFLAGS = -O3 -fomit-frame-pointer -funroll-loops -fforce-addr -fexpensive-optimizations
# -fforce-mem

# loader flags
LDFLAGS = 

### local program information
EXEC=conversion
SOURCES= conversion.c

### intermediate objects
OBJECTS = $(SOURCES: .c=.o)

### includes
INCLUDES = 

### headers
HEADERS =

### targets, dependencies and actions
$(EXEC): $(OBJECTS) Makefile
	$(LINK.c) $(CCFLAGS) -o $(EXEC) $(OBJECTS)

### sort out dependencies
depend:
	makedepend $(INCLUDES) $(HEADERS) $(SOURCES)

### housekeeping

clean:
	$(RM) *.o *~

cleanall: clean
	$(RM) $(EXEC)
