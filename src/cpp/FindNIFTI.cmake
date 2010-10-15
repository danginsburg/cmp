FIND_PATH(NIFTI_INCLUDE_DIR
	nifti1.h
	/usr/local/include/nifti /usr/include/nifti
)


IF (NIFTI_INCLUDE_DIR)
   SET(NIFTI_FOUND TRUE)
ENDIF (NIFTI_INCLUDE_DIR)


IF (NIFTI_FOUND)
   IF (NOT NIFTI_FIND_QUIETLY)
      MESSAGE(STATUS "Found NIFTI: ${NIFTI_LIBRARY}")
   ENDIF (NOT NIFTI_FIND_QUIETLY)
ELSE (NIFTI_FOUND)
   IF (NIFTI_FIND_REQUIRED)
      MESSAGE(FATAL_ERROR "Could not find NIFTI (which is required)")
   ENDIF (NIFTI_FIND_REQUIRED)
ENDIF (NIFTI_FOUND)