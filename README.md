# f23-cs6354-project

### Simulating cache:
We created a run.sh bach script which runs all the required python commands and saves their output in .txt files in results directory. In order to run it, do the following in the terminal:

```
chmod +x run.sh
```
```
./run.sh
```

<hr/>

### Analysing the output
After all the files were generated containing all the relevant information for miss ratio in each file for each properties, we created a python script which goes over all the files and creates a meaningful data-structure for us to use it to plot graphs and charts. In order to do that, run the following:

```
cd ./code
```
```
python3 analyser.py
```

After getting the output, we used MS Excel to plot all the data.
