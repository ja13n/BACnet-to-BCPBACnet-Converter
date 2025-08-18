        # Re-pack the modified files back into config.bog
    try:

        with zipfile.ZipFile(bog_file_path, 'w') as bog_file:
            for root, dirs, files in os.walk(temp_bog_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(temp_bog_dir)  # Preserve directory structure
                    bog_file.write(file_path, arcname=arcname)

        shutil.rmtree(temp_bog_dir)  # Clean up
        return True

    except Exception as e:
        logger.error(f"Error during XML modification: {e}")
        shutil.rmtree(temp_bog_dir)  # Clean up
        return False
