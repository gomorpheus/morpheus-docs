Scale Thresholds
----------------

Scale Thresholds are pre-configured settings for auto-scaling Instances. When adding auto-scaling to an instance, existing Scale Thresholds can be selected to determine auto-scaling rules.

Creating Scale Thresholds
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Provisioning -> Automation -> Scale Thresholds``
#. Select :guilabel:`+ ADD`
#. Populate the following:

NAME
 Name of the Scale Threshold
AUTO UPSCALE
  Enable to automatically upscale per Scale Threshold specifications
AUTO DOWNSCALE
  Enable to automatically downscale per Scale Threshold specifications
MIN COUNT
  Minimum node count for Instance. Auto-scaling will not downscale below MIN COUNT, and will auto upscale if the MIN COUNT is not met)
MAX COUNT
  Maximum node count for Instance. Auto-scaling will not upscale past MAX COUNT, and will auto downscale if MAX COUNT is exceeded.
ENABLE MEMORY THRESHOLD
  Check to set auto-scaling by specified memory utilization threshold (%)
MIN MEMORY
  Enter MIN MEMORY % for triggering downscaling.
MAX MEMORY
  Enter MAX MEMORY % for triggering upscaling.
ENABLE DISK THRESHOLD
  Check to set auto-scaling by specified disk utilization threshold (%)
MIN DISK
  Enter MIN DISK % for triggering downscaling.
MAX DISK
  Enter MAX DISK % for triggering upscaling.
ENABLE CPU THRESHOLD
  Check to set auto-scaling by specified overall CPU utilization threshold (%)
MIN CPU
  Enter MIN CPU % for triggering downscaling.
MAX CPU
  Enter MAX CPU % for triggering upscaling.
