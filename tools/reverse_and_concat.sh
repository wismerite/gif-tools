#!/bin/zsh
# first arg should be seconds to seek to in the third arg
# second arg should be duration to read from input in the third arg
# third arg should be the name of the input file
# fourth arg is the prefix for the new filenames

## there are 6 args
seek=$1
duration=$2
input=$3
output_prefix=$4
output_format=$5

# read input and generate trimmed ${output_format}
ffmpeg -ss $seek -t $duration -i $input -f $output_format new_${output_prefix}.${output_format}
# reverse new, trimmed ${output_format}
ffmpeg -i new_${output_prefix}.${output_format} -filter "reverse" -f $output_format rev_${output_prefix}.${output_format}
# concat trimmed and reverse ${output_format}s to try and make a loop
ffmpeg -i new_${output_prefix}.${output_format} -i rev_${output_prefix}.${output_format} -filter_complex "[0:v] [1:v] concat,scale=480:-1" -f $output_format concat_${output_prefix}.${output_format}
