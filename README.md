![EmblemaFuegoControl](https://user-images.githubusercontent.com/38228291/67335050-6ba2c280-f523-11e9-93c5-928435fdd118.png)
# Radiative transfer

## How to run the program
- Before running the program make sure you have the necessary requirements, clone the repository and run the program in your terminal.

   > git clone https://github.com/la-nacion-del-fuego/Radiacion-en-la-Piel.git
   
   > cd Radiacion-en-la-Piel/  
   
   > python3 ./rte.py

## Introduction
In this modeling and simulation project we will work with radiation and the theory of radiative transport, this research was developed mainly by the physicist-mathematician Subrahmanyan Chandrasekhar of Indian origin. We with that theory will simulate a ray of radiation that travels and makes contact with the skin of various parts of the human body , the energy of said ray will be lost to be absorbed but also that same energy will be distributed by dispersion.

## Abstract
In this project we focus especially on the radiative transfer equation, which tells us that a traveling radiation beam will lose energy by absorption, will gain energy by emission and redistribute energy by dispersion.

Our idea used in this project is to use this equation to visualize the absorption coefficient that the skin has exposed to a ray of solar radiation.

To better perform our simulation we will keep in mind that we will work with human skin which is made up of multiple layers, from the Epidermis which contains the stratum corneum, lucid stratum, granular stratum, spiny stratum and the basal stratum. Said layer measures at least 0.1mm deep. Then the Dermis would come and finally the hypodermis. All these layers alter the coefficient of absorption of the skin, apart from that we also have melanin which helps to avoid being damaged by UV rays.

having thus more complete the idea on which we will work it is necessary to establish our objective which is:
- Visualize the absorption of a radiation beam in human skin, calculating its coefficient and how it decreases as the radiation beam enters the human skin.
![images](https://user-images.githubusercontent.com/38228291/71786960-ee5ef800-3011-11ea-92ce-2d450fbc3427.png)
## Methodology 
- We will begin our model knowing that the absorption of the radiation beam on the surface of the epidermis will be very low and that the skin is not a radiation emitter therefore as it travels deeper into it, the absorption increases.

- The necessary variables for our model are:
>>- k: = Skin opacity, k (𝜆) cm-1
>>- dx: = It will be calculated every 0.1mm
>>- τ: = Optical depth, 𝜏 (dx, 𝜆)
>>- 𝜆: = It is the wavelength, 500 name this document
>>- N: = It is the number of iterations
>>- I0: = Is the initial intensity
>>- Iv: = Is the intensity at point v
- already working on the code, the first thing was to establish the software license and import the libraries that we will use.
- Now we will implement the opacity function **"def k"** that reveals how much transparency human skin has.
- The next thing will be to add the **"tau"** function to calculate the visual depth, this to know how far the light reaches the skin.
- Then we will add labels to improve the visualization of the results and to be able to choose from our viable options which part of the body to simulate.
- The next thing we implemented was a cycle which is responsible for modeling the radiative transfer for all layers of the skin.
- The following will be to print all the graphics of the iteration of different parts of the body in a single image.
- finally we will implement another cycle that will take X and Y to make the graphics and give them colors, title, label on the X and Y axis and then save the graphics as an example of all the parts of the body where we are going to simulate, among them are; heel of the foot, eyelid, abdomen of obese and thin people
## Outcome:
The graph shows the absorption when a ray of sunlight that travels in 90 ° and without any deviation or object that crosses it meets the heel skin. This shows its specific intensity in its total making contact with the skin and descending until traveling by 10 millimeters where from 9 already stops absorbing when its passage through the foot bone is blocked.

![Ejemplo](https://user-images.githubusercontent.com/38228291/71790090-ea8d9e80-302e-11ea-83a6-f4d80699d3dd.jpg)

Following the example above but now in other parts of the body we have the following results:

![unnamed (3)](https://user-images.githubusercontent.com/38228291/71790378-6805de80-3030-11ea-995a-b08f2048f369.jpg)
![unnamed](https://user-images.githubusercontent.com/38228291/71790396-81a72600-3030-11ea-90f8-299a59199fa2.jpg)
![unnamed (1)](https://user-images.githubusercontent.com/38228291/71790404-8d92e800-3030-11ea-9083-4da5eb9babf1.jpg)
![unnamed (2)](https://user-images.githubusercontent.com/38228291/71790409-9a174080-3030-11ea-9967-85a2615ec8c5.jpg)

## Bibliography
- [Vitamin D obtained by sunlight](http://www.fundaciondn.org/reto/la-vitamina-d-la-de-la-luz-del-sol/?fbclid=IwAR2u47-OlbKQqV20ZUsU_-hjoF41DZp2SRDyKN9KwALsftvezPtMaA5GKqM)
- [Vitamin D information](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3897598/?fbclid=IwAR2aO93VCq1d-P38d-78dmIxr7gtQLNWCd_FlABwEJEpYLZssLmnR_uovio)
- [Determining an Effective UV Radiation Exposure Time for Vitamin D Synthesis](https://onlinelibrary.wiley.com/doi/full/10.1111/php.12651)
- [Instrumental Measurements of Skin Color and Skin Ultraviolet Light Sensitivity](https://academic.oup.com/aje/article/156/4/353/112408)
- [Mathematical descriptions of opacity](https://en.wikipedia.org/wiki/Mathematical_descriptions_of_opacity)
- [Penetration depth](https://en.wikipedia.org/wiki/Penetration_depth)
- [Do white people have melanin?](https://www.quora.com/Do-white-people-have-melanin)
- [Descriptive statistics for instrumental measurements of skin color and skin sensitivity](https://academic.oup.com/view-large/867813)
- [graph showing the change of vitamin D in two subjects with different skin tone exposed to UVR rays](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3897598/figure/F33/)
- [The wavelength range of optical radiation](https://light-measurement.com/wavelength-range/?fbclid=IwAR0e8eht2FegvKUaKIGRH4NbMUdpR1__XrhesbgqO9w2EURHxQeKXcd4asQ)
- [Skin Permeability](https://www.sciencedirect.com/topics/medicine-and-dentistry/skin-permeability)
- [Dermal exposure to chemicals in the workplace: just how important is skin absorption?](https://oem.bmj.com/content/61/4/376.full)
- [The Appearance of Human Skin](http://www1.cs.columbia.edu/CAVE/publications/pdfs/Igarashi_CUTR05.pdf)
- [Quantitative and Qualitative Measurement Of Skin Color](http://www.cedlabs.com/wp-content/uploads/2014/08/Color-de-la-piel.pdf)
- [image of sun and skin](https://www.google.com/search?q=luz+solar+en+la+piel+dibujo&tbm=isch&ved=2ahUKEwjTrPuxv-3mAhVuma0KHQDCBj0Q2-cCegQIABAA&oq=luz+solar+en+la+piel+dibujo&gs_l=img.3...9327.10678..10978...0.0..0.128.804.0j7......0....1..gws-wiz-img.fy7NnsWIh9c&ei=XmESXtOFKe6ytgWAhJvoAw&bih=608&biw=1366&rlz=1C1CHBF_esMX810MX810&hl=es-419#imgrc=oO0zdwyT7k5wRM)
- [Image of the fire nation](https://www.google.com/search?q=icono+nacion+del+fuego&rlz=1C1CHBF_esMX810MX810&sxsrf=ACYBGNQBf63ha8ZuphTKoJyBet7DIcMDYQ:1578263747956&tbm=isch&source=iu&ictx=1&fir=z_gOm1JpHyiNIM%253A%252CiJVVPGZI0opoaM%252C_&vet=1&usg=AI4_-kTvyOBniqJ5OpJ5eMbeiXlamUUOdw&sa=X&ved=2ahUKEwik6bvQwu3mAhWEna0KHSqwCHUQ9QEwAHoECAoQBg#imgrc=z_gOm1JpHyiNIM:)
