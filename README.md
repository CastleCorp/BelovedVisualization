# BelovedVisualization
Word frequency in Toni Morrison's 'Beloved'

## Dependencies
 - matplotlib
 - numpy
 - wordcloud

## Running
In the repository `python text-analysis.py <input file>`. As it ships, this would be `python text-analysis.py input.txt`, but the option exists for you to substitute your own text or change the name of the file should the need arise.

When the script is run, it will first create the bar graph which opens in it's own window. Once you close the bar graph window, the script will create the word cloud. Once the word cloud is closed, the script will exit.

### Notes
When you run the script, you will see a warning along the lines of `UserWarning: tight_layout : falling back to Agg renderer
warnings.warn("tight_layout : falling back to Agg renderer")`, which you can ignore. Matplotlib is simply grumpy.
