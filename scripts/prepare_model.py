import os
import subprocess
import shutil

MODEL_NAME = "yolo-v4-tiny-tf"

# repo root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

OMZ_REPO = os.path.join(REPO_ROOT, "open_model_zoo")
OMZ_MODEL_TOOLS = os.path.join(OMZ_REPO, "tools", "model_tools")

MODEL_OUTPUT = os.path.join(
    OMZ_MODEL_TOOLS,
    "public",
    MODEL_NAME,
    "FP16"
)

DEST_MODEL_DIR = os.path.join(REPO_ROOT, "models", "yolo-v4-tiny")


def run_command(cmd, cwd=None):
    print("\nRunning:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def clone_omz():
    if not os.path.exists(OMZ_REPO):
        print("Cloning Open Model Zoo...")
        run_command([
            "git",
            "clone",
            "https://github.com/openvinotoolkit/open_model_zoo.git"
        ])
    else:
        print("Open Model Zoo already exists.")


def download_model():
    model_pb = os.path.join(
        OMZ_MODEL_TOOLS,
        "public",
        MODEL_NAME,
        "yolo-v4-tiny.pb"
    )

    if not os.path.exists(model_pb):
        print("Downloading model...")
        run_command(
            ["python", "downloader.py", "--name", MODEL_NAME],
            cwd=OMZ_MODEL_TOOLS
        )
    else:
        print("Model already downloaded.")


def convert_model():
    xml_model = os.path.join(MODEL_OUTPUT, f"{MODEL_NAME}.xml")

    if not os.path.exists(xml_model):
        print("Converting model to OpenVINO IR...")
        run_command(
            ["python", "converter.py", "--name", MODEL_NAME],
            cwd=OMZ_MODEL_TOOLS
        )
    else:
        print("Model already converted.")


def copy_model():

    src_xml = os.path.join(MODEL_OUTPUT, f"{MODEL_NAME}.xml")
    src_bin = os.path.join(MODEL_OUTPUT, f"{MODEL_NAME}.bin")

    if not os.path.exists(src_xml):
        raise FileNotFoundError(
            f"Converted model not found: {src_xml}"
        )

    os.makedirs(DEST_MODEL_DIR, exist_ok=True)

    shutil.copy(src_xml, DEST_MODEL_DIR)
    shutil.copy(src_bin, DEST_MODEL_DIR)

    print("Model copied to:", DEST_MODEL_DIR)


def main():

    clone_omz()
    download_model()
    convert_model()
    copy_model()

    print("\nModel preparation complete!")


if __name__ == "__main__":
    main()