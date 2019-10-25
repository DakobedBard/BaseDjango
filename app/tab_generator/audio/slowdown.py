import ffmpy

def slowdown_audio(filename, slowdown):
    '''
    :param filename:  Pass in the name of a file
    :param -> double slowdown: Factor by which to slow down the audio
    :return: True if successfully made the conversion
    '''
    try:
        ff = ffmpy.FFmpeg(inputs={filename: None}, outputs={"{}{}".format(filename,str(slowdown)): ["-filter:a", "atempo={}"]})
        ff.run()
    except Exception as e:
        print(e)
        return False
    return True