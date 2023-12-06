echo "random 16384 1 128"
python3 code/sim.py random 16384 1 128 > results/random_16384_1_128.txt
echo "random 16384 4 128"
python3 code/sim.py random 16384 4 128 > results/random_16384_4_128.txt
echo "random 16384 16 128"
python3 code/sim.py random 16384 16 128 > results/random_16384_16_128.txt

echo "random 16384 1 512"
python3 code/sim.py random 16384 1 512 > results/random_16384_1_512.txt
echo "random 16384 4 512"
python3 code/sim.py random 16384 4 512 > results/random_16384_4_512.txt
echo "random 16384 16 512"
python3 code/sim.py random 16384 16 512 > results/random_16384_16_512.txt

echo "random 16384 1 4096"
python3 code/sim.py random 16384 1 4096 > results/random_16384_1_4096.txt
echo "random 16384 4 4096"
python3 code/sim.py random 16384 4 4096 > results/random_16384_4_4096.txt
echo "random 16384 16 4096"
python3 code/sim.py random 16384 16 4096 > results/random_16384_16_4096.txt


echo "lru 16384 1 128"
python3 code/sim.py lru 16384 1 128 > results/lru_16384_1_128.txt
echo "lru 16384 4 128"
python3 code/sim.py lru 16384 4 128 > results/lru_16384_4_128.txt
echo "lru 16384 16 128"
python3 code/sim.py lru 16384 16 128 > results/lru_16384_16_128.txt

echo "lru 16384 1 512"
python3 code/sim.py lru 16384 1 512 > results/lru_16384_1_512.txt
echo "lru 16384 4 512"
python3 code/sim.py lru 16384 4 512 > results/lru_16384_4_512.txt
echo "lru 16384 16 512"
python3 code/sim.py lru 16384 16 512 > results/lru_16384_16_512.txt

echo "lru 16384 1 4096"
python3 code/sim.py lru 16384 1 4096 > results/lru_16384_1_4096.txt
echo "lru 16384 4 4096"
python3 code/sim.py lru 16384 4 4096 > results/lru_16384_4_4096.txt
echo "lru 16384 16 4096"
python3 code/sim.py lru 16384 16 4096 > results/lru_16384_16_4096.txt


echo "lfu 16384 1 128"
python3 code/sim.py lfu 16384 1 128 > results/lfu_16384_1_128.txt
echo "lfu 16384 4 128"
python3 code/sim.py lfu 16384 4 128 > results/lfu_16384_4_128.txt
echo "lfu 16384 16 128"
python3 code/sim.py lfu 16384 16 128 > results/lfu_16384_16_128.txt

echo "lfu 16384 1 512"
python3 code/sim.py lfu 16384 1 512 > results/lfu_16384_1_512.txt
echo "lfu 16384 4 512"
python3 code/sim.py lfu 16384 4 512 > results/lfu_16384_4_512.txt
echo "lfu 16384 16 512"
python3 code/sim.py lfu 16384 16 512 > results/lfu_16384_16_512.txt

echo "lfu 16384 1 4096"
python3 code/sim.py lfu 16384 1 4096 > results/lfu_16384_1_4096.txt
echo "lfu 16384 4 4096"
python3 code/sim.py lfu 16384 4 4096 > results/lfu_16384_4_4096.txt
echo "lfu 16384 16 4096"
python3 code/sim.py lfu 16384 16 4096 > results/lfu_16384_16_4096.txt

