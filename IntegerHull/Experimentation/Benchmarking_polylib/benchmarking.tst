## In each row, the first column indicates whether the constraint is an equality (0)
## or inequality (1). The final column corresponds to the constant term

MakePoly := proc(B)
local n :: integer,
      m :: integer,
      i :: integer,
      j :: integer,
      vars :: list,
      P :: list,
      expr;

    # Header:
    # B[1,1] = number of constraints (rows after header)
    # B[1,2] = number of columns = 2 + nvars
    m := B[1,1];          # number of constraints
    n := B[1,2] - 2;      # number of variables

    # Create variables x_1, ..., x_n
    vars := [ seq( convert(cat(x_, j), symbol), j = 1 .. n ) ];

    P := [];

    # Constraint rows: 2 .. m+1
    for i from 2 to m do

        # Linear part: columns 2 .. n+1 are coeffs of vars
        expr := add( B[i, j] * vars[j-1], j = 2 .. n+1 )
                + B[i, n+2];   # last column is constant term

        if B[i,1] = 1 then
            # inequality: expr >= 0
            P := [ op(P), expr >= 0 ];
        elif B[i,1] = 0 then
            # equality: expr = 0
            P := [ op(P), expr = 0 ];
        else
            error "Unexpected eq/ineq flag %1 in row %2", B[i,1], i;
        end if;
    end do;

    return P;
end proc:


print("The polyhedral set is", i, "and method used is", test_type):

fd := fopen(i, READ, TEXT):
m := readdata(fd, integer, 2):
fclose(fd):
fd := fopen(i, READ, TEXT):
B := readdata(fd, integer, m[1, 2]):
z := MakePoly(B):
fclose(fd):

P:= PolyhedralSets:-PolyhedralSet(z):

if test_type = oldmethod then
    print("Time for IntegerHull(mode=oldmethod) for test", i, "is",
          CodeTools:-Usage(PolyhedralSets:-IntegerHull(P, mode=oldmethod),
                           output = ['cputime', 'bytesused']));
elif test_type = newmethod then
    print("Time for IntegerHull(mode=newmethod) for test", i, "is",
          CodeTools:-Usage(PolyhedralSets:-IntegerHull(P, mode=newmethod),
                           output = ['cputime', 'bytesused']));
else
    error "Unknown test_type: %1", test_type;
end if:


