import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description="Concatenate counts after running featureCounts or salmon.")
    parser.add_argument("--type", required=True, help="Input either featureCounts or salmon") #TODO: add other types such as kallisto or stringtie
    parser.add_argument("--samples_list", required=True, help="This is a space separated file where the first column is the sample name and the second column is the path to the counts file")
    parser.add_argument("--outfile", required=True, help="Give the path to the output file")

    return parser.parse_args()

def main():
    args = parse_args()
    df = pd.DataFrame()
    with open(args.samples_list) as file:
        for line in file:
            cols = line.rstrip("\n").split(" ")
            sample_id = cols[0]
            file_path = cols[1]
            if args.type == "featureCounts":
                count = pd.read_csv(file_path, sep="\t", comment='#')
                df[sample_id] = count.iloc[:, 6]
            else:
                count = pd.read_csv(file_path, sep="\t")
                df[sample_id] = count.iloc[:, 4]
    df.to_csv(args.outfile, sep="\t", index=False)

main()