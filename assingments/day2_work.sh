mkdir project
cd project

mkdir dir1
mkdir dir2
mkdir dir3

touch file1.txt file2.txt file3.txt file4.txt
touch shell_script.sh

cp file1.txt ./dir1
cp file2.txt ./dir2

mv dir2/file2.txt dir2/file2name_changed.txt

find . -name "file2name_changed.txt"
chmod +x shell_script.sh

cd ..

tar -cvf project_tarfile.tar.gz
mkdir recoverydir

tar -xzvf project_tarfile.tar.gz ./recoverydir

tar -xzvf project_tarfile.tar.gz -C recoverydir/

find recoverydir

#find => it verifies the final location
#-xzvf => Extracts the tar file
#cp => copies the file content from one file to another file
#mv => renames the existing file name into new file
#touch => used to create new files
#mkdir => used to create th enew directories
#chmod => setting the new permissions or changing/modifying the permissions
#cd => used to change the directory
