# pylint: skip-file
from gif_template import GifTemplate

gif_url = 'https://media1.tenor.com/images/a42798da3846ddfc1a8a13e3d114e696/tenor.gif?itemid=10569428'

my_gif = GifTemplate('baby', gif_url)
out_gif = my_gif.generate_white_bg_black_impact('congratulations-gif', 'Congratulations, you got the module working!', 42)
out_gif.save_gif_fs("out.gif")