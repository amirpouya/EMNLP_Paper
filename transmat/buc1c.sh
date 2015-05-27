echo "Training..."

python train_tm.py -o tm ../bucc/dic.5k.train ../bucc/vectors.en bucc/vectors.de


echo "Testing standard NN retrieval (baseline)"

python test_tm.py tm.txt ../bucc/dic.2k.test ../bucc/vectors.en bucc/vectors.de


echo "Testing GC retrieval with 5000 aditional elements"

python -c 5000 test_tm.py tm.txt test_tm.py tm.txt bucc/dic.2k.test bucc/vectors.en bucc/vectors.de



