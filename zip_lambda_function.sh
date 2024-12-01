mkdir package
pip install numpy --platform manylinux2014_aarch64 --only-binary=:all: --target ./package
cp lambda_function.py package/
cd package
zip -r ../lambda_function.zip .
cd ..
rm -rf package