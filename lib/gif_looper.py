#!/usr/bin/python
import ffmpeg as ff


## useful thing to get args a filter will expect
# ffmpeg.get_args([insert your input/filter/output])

def gif_looper(seek=0, 
               duration=1,
               input_filename="",
               output_prefix="default_prefix",
               output_format="gif",
               options={}):

    if input_filename == "":
        raise Exception("Input is empty, need an input for gif_looper")
        return False

    # read input file to stream
    input_file = ff.input(input_filename, ss=seek, t=duration).video

    # some transforms, performed sequentially
    # passed via "options" kwarg
    if "palette" in options:
        # palette should always be first
        palette_filename = f'{output_prefix}_palette.png'

        # write out palette
        (
            input_file
            .filter(filter_name="palettegen")
            .output(palette_filename)
            .run(overwrite_output=True)
        )
    
        input_file = (
            ff.filter(
                [
                    input_file,
                    ff.input(palette_filename)
                ],
                filter_name="paletteuse",
                dither="heckbert",
                new=False,
            )
        )

        #input_file = input_file.filter("paletteuse", input_file, palette_file)
    if "scale" in options:
        # scale it, probably should come right after palette so less data needs to passed along.
        # if quality issues, we can look at scaling at the end
        input_file = (
            ff.filter(input_file,
                    filter_name="scale", 
                    w=options['scale']['x'], 
                    h=options['scale']['y'])
        )


    if "rev_and_join" in options:
        rev_input = input_file.video.filter('reverse')
        input_file = ff.concat(input_file, rev_input)
    
    out = ff.output(input_file, f'{output_prefix}.{output_format}', f=output_format)
    out.run(overwrite_output=True)