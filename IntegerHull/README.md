# IntegerHull

The **IntegerHull** package is written in [Maple](https://www.maplesoft.com/) and implements a new algorithm for computing the **integer hull** of a rational polyhedral set. It provides:

- **NewIntegerHull** — our optimized integer-hull algorithm  
- **IntegerHull** — Maple’s original integer-hull method (kept for comparison)

This package integrates with the **PolyhedralSets** Maple library and includes the full benchmarking framework used in our experimentation.


## Installation Guide
This package can be installed as follows:
1. Clone or Download this repository (i.e. `https://github.com/mukherjeechirantan/PolyhedralSets-Software.git`)
2. Navigate to the repository folder (i.e. `cd ./IntegerHull`)
3. Copy the full path of `master.mla` by running `pwd`
4. Edit your Maple initialization file `~/.mapleinit` using `libname :=  "<path>", libname:`

After successful installation `master.mla` will be integrated into your Maple environment. 
Note that `<path>` should be replaced with the full path to where `master.mla` is located.

In addition to installing the package, you also need to have Maple installed to view the demo. You can download Maple from their [official website](https://www.maplesoft.com/).

## Usage and Documentation
This package can be loaded in Maple by using `with(IntegerHull);`. This command also displays all available functions.

Compute the integer hull using the new algorithm: `IntegerHull(P, mode = newmethod);`

Compute using Maple’s default integer-hull method: `IntegerHull(P, mode = oldmethod);` 

If no options are provided, the function runs with `mode = oldmethod`.
