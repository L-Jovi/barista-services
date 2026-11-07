## Notice

`setout.sh` prepares JavaScript patch files for Upyun. It copies the development files from `local/` into `cloud/`, then offers a separate upload step.

Copying and uploading are distinct actions: creating the files under `cloud/` does not mean they have been uploaded. Check the script's source paths, target paths, and upload configuration before using it.
