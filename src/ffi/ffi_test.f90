module ffi_test
  use, intrinsic:: iso_c_binding
  implicit none

contains

  function add(a, b) result(c) bind(C, name = "ffi_mypackage_add")
    real(c_double):: c
    real(c_double), intent(in):: a, b

    c = a + b

    return
  end function add

end module ffi_test
