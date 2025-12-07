# Define the Maple executable and the files to be processed
MAPLE_EXEC := maple
INPUT_FILES := $(wildcard Input/*)
OUTPUT_FILE_oldmethod := results_oldmethod.output
OUTPUT_FILE_newmethod := results_newmethod.output
BENCHMARKING_FILE_oldmethod := BENCHMARKING_results_oldmethod.output
BENCHMARKING_FILE_newmethod := BENCHMARKING_results_newmethod.output
CRASH_LOG := crash_log.txt

# Ensure input files exist
ifeq ($(strip $(INPUT_FILES)),)
$(error "No input files found in Input/")
endif

.PHONY: all runoldmethod runnewmethod clean

# Target to run all input files through Maple for both methods
all: runoldmethod runnewmethod

############################################################
# oldmethod
############################################################

runoldmethod: $(OUTPUT_FILE_oldmethod) $(BENCHMARKING_FILE_oldmethod)

$(OUTPUT_FILE_oldmethod): $(INPUT_FILES)
	@echo "Running IntegerHull(mode=oldmethod) on input files"
	@rm -f $(OUTPUT_FILE_oldmethod) $(BENCHMARKING_FILE_oldmethod) $(CRASH_LOG)
	@for file in $(INPUT_FILES); do \
		echo "Running IntegerHull(mode=oldmethod): $$file"; \
		ulimit -t 300; \
		ulimit -m 8388608; \
		echo "i := \"$$file\"; test_type := oldmethod;" | cat - benchmarking.tst > temp.tst; \
		$(MAPLE_EXEC) < temp.tst > temp_output 2>&1; \
		cat temp_output >> $(OUTPUT_FILE_oldmethod); \
		if grep -q "Error," temp_output; then \
			echo "Crash detected for file: $$file" >> $(CRASH_LOG); \
			echo "Method: IntegerHull" >> $(CRASH_LOG); \
			echo "Mode: oldmethod" >> $(CRASH_LOG); \
			grep "Error," temp_output >> $(CRASH_LOG); \
			echo "------------------------------------" >> $(CRASH_LOG); \
		fi; \
		rm -f temp.tst temp_output; \
	done

$(BENCHMARKING_FILE_oldmethod): $(OUTPUT_FILE_oldmethod)
	@echo "Benchmark for IntegerHull(mode=oldmethod)"
	@grep -A2 "\"Time for IntegerHull(mode=oldmethod) for test\", \"" $(OUTPUT_FILE_oldmethod) > $(BENCHMARKING_FILE_oldmethod)
	@rm -f $(OUTPUT_FILE_oldmethod)

############################################################
# newmethod
############################################################

runnewmethod: $(OUTPUT_FILE_newmethod) $(BENCHMARKING_FILE_newmethod)

$(OUTPUT_FILE_newmethod): $(INPUT_FILES)
	@echo "Running IntegerHull(mode=newmethod) on input files"
	@rm -f $(OUTPUT_FILE_newmethod) $(BENCHMARKING_FILE_newmethod) $(CRASH_LOG)
	@for file in $(INPUT_FILES); do \
		echo "Running IntegerHull(mode=newmethod): $$file"; \
		ulimit -t 300; \
		ulimit -m 8388608; \
		echo "i := \"$$file\"; test_type := newmethod;" | cat - benchmarking.tst > temp.tst; \
		$(MAPLE_EXEC) < temp.tst > temp_output 2>&1; \
		cat temp_output >> $(OUTPUT_FILE_newmethod); \
		if grep -q "Error," temp_output; then \
			echo "Crash detected for file: $$file" >> $(CRASH_LOG); \
			echo "Method: IntegerHull" >> $(CRASH_LOG); \
			echo "Mode: newmethod" >> $(CRASH_LOG); \
			grep "Error," temp_output >> $(CRASH_LOG); \
			echo "------------------------------------" >> $(CRASH_LOG); \
		fi; \
		rm -f temp.tst temp_output; \
	done

$(BENCHMARKING_FILE_newmethod): $(OUTPUT_FILE_newmethod)
	@echo "Benchmark for IntegerHull(mode=newmethod)"
	@grep -A2 "\"Time for IntegerHull(mode=newmethod) for test\", \"" $(OUTPUT_FILE_newmethod) > $(BENCHMARKING_FILE_newmethod)
	@rm -f $(OUTPUT_FILE_newmethod)

############################################################
# Clean
############################################################

clean:
	rm -f $(BENCHMARKING_FILE_oldmethod) $(OUTPUT_FILE_oldmethod) \
	      $(BENCHMARKING_FILE_newmethod) $(OUTPUT_FILE_newmethod) \
	      $(CRASH_LOG) temp.tst temp_output
