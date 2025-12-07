# Define the Maple executable and the files to be processed
MAPLE_EXEC := maple
INPUT_FILES := $(wildcard Input/*)

# Outputs per mode
OUTPUT_FILE_NEW := results_newmethod.output
OUTPUT_FILE_OLD := results_oldmethod.output

# Benchmarks per mode
BENCHMARKING_FILE_NEW := BENCHMARKING_results_newmethod.output
BENCHMARKING_FILE_OLD := BENCHMARKING_results_oldmethod.output

# Crash log (shared)
CRASH_LOG := crash_log.txt

# Ensure input files exist
ifeq ($(strip $(INPUT_FILES)),)
$(error "No input files found in Input/")
endif

.PHONY: all test test_newmethod test_oldmethod clean

# Default target
all: test

# Run both modes
test: test_newmethod test_oldmethod

# -----------------------------
# newmethod
# -----------------------------
test_newmethod: $(OUTPUT_FILE_NEW) $(BENCHMARKING_FILE_NEW)

$(OUTPUT_FILE_NEW): $(INPUT_FILES)
	@echo "Running IntegerHull tests (mode = newmethod)"
	@rm -f $(OUTPUT_FILE_NEW) $(BENCHMARKING_FILE_NEW) $(CRASH_LOG)
	@for file in $(INPUT_FILES); do \
		echo "Running test: $$file"; \
		ulimit -t 600; \
		ulimit -m 11534336; \
		echo "LoopI := \"$$file\"; ModeCall := newmethod;" | cat - benchmarking.tst > temp.tst; \
		$(MAPLE_EXEC) < temp.tst > temp_output 2>&1; \
		cat temp_output >> $(OUTPUT_FILE_NEW); \
		if grep -q "Error," temp_output; then \
			echo "Crash detected for file: $$file" >> $(CRASH_LOG); \
			echo "Mode: newmethod" >> $(CRASH_LOG); \
			grep "Error," temp_output >> $(CRASH_LOG); \
			echo "------------------------------------" >> $(CRASH_LOG); \
		fi; \
		rm -f temp.tst temp_output; \
	done

$(BENCHMARKING_FILE_NEW): $(OUTPUT_FILE_NEW)
	@echo "Benchmark for IntegerHull tests (mode = newmethod)"
	@grep -A13 "\"newmethod time for\", \"" $(OUTPUT_FILE_NEW) > $(BENCHMARKING_FILE_NEW)
	@rm -f $(OUTPUT_FILE_NEW)

# -----------------------------
# oldmethod
# -----------------------------
test_oldmethod: $(OUTPUT_FILE_OLD) $(BENCHMARKING_FILE_OLD)

$(OUTPUT_FILE_OLD): $(INPUT_FILES)
	@echo "Running IntegerHull tests (mode = oldmethod)"
	@rm -f $(OUTPUT_FILE_OLD) $(BENCHMARKING_FILE_OLD) $(CRASH_LOG)
	@for file in $(INPUT_FILES); do \
		echo "Running test: $$file"; \
		ulimit -t 600; \
		ulimit -m 11534336; \
		echo "LoopI := \"$$file\"; ModeCall := oldmethod;" | cat - benchmarking.tst > temp.tst; \
		$(MAPLE_EXEC) < temp.tst > temp_output 2>&1; \
		cat temp_output >> $(OUTPUT_FILE_OLD); \
		if grep -q "Error," temp_output; then \
			echo "Crash detected for file: $$file" >> $(CRASH_LOG); \
			echo "Mode: oldmethod" >> $(CRASH_LOG); \
			grep "Error," temp_output >> $(CRASH_LOG); \
			echo "------------------------------------" >> $(CRASH_LOG); \
		fi; \
		rm -f temp.tst temp_output; \
	done

$(BENCHMARKING_FILE_OLD): $(OUTPUT_FILE_OLD)
	@echo "Benchmark for IntegerHull tests (mode = oldmethod)"
	@grep -A13 "\"oldmethod time for\", \"" $(OUTPUT_FILE_OLD) > $(BENCHMARKING_FILE_OLD)
	@rm -f $(OUTPUT_FILE_OLD)

# Clean up any generated files
clean:
	rm -f \
	  $(OUTPUT_FILE_NEW) $(BENCHMARKING_FILE_NEW) \
	  $(OUTPUT_FILE_OLD) $(BENCHMARKING_FILE_OLD) \
	  $(CRASH_LOG) temp.tst temp_output
